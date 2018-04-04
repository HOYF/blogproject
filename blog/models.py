# -*- conding:utf-8 -*-

from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.six import python_2_unicode_compatible
import markdown
from django.utils.html import strip_tags

@python_2_unicode_compatible # 装饰器，用于兼容Python2
class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

@python_2_unicode_compatible
class Tag(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

@python_2_unicode_compatible
class Post(models.Model):
    title = models.CharField(max_length=100)
    # 存储比较短的字符串可以使用 CharField，
    # 存储比较长的字符串需要使用 TextField
    body = models.TextField()
    # 文章创建时间
    created_time = models.DateTimeField()
    # 最后一次修改时间
    modified_time = models.DateTimeField()
    # blank=True 表示可以允许空值
    excerpt = models.CharField(max_length=200, blank=True)
    # ForeignKey 一对多关系，一篇文章只能有一个分类，但一个分类可以有多篇文章
    # category = models.ForeignKey(Category)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    # ManyToManyField 多对多关系，一篇文章可以有多个标签，一个标签可以有多篇文章
    tags = models.ManyToManyField(Tag, blank=True)
    # 通过ForeignKey 把文章与User表关联，User表是Django内置但表
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    # 记录阅读量，PositiveIntegerField该类型只允许为正整数或0
    views = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        # reverse()函数，第一个参数 'blog:detail' 指的是blog应用下的 name='detail' 的函数
        # get_absolute_url() 函数会返回类似 /post/255  /post/2 这种格式的url，其中255、2指的是文章id，即pk
        return reverse('blog:detail', kwargs={'pk':self.pk})

    # 该方法首先将自身对应的 views 字段的值 +1，此时数据库中的值还没变，
    # 然后调用 save将更改后的值保存到数据库
    def increase_views(self):
        self.views += 1
        self.save(update_fields=['views']) # 这里使用了update_fields参数来告诉Django只更新数据库中 views 字段的值，以提高效率


    def save(self, *args, **kwargs):
        if not self.excerpt: # 如果没有填写摘要
            md = markdown.Markdown(extensions=[
                'markdown.extensions.extra',
                'markdown.extensions.codehilite',
            ])
            # 先将 Markdown 文本渲染成HTML文本
            # strip_tags 去掉HTML文本的全部标签
            # 从文本摘取 54 个字符赋给 excerpt
            self.excerpt = strip_tags(md.convert(self.body))[:54]
        #     调用父类的 save 方法将数据保存到数据库
        super(Post, self).save(*args, **kwargs)



    # 子类Meta可以指定一些属性来规定这个类该有的一些特性
    class Meta:
        # ordering属性用来指定文章排序方式，[-created_time]按创建时间逆序，
        ordering = ['-created_time']


