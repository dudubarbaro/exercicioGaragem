from rest_framework.serializers import ModelSerializer

from models.veiculo import Veiculo


class VeiculoSerializer(ModelSerializer):
    class Meta:
        model = Veiculo
        fields = "__all__"
