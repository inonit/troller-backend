from django.urls import path
from . import views


urlpatterns = [
    ## messages
    path('messages/create', views.MessageCreateView.as_view()),
    path('messages/list', views.MessageListView.as_view()),
    ]
