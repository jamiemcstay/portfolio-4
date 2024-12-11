from .import views
from django.urls import path

urlpatterns = [
    path('', views.ReviewList.as_view(), name='home'),
    path('my-reviews/', views.my_reviews, name='my_reviews'),
    path('add-review/', views.add_review, name='add_review'),
    path('<slug:slug>/', views.review_detail, name='review_detail'),
    path('review/edit/<slug:slug>', views.review_edit, name='review_edit'),
    path('<slug:slug>/delete/', views.review_delete, name='review_delete')
]



