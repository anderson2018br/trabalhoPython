from django.contrib import admin

# Register your models here.

from core.models import Cliente, Sexo, EstadoCivil, ProdutoComprado, Produto
from django.urls import reverse
from django.utils.http import urlencode
from django.utils.html import format_html
@admin.register(Sexo)
class SexoAdmin(admin.ModelAdmin):
    list_display = ("descricao",)
    list_filter = ("descricao",)
    def get_model_perms(self, request):
        """
        Return empty perms dict thus hiding the model from admin index.
        """
        return {}
    pass

@admin.register(EstadoCivil)
class EstadoCivilAdmin(admin.ModelAdmin):
    list_display = ("descricao",)
    list_filter = ("descricao",)
    def get_model_perms(self, request):
        """
        Return empty perms dict thus hiding the model from admin index.
        """
        return {}
    pass

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ("nome", "ultimo_nome", 'cpf', "media_valor", "produtos_comprados")
    list_filter = ("nome", "ultimo_nome", 'cpf', 'datanascimento')
    search_fields = ("nome",'ultimo_nome')
    def media_valor(self, obj):
        from django.db.models import Avg
        result = ProdutoComprado.objects.filter(cliente=obj).aggregate(Avg("preco"))
        return "R$ 0,00" if result['preco__avg'] == None else "R$ "+str(result['preco__avg'])
    
    media_valor.short_description = "média do valor gasto"

    def produtos_comprados(self, obj):
        count = ProdutoComprado.objects.filter(cliente=obj).count()
        url = (
            reverse("admin:core_produtocomprado_changelist")
            + "?"
            + urlencode({"cliente__id": f"{obj.id}"})
        )
        return format_html('<a href="{}">{} Produto'+("" if count == 1  else "s")+'</a>', url, count)

    produtos_comprados.short_description = "Produtos comprados"
    pass


@admin.register(ProdutoComprado)
class ProdutoCompradoAdmin(admin.ModelAdmin):
    list_display = ("produto", "preco")
    list_filter = ("produto", "preco")

    pass


@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ("descricao", "preco")
    list_filter = ("descricao", "preco")
    pass