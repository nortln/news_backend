from django.urls import path

from . import views

urlpatterns = [
    path('', views.news_list),
    path('news/', views.news_list, name='news-list'),
    path('news/<int:pk>/', views.news_detail, name='news-detail'),
    path('news/tag/<str:tag>/', views.news_by_tag, name='news-by-tag'),
    path('news/statistics/', views.news_statistics, name='news-statistics'),
    path('news/<int:pk>/like/', views.like_news, name='like-news'),
]
