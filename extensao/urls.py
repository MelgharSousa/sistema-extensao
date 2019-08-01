from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', views.home, name='home'),
    path('novos_cursos', views.novos_cursos, name='novos_cursos'),
    path('inscricoes_abertas', views.inscricoes_abertas, name='inscricoes_abertas'),
    path('inscricoes_finalizadas', views.inscricoes_finalizadas, name='inscricoes_finalizadas'),
    path('concluidos', views.concluidos, name='concluidos'),
    path('detalhes_curso/<int:id>/', views.detalhes_curso,
         name='detalhes_curso'),
    path('signup/', views.signup, name='signup'),
    path('alterar_senha', views.alterar_senha, name='alterar_senha'),
    path('recuperar_senha', views.recuperar_senha, name='recuperar_senha'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('participante/', views.participante, name='participante'),
    path('participante_save/', views.participante_save,
         name='participante_save'),
    path('inscricao_save/<int:id>/', views.inscricao_save,
         name='inscricao_save'),
    path('confirmar_inscricao/<int:id>/', views.confirmar_inscricao,
         name='confirmar_inscricao'),
    path('comprovante_inscricao/<int:id>/', views.comprovante_inscricao,
         name='comprovante_inscricao'),
    path('editar/<int:id>/', views.editar, name='editar'),
    path('participante_detalhes/<int:id>/', views.participante_detalhes,
         name='participante_detalhes'),
    path('participante_check/<int:id>/', views.participante_check,
         name='participante_check'),
    path('minhas_inscricoes/<int:id>/', views.minhas_inscricoes,
         name='minhas_inscricoes'),
    path('gerar_comprovante/<int:id>/', views.gerar_comprovante,
         name='gerar_comprovante'),
]
