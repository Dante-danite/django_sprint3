from django.shortcuts import get_object_or_404, render
from blog.models import Post, Category
import datetime
now = datetime.datetime.now()


def index(request):
    template = 'blog/index.html'
    post_list = Post.objects.filter(
        category__is_published=True,
        is_published=True,
        pub_date__lt=now).order_by('-id')[:5]
    context = {'post_list': post_list}

    return render(request, template, context)


def post_detail(request, post_id):
    post = get_object_or_404(
        Post, id=post_id,
        is_published=True,
        pub_date__lt=now,
        category__is_published=True
    )
    template = 'blog/detail.html'
    context = {'post': post}

    return render(request, template, context)


def category_posts(request, slug):
    template = 'blog/category.html'
    category = get_object_or_404(
        Category,
        slug=slug,
        is_published=True
    )
    post_list = Post.objects.filter(
        pub_date__lt=now,
        is_published=True,
        category=category
    )
    context = {
        'category': category,
        'post_list': post_list
    }

    return render(request, template, context)
