from rest_framework import serializers
from .models import Curso, Avaliacao


class AvaliacaoSerializer(serializers.ModelSerializer):
    class Meta:
        extra_kwargs = {
            'email': {'write_only': True}
        }
        model = Avaliacao
        fields = ('id', 'email', 'curso', 'nome', 'email',
                  'comentario', 'avaliacao', 'criacao', 'ativo')


class CursoSerializer(serializers.ModelSerializer):
    # Nested Relationship
    #avaliacoes = AvaliacaoSerializer(many=True, read_only=True)

    # HyperLinked Related field
    """ avaliacoes = serializers.HyperlinkedRelatedField(
        many=True, read_only=True, view_name='avaliacao-detail') """

    # PrimaryKey related field
    avaliacoes = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Curso
        fields = ('id', 'titulo', 'url', 'criacao', 'ativo', 'avaliacoes')
