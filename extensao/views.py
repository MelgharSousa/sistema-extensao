from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm, PasswordResetForm
from .models import Participante, Oferta, Inscricao, Situacao, TipoOferta
from .forms import ParticipanteForm, EditarParticipanteForm
from django.contrib import messages
import re
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _


# view da página home
def home(request):
    ofertas = Oferta.objects.all()
    return render(request, 'extensao/home.html', {'ofertas': ofertas})


def categoria(request):
    p = {'1', '2'}
    tipo_oferta = request.GET.get('cat')
    if tipo_oferta in p:
        ofertas = Oferta.objects.filter(tipo_oferta=int(tipo_oferta))
    else:
        ofertas = Oferta.objects.all()

    context = {'ofertas': ofertas}
    return render(request, 'extensao/home.html', context)



# View Categoria de Cursos
def novos_cursos(request):
    situacao = Situacao.objects.get(id=1)
    ofertas = Oferta.objects.filter(situacao=situacao)
    return render(request, 'extensao/novos_cursos.html', {'ofertas': ofertas})


def inscricoes_abertas(request):
    situacao = Situacao.objects.get(id=2)
    ofertas = Oferta.objects.filter(situacao=situacao)
    return render(request, 'extensao/inscricoes_abertas.html',
    {'ofertas': ofertas})


def inscricoes_finalizadas(request):
    situacao = Situacao.objects.get(id=3)
    ofertas = Oferta.objects.filter(situacao=situacao)
    return render(request, 'extensao/inscricoes_finalizadas.html',
    {'ofertas': ofertas})


def concluidos(request):
    situacao = Situacao.objects.get(id=4)
    ofertas = Oferta.objects.filter(situacao=situacao)
    return render(request, 'extensao/concluidos.html', {'ofertas': ofertas})


#View Detalhes do Curso
def detalhes_oferta(request, id):
    oferta = Oferta.objects.get(id=id)
    context = {'oferta': oferta}
    return render(request, 'extensao/detalhes_oferta.html', context)


#View Cadastrar Usuário
def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Cadastro Realizado com Sucesso!'
            , extra_tags='login')
            return redirect('login')
    else:
        form = UserCreationForm()

    return render(request, 'registration/signup.html', {'form': form})


#View Alterar Senha
def alterar_senha(request):
    if request.method == 'POST':
        form = PasswordChangeForm(user=request.user)
        if form.is_valid():
            form.save()

            update_session_auth_hash(request, form.user)# atualiza a sessão
            messages.success(request, ('Sua senha foi alterada com sucesso!'))
            return redirect('home')

    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'extensao/alterar_senha.html', {
        'form': form
    })



#View em espera...
def recuperar_senha(request):
    if request.method == 'POST':
        form = PasswordResetForm(user=request.user)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            #messages.success(request, ('Sua senha foi alterada com sucesso!'))
            return redirect('home')

    else:
        form = PasswordResetForm(request.user)
    return render(request, 'extensao/recuperar_senha.html', {
        'form': form
    })


#View Participante (Formulário)
def participante(request):
    usuario = User.objects.get(username=request.user)

    if participante_check(id=usuario.id):
        #messages.warning(request, 'Você já possui cadastro!', extra_tags='cadastrado1')
        return redirect('home')
    else:
        form = ParticipanteForm
        data = {'form': form}
        messages.warning(request, 'Para se inscrever em um curso você deve está cadastrado no sistema!',
        extra_tags='cadastro20')
    return render(request, 'extensao/cadastro.html', data)


