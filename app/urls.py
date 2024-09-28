from django.contrib import admin
from django.urls import path
from genres.views import GenreCreateListView, GenreRetrieveUpdateDestroyAPIView
from actors.views import ActorListCreateAPIView, ActorRetrieveUpdateDestroyAPIView

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('genre/', GenreCreateListView.as_view(), name='genre_create_list'),
    path('genre/<int:pk>/', GenreRetrieveUpdateDestroyAPIView.as_view(), name='genre_retrive_update_delete'),
    
    path('actor/', ActorListCreateAPIView.as_view(), name='actor_list_view'),
    path('actor/<int:pk>/', ActorRetrieveUpdateDestroyAPIView.as_view(), name='actor_retrive_update_delete')
]
