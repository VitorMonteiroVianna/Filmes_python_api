from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from genres.models import Genre
from genres.serializers import GenrerSerializer
from genres.permitions import GenrePermissionClass


class GenreCreateListView(generics.ListCreateAPIView):
    """
    Endpoint reponsavel por listar os generos disposniveis com GET e adicionar novos com POST.
    """
    permission_classes = (IsAuthenticated, GenrePermissionClass)
    queryset = Genre.objects.all()
    serializer_class = GenrerSerializer


class GenreRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    """
    Endpoint reponsavel por passar as informações de um genero especifico de acordo com seu ID. Pode fazer alterações nesse genero: use o PUT, PATCH para atualizar o endpont e DELETE para exclui-lo.
    """
    permission_classes = (IsAuthenticated, GenrePermissionClass)
    queryset = Genre.objects.all()
    serializer_class = GenrerSerializer