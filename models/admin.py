from django.contrib import admin

from models.modelo import Modelo
from models.veiculo import Veiculo
from models.categoria import Categoria
from models.cor import Cor
from models.acessorio import Acessorio
from models.marca import Marca

admin.site.register(Veiculo)
admin.site.register(Modelo)
admin.site.register(Categoria)
admin.site.register(Cor)
admin.site.register(Acessorio)
admin.site.register(Marca)
