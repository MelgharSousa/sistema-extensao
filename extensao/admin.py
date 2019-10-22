from django.contrib import admin

from .models import (
    Participante,
    Oferta,
    Inscricao,
    EquipeParticipante,
    Situacao,
    SituacaoInscricao,
    Arquivo,
    TipoOferta
)

class OfertaAdmin(admin.ModelAdmin):
    list_display = ('nome_oferta', 'id', 'situacao', 'criado', 'modificado',)
    list_filter = ('nome_oferta', 'situacao',)
    search_fields = ('id', 'nome_oferta')


class ParticipanteAdmin(admin.ModelAdmin):
    list_display = ('nome', 'id', 'cpf', 'email', 'criado', 'modificado',)
    list_filter = ('nome', 'cpf', 'email')
    search_fields = ('id', 'nome')


class InscricaoAdmin(admin.ModelAdmin):

    list_display = ('participante', 'id', 'oferta', 'criado', 'modificado', 'situacao_inscricao')
    list_filter = ('oferta', 'situacao_inscricao')
    search_fields = ('id', 'participante')

admin.site.register(EquipeParticipante)
admin.site.register(Oferta, OfertaAdmin)
admin.site.register(Participante, ParticipanteAdmin)
admin.site.register(Situacao)
admin.site.register(SituacaoInscricao)
admin.site.register(Arquivo)
admin.site.register(TipoOferta)
admin.site.register(Inscricao, InscricaoAdmin)


