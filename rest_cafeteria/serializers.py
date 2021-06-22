from rest_framework import serializers

from cafeteria.models import Alimento


class AlimentosSerializer(serializers.ModelSerializer):

    class Meta:

        model = Alimento

        fields = ['idAlimento', 'nombre', 'descripcion', 'precio','categoria','tipoAlimento']