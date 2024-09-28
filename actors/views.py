from rest_framework import generics
from actors.models import Actor
from actors.serializers import ActorSerializer


class ActorListCreateAPIView(generics.ListCreateAPIView):
    """
    Endpoint reponsavel por listar os atores disposniveis com GET e adicionar novos com POST.
    """
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer
    

class ActorRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    """
    Endpoint reponsavel por passar as informações de um ator especifico de acordo com seu ID. Pode fazer alterações nesse ator: use o PUT, PATCH para atualizar o endpont e DELETE para exclui-lo.
    """
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer