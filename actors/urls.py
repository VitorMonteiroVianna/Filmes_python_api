from django.urls import path
from . import views


urlpatterns = [
    path('actor/', views.ActorListCreateAPIView.as_view(), name='actor_list_view'),
    path('actor/<int:pk>/', views.ActorRetrieveUpdateDestroyAPIView.as_view(), name='actor_retrive_update_delete'),
]