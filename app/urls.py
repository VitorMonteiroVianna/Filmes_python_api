from django.contrib import admin
from django.urls import path
from genres.views import GenreCreateListView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('genre/', GenreCreateListView.as_view(), name='create_list_view'),
]
