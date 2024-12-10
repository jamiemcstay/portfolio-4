from .import views
from django.urls import path

urlpatterns = [
    path('', views.ReviewList.as_view(), name='home'),
    path('my-reviews/', views.my_reviews, name="my_reviews"),
    path('<slug:slug>/', views.review_detail, name='review_detail'),
]

