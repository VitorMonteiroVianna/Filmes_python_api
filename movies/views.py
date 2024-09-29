from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from movies.models import Movie
from movies.serializers import MovieSerializer


class MovieListCreateAPIView(generics.ListCreateAPIView):
    """
    Endpoint reponsavel por listar os filmes disposniveis com GET e adicionar novos com POST.
    """
    permission_classes = (IsAuthenticated,)
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer


class MovieRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    """
    Endpoint reponsavel por passar as informações de um filmes especifico de acordo com seu ID. Pode fazer alterações nesse filmes: use o PUT, PATCH para atualizar o endpont e DELETE para exclui-lo.
    """
    permission_classes = (IsAuthenticated,)
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

