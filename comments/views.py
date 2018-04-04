# -*- conding:utf-8 -*-
from django.shortcuts import render, get_object_or_404, redirect
from blog.models import Post
from .models import Comment
from .forms import CommentForm

def post_comment(request, post_pk):
    # 根据传入的文章ID post_pk 获取被评论的文章
    post = get_object_or_404(Post, pk=post_pk)
    if request.method == 'POST': # 当用户以POST请求提交表单时
        form = CommentForm(request.POST) # 用户提交的数据存在 request.POST， 这是一个类字典对象，我们利用这些数据构造了CommentForm的实例
        if form.is_valid(): # 当调用 is_valid() 时，Django自动帮我们检查表单的数据是否符合格式要求
            # save方法保存数据到数据库，但commit=False的作用时仅仅利用表单的数据生成 Comment 模型的实例，但还不保存评论数据到数据库
            comment = form.save(commit=False)
            comment.post = post # 将评论和被评论的文章关联起来
            comment.save() # 最终保存数据进数据库
            # 重定向到 post 的详情页，实际上当 redirect 函数接收一个模型的实例时，它会调用这个模型实例的 get_absolute_url 方法，该方法返回一个文章详情URL
            return redirect(post)
        else:
            # 检查到数据不合法，重新渲染详情页面，并且渲染表单的错误
            comment_list = post.comment_set.all() # 获取该文章下的所有评论，因为Post 和 Comment 是 ForeignKey 关联的，因此使用 Post.comment_set.all()反向查询全部评论
            context = {'post':post,
                       'form':form,
                       'comment_list':comment_list
                       }
            return render(request, 'blog/detail.html', context=context)
    # 不是post 请求，说明用户没有提交数据，重定向到文章详情页
    return redirect(post)
