from django.shortcuts import render, HttpResponse, redirect
from ..user_app.models import User,Friend

def welcome(request):

    this_user = User.objects.get(id=request.session['user_id'])

    af1 = this_user.friend_sender.all().values('receiver')
    nfyet = User.objects.exclude(id__in=af1).exclude(id=request.session['user_id'])
    
    context = {
        'this_user'          : this_user,
        'this_users_friends' : Friend.objects.filter(sender=this_user),
        'nfyet'              : nfyet
    }
    return render(request, "friends_app/welcome.html", context)

def make_friends(request):
    
    # assume all input data is valid, because all the user does is hit the button

    response = Friend.objects.create(
        sender      = User.objects.get(id=request.session['user_id']),
        receiver    = User.objects.get(id=request.POST['new_friend_id'])
    )

    return redirect('/friends/welcome')

def show_friend(request, friend_id):
    context = {
        'friend' : User.objects.get(id=friend_id)
    }
    return render(request, "friends_app/show_friend.html",context)

def remove_friend(request, friend_id):
    this_user = User.objects.get(id=request.session['user_id'])
    this_friend = User.objects.get(id=friend_id)
    friend_object = Friend.objects.filter(sender=this_user,receiver=this_friend)
    friend_object.delete()
    
    return redirect('/friends/welcome')