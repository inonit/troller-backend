from django.urls import path, re_path
from . import views

urlpatterns = [
    ## profiles
    path('profiles/create', views.ProfileCreateView.as_view(), name="profiles_create"),
    path('profiles/list', views.ProfileListView.as_view(), name="profiles"),

    ## users
    path('users/create', views.UserCreateView.as_view(), name="users_create"),

    ## likes
    path('likes/create', views.LikeCreateView.as_view()),
    path('likes/list', views.LikeListView.as_view()),
    re_path('likes/(?P<pk>\d+)/update', views.LikeUpdateView.as_view()),
    re_path('likes/(?P<pk>\d+)/delete', views.LikeDeleteView.as_view()),

    ## messages
    path('messages/create', views.MessageCreateView.as_view()),
    path('messages/list', views.MessageListView.as_view()),
    re_path('messages/(?P<pk>\d+)/update', views.MessageUpdateView.as_view()),
    re_path('messages/(?P<pk>\d+)/delete', views.MessageDeleteView.as_view()),
    ]
