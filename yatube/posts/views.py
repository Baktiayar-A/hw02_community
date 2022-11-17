from django.conf import settings
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404, render

from .models import Group, Post

User = get_user_model()


def index(request):
    template = 'posts/index.html'
    title = "Последние обновления на сайте"
    paginator = Paginator(Post.objects.all(), settings.NUM_OF_POSTS)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'title': title,
        'page_obj': page_obj,
    }
    return render(request, template, context)


def group_posts(request, slug):
    template = 'posts/group_list.html'
    title = f"Записи сообщества {slug}"
    group = get_object_or_404(Group, slug=slug)
    post_list = group.group.select_related('group').all()
    paginator = Paginator(post_list, settings.NUM_OF_POSTS)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'title': title,
        'group': group,
        'page_obj': page_obj,
    }
    return render(request, template, context)


@login_required
def profile(request, username):
    template = 'posts/profile.html'
    profile_name = get_object_or_404(User, username=username)
    title = f"Профайл пользователя {profile_name}"
    post_list = profile_name.posts.select_related('author').all()
    paginator = Paginator(post_list, settings.NUM_OF_POSTS)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'title': title,
        'profile_name': profile_name,
        'post_list': post_list,
        'page_obj': page_obj,
    }
    return render(request, template, context)


def post_detail(request, post_id):
    template = 'posts/post_detail.html'
    post = Post.objects.get(pk=post_id)
    posts_count = post.author.posts.count()
    title = f"Пост { post }"
    context = {
        'title': title,
        'post': post,
        'posts_count': posts_count,
    }
    return render(request, template, context)
