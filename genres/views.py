from rest_framework import generics
from genres.models import Genre
from genres.serializers import GenrerSerializer


class GenreCreateListView(generics.ListCreateAPIView):
    """
    Endpoint reponsavel por listar os generos disposniveis com GET e adicionar novos com POST.
    """
    queryset = Genre.objects.all()
    serializer_class = GenrerSerializer


class GenreRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    """
    Endpoint reponsavel por passar as informações de um genero especifico de acordo com seu ID. Pode fazer alterações nesse genero: use o PUT, PATCH para atualizar o endpont e DELETE para exclui-lo.
    """
    queryset = Genre.objects.all()
    serializer_class = GenrerSerializer