from django.urls import path
from . import views


urlpatterns = [
    path('posts/', views.AlbumReviewList.as_view()),
    path('post/<int:pk>/', views.AlbumReviewDetail.as_view()),
]