#View Participante Save (Grava os dados do formulário no BD)
def participante_save(request):
    form = ParticipanteForm(request.POST, request.FILES or None)
    usuario = User.objects.get(username=request.user)
    if form.is_valid():
        nome = form.cleaned_data['nome']
        cpf = form.cleaned_data['cpf']
        sexo = form.cleaned_data['sexo']
        nome_mae = form.cleaned_data['nome_mae']
        responsavel = form.cleaned_data['responsavel']
        data_nascimento = form.cleaned_data['data_nascimento']
        nacionalidade = form.cleaned_data['nacionalidade']
        estado_nascimento = form.cleaned_data['estado_nascimento']
        municipio_nascimento = form.cleaned_data['municipio_nascimento']
        identidade_candidato = form.cleaned_data['identidade_candidato']
        titulo = form.cleaned_data['titulo']
        reservista = form.cleaned_data['reservista']
        data_identidade = form.cleaned_data['data_identidade']
        orgao_emissor = form.cleaned_data['orgao_emissor']
        uf_identidade = form.cleaned_data['uf_identidade']
        municipio_identidade = form.cleaned_data['municipio_identidade']
        pais_origem = form.cleaned_data['pais_origem']
        logradouro = form.cleaned_data['logradouro']
        complemento = form.cleaned_data['complemento']
        bairro = form.cleaned_data['bairro']
        estado = form.cleaned_data['estado']
        cidade_endereco = form.cleaned_data['cidade_endereco']
        cep = form.cleaned_data['cep']
        email = form.cleaned_data['email']
        telefone_residencial = form.cleaned_data['telefone_residencial']
        telefone_celular = form.cleaned_data['telefone_celular']
        foto_perfil = form.cleaned_data['foto_perfil']


        participante = Participante(
        usuario=usuario, nome=nome, cpf=cpf, sexo=sexo, nome_mae=nome_mae,
        responsavel=responsavel, data_nascimento=data_nascimento,
        nacionalidade=nacionalidade, estado_nascimento=estado_nascimento,
        municipio_nascimento=municipio_nascimento, identidade_candidato=
        identidade_candidato, titulo=titulo, reservista=reservista, data_identidade=data_identidade,
        orgao_emissor=orgao_emissor, uf_identidade=uf_identidade, municipio_identidade=
        municipio_identidade, pais_origem=pais_origem, logradouro=logradouro,
        complemento=complemento, bairro=bairro, estado=estado, cidade_endereco=
        cidade_endereco, cep=cep, email=email, telefone_residencial=
        telefone_residencial, telefone_celular=telefone_celular, foto_perfil=foto_perfil
        )

        if participante_check(id=usuario.id):
            messages.warning(request, 'Você já possui cadastro!', extra_tags='cadastrado1')
            return redirect('home')
        else:
            participante_cpf = Participante.objects.filter(cpf=cpf)
           # participante_nome = Participante.objects.filter(nome=nome)
            #x = re.findall("[A-Z]")
            if not participante_cpf.exists():
                #and participante_nome == x:
                participante.save()
                messages.success(request, 'Pronto para realizar inscrição! Selecione um curso.',
                                 extra_tags='cadastrado')
                return redirect('home')
            else:
                messages.success(request, 'Existe outro Usuário com esse CPF!', extra_tags='cpf')
                #messages.success(request, 'Campo Inválido! Use apenas letras maiúsculas', extra_tags='nome')
            return render(request, 'extensao/cadastro.html', {'form': form})



#View Editar Participante (Atualiza os dados da tabela participante no BD)
def editar(request):
    usuario = User.objects.get(username=request.user)
    editado = Participante.objects.filter(usuario=usuario).first()

    form = EditarParticipanteForm(request.POST, request.FILES or None, instance=editado)
    if request.method == "POST" and "FILES":

       if form.is_valid():
            form.save()
            messages.warning(request, 'Alterado com sucesso! Voltar para a página inicial.',
            extra_tags='editado10')


    else:
        form = EditarParticipanteForm(instance=editado)
        form.fields["cpf"].widget.attrs['readonly'] = True
        form.fields["usuario"].widget.attrs['readonly'] = True
        form.fields["municipio_nascimento"].widget.attrs['readonly'] = True
        form.fields["foto_perfil"].widget.attrs['readonly'] = True

    return render(request, 'extensao/editar.html', {'form': form})



