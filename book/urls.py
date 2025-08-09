from django.urls import path
from .views import ReviewListView, ReviewCreateView, ReviewUpdateView, ReviewActivationView

urlpatterns = [
    path('reviews/', ReviewListView.as_view(), name='review-list'),
    path('reviews/create/', ReviewCreateView.as_view(), name='review-create'),
    path('reviews/<int:pk>/update/', ReviewUpdateView.as_view(), name='review-update'),
    path('reviews/<int:pk>/toggle-active/', ReviewActivationView.as_view(), name='review-activate'),
    
]