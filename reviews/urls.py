from django.urls import path
from . import views


urlpatterns = [
    path('review/', views.ReviewListCreateAPIView.as_view(), name='review_list_view'),
    path('review/<int:pk>/', views.ReviewRetrieveUpdateDestroyAPIView.as_view(), name='review_retrive_update_delete'),
]