from django.contrib import admin

from .models import (
    Participante,
    CursoExtensao,
    Inscricao,
    EquipeParticipante,
    Situacao,
    SituacaoInscricao,
    Arquivo
)

class CursoExtensaoAdmin(admin.ModelAdmin):
    list_display = ('nome_curso', 'id', 'situacao', 'criado', 'modificado',)
    list_filter = ('nome_curso', 'situacao',)
    search_fields = ('id', 'nome_curso')


class ParticipanteAdmin(admin.ModelAdmin):
    list_display = ('nome', 'id', 'cpf', 'email', 'criado', 'modificado',)
    list_filter = ('nome', 'cpf', 'email')
    search_fields = ('id', 'nome')


class InscricaoAdmin(admin.ModelAdmin):

    list_display = ('participante', 'id', 'curso_extensao', 'criado', 'modificado', 'situacao_inscricao')
    list_filter = ('curso_extensao', 'situacao_inscricao')
    search_fields = ('id', 'participante')

admin.site.register(EquipeParticipante)
admin.site.register(CursoExtensao, CursoExtensaoAdmin)
admin.site.register(Participante, ParticipanteAdmin)
admin.site.register(Situacao)
admin.site.register(SituacaoInscricao)
admin.site.register(Arquivo)
admin.site.register(Inscricao, InscricaoAdmin)


