from django.db import models

from models.cor import Cor
from models.modelo import Modelo
from uploader.models import Image


class Veiculo(models.Model):
    id = models.BigAutoField(primary_key=True)
    cor = models.ForeignKey(Cor, on_delete=models.PROTECT, related_name="veiculos")
    modelo = models.ForeignKey(
        Modelo, on_delete=models.PROTECT, related_name="veiculos"
    )
    ano = models.IntegerField(null=True, blank=True)
    descricao = models.CharField(max_length=255, null=True, blank=True)
    preco = models.DecimalField(decimal_places=2, max_digits=5, null=True, blank=True)
    imagem = models.ForeignKey(
        Image,
        related_name="+",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        default=None,
    )

    def __str__(self):
        return f"{self.ano} ({self.descricao})"

    class Meta:
        verbose_name = "Veiculo"
        verbose_name_plural = "Veiculos"
