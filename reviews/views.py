from rest_framework import generics
from reviews.models import Review
from reviews.serializers import ReviewSerializer


class ReviewListCreateAPIView(generics.ListCreateAPIView):
    """
    Endpoint reponsavel por listar as avaliações disposniveis com GET e adicionar novas com POST.
    """
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer


class ReviewRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    """
    Endpoint reponsavel por passar as informações de uma avaliação especifica de acordo com seu ID. Pode fazer alterações nessa avaliação: use o PUT, PATCH para atualizar o endpont e DELETE para exclui-lo.
    """
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

