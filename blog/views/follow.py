from django.contrib.auth.models import User
from django.core.paginator import Paginator
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from blog.models.post import Post
from blog.models.followers import Follower
from django.http import HttpResponse

@csrf_exempt
def follow(request):
    
    if request.user.is_authenticated:
        follow_by = request.user
        try:
            to_follow = User.objects.get(username=request.POST['username'])
        except:
            return HttpResponse("Do Nothing!")
        if request.POST.get('click',None):
            try:

                obj, created = Follower.objects.get_or_create(follower=follow_by, following=to_follow)
            except ValueError as message:
                return HttpResponse(message)
            if created:
                return HttpResponse("Unfollow")

            obj.delete()
            return HttpResponse("Follow")
        try:
            Follower.objects.get(follower=follow_by, following=to_follow)
            return HttpResponse("Unfollow")
        except:
            return HttpResponse("Follow")

    else:
        print("Do Nothing")