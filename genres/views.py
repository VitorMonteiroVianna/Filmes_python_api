from rest_framework import generics
from genres.models import Genre
from genres.serializers import GenrerSerializer


class GenreCreateListView(generics.ListCreateAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenrerSerializer


class GenreRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenrerSerializer