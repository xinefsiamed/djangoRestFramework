from rest_framework import generics
from rest_framework.generics import get_object_or_404

from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import mixins
from rest_framework import permissions
from .permissions import EhSuperUser

from .models import Curso, Avaliacao
from .serializers import CursoSerializer, AvaliacaoSerializer


"""
API v1
"""


class CursosAPIView(generics.ListCreateAPIView):
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer


class CursoAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer


class AvaliacoesAPIView(generics.ListCreateAPIView):
    queryset = Avaliacao.objects.all()
    serializer_class = AvaliacaoSerializer

    def get_queryset(self):
        if self.kwargs.get('curso_pk'):
            return self.queryset.filter(curso=self.kwargs.get('curso_pk'))
        return self.queryset.all()


class AvaliacaoAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Avaliacao.objects.all()
    serializer_class = AvaliacaoSerializer

    def get_object(self):
        if self.kwargs.get('avaliacao_pk'):
            return get_object_or_404(self.get_queryset(),
                                     curso_id=self.kwargs.get('curso_pk'),
                                     pk=self.kwargs.get('avaliacao_pk'))

        return get_object_or_404(self.get_queryset(), pk=self.kwargs.get('avaliacao_pk'))


"""
API v2
"""


class CursoViewSet(viewsets.ModelViewSet):
    permission_classes = (
        EhSuperUser,
        permissions.DjangoModelPermissions, )
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer

    @action(detail=True, methods=['GET'])
    def avaliacoes(self, request, pk=None):
        curso = self.get_object()
        serializer = AvaliacaoSerializer(curso.avaliacoes.all(), many=True)
        return Response(serializer.data)


""" class AvaliacaoViewSet(viewsets.ModelViewSet):
    queryset = Avaliacao.objects.all()
    serializer_class = AvaliacaoSerializer """


class AvaliacaoViewSet(mixins.ListModelMixin,
                       mixins.CreateModelMixin,
                       mixins.RetrieveModelMixin,
                       mixins.UpdateModelMixin,
                       mixins.DestroyModelMixin,
                       viewsets.GenericViewSet):

    queryset = Avaliacao.objects.all()
    serializer_class = AvaliacaoSerializer
