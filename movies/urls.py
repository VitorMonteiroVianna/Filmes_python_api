from django.urls import path
from . import views


urlpatterns =  [
    path('movie/', views.MovieListCreateAPIView.as_view(), name='movie_list_view'),
    path('movie/<int:pk>/', views.MovieRetrieveUpdateDestroyAPIView.as_view(), name='movie_retrive_update_delete'),
]