from rest_framework.viewsets import ModelViewSet

from models.veiculo import Veiculo
from serializers.veiculo import VeiculoSerializer


class VeiculoViewSet(ModelViewSet):
    queryset = Veiculo.objects.all()
    serializer_class = VeiculoSerializer
