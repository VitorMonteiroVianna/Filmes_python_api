from rest_framework import generics
from genres.models import Genre
from genres.serializers import GenrerSerializer


class GenericCreateListView(generics.ListCreateAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenrerSerializer