from ..models import Post, Category, Tag
from django import template
from django.db.models.aggregates import Count

register = template.Library()

# 返回数据库中前 num 篇文章
@register.simple_tag
def get_recent_posts(num=5):
    return Post.objects.all().order_by('-created_time')[:num]

# 归档模板标签
@register.simple_tag
def archives():
    # dates返回一个列表，列表中的元素为每一篇文章的创建时间(精确到月份)，order='DESC' 表示降序
    return Post.objects.dates('created_time', 'month', order='DESC')

# 分类模板标签
@register.simple_tag
def get_categories():
    # return Category.objects.all()
    # 引入Count函数，计算分类下的文章数，其接受的参数为需要计数的模型名称
    return Category.objects.annotate(num_posts=Count('post')).filter(num_posts__gt=0)


# 标签云
@register.simple_tag
def get_tags():
    return Tag.objects.annotate(num_posts=Count('post')).filter(num_posts__gt=0)
