from django.urls import path, include
from . import views


urlpatterns = [
    # ----View Home----
    path('', views.home, name='home'),


    # ---- Área dos Cursos -----

    # View Categoria de Cursos
    path('novos_cursos', views.novos_cursos, name='novos_cursos'),
    path('inscricoes_abertas', views.inscricoes_abertas,
         name='inscricoes_abertas'),
    path('inscricoes_finalizadas', views.inscricoes_finalizadas,
         name='inscricoes_finalizadas'),
    path('concluidos', views.concluidos, name='concluidos'),

    #View Detalhes do Curso
    path('detalhes_curso/<int:id>/', views.detalhes_curso,
         name='detalhes_curso'),


    #---- Área do Usuário ----

    #View Cadastrar Usuário
    path('signup/', views.signup, name='signup'),

    #View Alterar Senha
    path('alterar_senha', views.alterar_senha, name='alterar_senha'),

    #View em espera...
    path('recuperar_senha', views.recuperar_senha, name='recuperar_senha'),

    #View Auth do Django
    path('accounts/', include('django.contrib.auth.urls')),


    #---- Área do Participante ----

    #View Participante (Formulário)
    path('participante/', views.participante, name='participante'),

    #View Participante Save (Grava os dados no formulário no BD)
    path('participante_save/', views.participante_save,
         name='participante_save'),

   #View Editar Participante (Atualiza os dados da tabela participante no BD)
    path('editar/', views.editar, name='editar'),

    # View Detalhes do Participante
    path('participante_detalhes/', views.participante_detalhes,
         name='participante_detalhes'),

    # View Verifica Participante (Verifica se o Usuário autentificado no sistema possui Participante ou seja, está cadastro)
    path('participante_check/<int:id>/', views.participante_check,
         name='participante_check'),

    # View Minhas Inscrições (Exibi as inscrições já realizadas pelo Participante)
    path('minhas_inscricoes/', views.minhas_inscricoes,
         name='minhas_inscricoes'),

    # View Gerar Comprovante (Exibi o comprovante de cada inscrição realizada pelo Participante)
    path('gerar_comprovante/<int:id>/', views.gerar_comprovante,
         name='gerar_comprovante'),

    # View Comprovante de Inscrição (Exibi o Comprovante após a confirmação da Inscricão)
    path('comprovante_inscricao/<int:id>/', views.comprovante_inscricao,
         name='comprovante_inscricao'),

    # View Inscrição (Faz o relacionamento dos Objetos Participante e Curso na tabela Inscrição do BD)
    path('inscricao_save/<int:id>/', views.inscricao_save,
         name='inscricao_save'),

    # View Confirmar Inscrição (Grava os dados na tabela Inscrição)
    path('confirmar_inscricao/<int:id>/', views.confirmar_inscricao,
         name='confirmar_inscricao'),





]
