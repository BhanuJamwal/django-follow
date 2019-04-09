from django.contrib.auth.models import User
from django.core.paginator import Paginator
from django.shortcuts import render
from django.http import HttpResponse
from blog.models.followers import Follower

from blog.models.post import Post

NUM_OF_POSTS = 5



def home(request, username=None):
    if request.user.is_authenticated:
        current_user = request.user
        first_name = ''
        last_name = ''

        if username:
            user = User.objects.get(username=username)
            # to_follow = User.objects.get(username=username)
            first_name = user.first_name
            last_name = user.last_name
            # post_list = Post.objects.filter(user=user)
            posts = []
            return render(request, 'blog/home.html', {'posts': posts,
                                              'username':username,
                                              'first_name': first_name,
                                              'last_name': last_name})
        else:
            ul = Follower.objects.filter(follower=current_user).values_list('following', flat=True)
            post_list = Post.objects.filter(user__in=ul)
            post_list = post_list.order_by('-pub_date')

            paginator = Paginator(post_list, NUM_OF_POSTS)  # Show NUM_OF_PAGES posts per page
            page = request.GET.get('page')

            posts = paginator.get_page(page)

            return render(request, 'blog/home.html', {'posts': posts,
                                                    'username':username,
                                                    'first_name': first_name,
                                                    'last_name': last_name})
    else:
        return render(request, 'blog/home.html', {'message': 'No blog found please login and follower users to see all their post'})

def blogs(request):

    post_list = Post.objects.all()
    post_list = post_list.order_by('-pub_date')

    paginator = Paginator(post_list, NUM_OF_POSTS)  # Show NUM_OF_PAGES posts per page
    page = request.GET.get('page')

    posts = paginator.get_page(page)

    return render(request, 'blog/home.html', {'posts': posts})
