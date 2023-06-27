from django.shortcuts import get_object_or_404, render
from blog.models import Post, Category
import datetime
now = datetime.datetime.now()


def index(request):
    template = 'blog/index.html'
    post_list = Post.objects.values('title').filter(
        category__is_published=True,
        is_published=True,
        pub_date__lte=now).order_by('-id')[:5]
    context = {'post_list': post_list}

    return render(request, template, context)


def post_detail(request, post_id):
    detail_post = Post.objects.get(post_id=post_id)
    post = get_object_or_404(Category, is_published=False, pub_date__gt=now, category__is_published=False)
    template = 'blog/detail.html'
    context = {'detail_post': detail_post, 'post': post}

    return render(request, template, context)


def category_posts(request, slug):
    template = 'blog/category.html'
    post = get_object_or_404(Category, is_published=False)
    post_category = Post.objects.all().filter(
        slug=slug,
        is_published=True,
        pub_date__lte=now)
    context = {
        'post_category': post_category,
        'posts': post
    }

    return render(request, template, context)
