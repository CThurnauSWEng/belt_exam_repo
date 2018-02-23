from django.conf.urls import url
from . import views           
urlpatterns = [
    url(r'^welcome', views.welcome),    
    url(r'^show_friend/(?P<friend_id>\d+)$', views.show_friend),    
    url(r'^remove_friend/(?P<friend_id>\d+)$', views.remove_friend),    
    url(r'^make_friends', views.make_friends)    
]
