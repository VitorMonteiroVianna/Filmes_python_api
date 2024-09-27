from django.contrib import admin
from django.urls import path
from genres.views import GenericCreateListView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('genre/', GenericCreateListView.as_view(), name='create_list_view'),
]