# View Detalhes do Participante
def participante_detalhes(request):
    usuario = User.objects.get(username=request.user)
    participante = Participante.objects.filter(usuario=usuario).first()
    context = {'participante': participante}
    if participante_check(id=usuario.id):
        messages.warning(request, 'Você precisa está logado no sistema!',
        extra_tags='editado01')
        return render(request, 'extensao/participante_detalhes.html', context)
    else:
        messages.warning(request, 'Você ainda não está cadastrado! Realize seu cadastro Aqui.', extra_tags='editado')
        return redirect('home')


# View Verifica Participante (Verifica se o Usuário autentificado no sistema possui Participante ou seja, está cadastrado)
def participante_check(id):
    usuario = User.objects.get(pk=id)
    participante = Participante.objects.filter(usuario=usuario).first()
    if participante != None:
        return True
    else:
        return False


# View Minhas Inscrições (Exibi as inscrições já realizadas pelo Participante)
def minhas_inscricoes(request):
    usuario = User.objects.get(username=request.user)
    if participante_check(id=usuario.id):
        participante = Participante.objects.get(usuario=usuario)
        inscricoes = Inscricao.objects.filter(participante=participante)

        context = {'inscricoes': inscricoes}

        if inscricoes.exists():
            return render(request, 'extensao/minhas_inscricoes.html', context)
        else:
            messages.warning(request, 'Você não está inscrito em nenhum curso! Selecione um curso.',
            extra_tags='inscricao3')
            return render(request, 'extensao/detalhes_oferta.html', context)
    else:
        messages.warning(request, 'Realize seu cadastro Aqui!', extra_tags='editado')
        return redirect('home')


# View Gerar Comprovante (Exibi o comprovante de cada inscrição realizada pelo Participante)
def gerar_comprovante(request, id):
    inscricao = Inscricao.objects.get(pk=id)
    context = {'inscricao': inscricao}
    messages.warning(request, 'Você precisa está logado no sistema!',
    extra_tags='comprovante01')
    return render(request, 'extensao/gerar_comprovante.html', context)


# View Comprovante de Inscrição (Exibi o Comprovante após a confirmação da Inscricão)
def comprovante_inscricao(request, id):
    inscricao = Inscricao.objects.get(pk=id)
    context = {'inscricao': inscricao}
    messages.warning(request, 'Você precisa está logado no sistema!',
    extra_tags='comprovante02')
    return render(request, 'extensao/comprovante_inscricao.html', context)


# View Inscrição (Grava os dados na tabela Inscrição)
def inscricao_save(request, id):
        usuario = User.objects.get(username=request.user)
        ofertas = Oferta.objects.get(pk=id)
        context = {'ofertas': ofertas}
        participante = Participante.objects.get(usuario=usuario)
        oferta = Oferta.objects.get(pk=id)
        inscricao = Inscricao(participante=participante, oferta=oferta)
        inscricao_check = Inscricao.objects.filter(participante_id=participante.id,
        oferta_id=oferta.id)
        if not inscricao_check.exists():
            inscricao.save()
            return redirect('gerar_comprovante', inscricao.id)
        else:
            messages.warning(request, 'Você já está inscrito nesse curso!',
            extra_tags='inscricao_save')
            return render(request, 'extensao/detalhes_oferta.html', context)


 # View Confirmar Inscrição (Relaciona os Objetos Participante e Curso na tabela Inscrição do BD)
def confirmar_inscricao(request, id):
    usuario = User.objects.get(username=request.user)
    if participante_check(id=usuario.id):
        ofertas = Oferta.objects.get(pk=id)
        participante = Participante.objects.get(usuario=usuario)
        oferta = Oferta.objects.get(pk=id)
        inscricao_check = Inscricao.objects.filter(participante_id=participante.id, oferta_id=oferta.id)
        context = {'ofertas': ofertas, 'participante': participante}
        if not inscricao_check.exists():
            return render(request, 'extensao/confirmar_inscricao.html', context)
        else:
            messages.warning(request, 'Você já está inscrito nesse curso!',
            extra_tags='inscricao1')

        return redirect('detalhes_oferta', id=id)
    else:
        messages.warning(request, ' Seu cadastro ainda não está completo! Clique aqui para concluir cadastro.',
        extra_tags='inscricao2')
    return redirect('detalhes_oferta', id=id)
