from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm, PasswordResetForm
from .models import Participante, CursoExtensao, Inscricao, Situacao
from .forms import ParticipanteForm, EditarParticipanteForm
from django.contrib import messages


# view da página home
def home(request):
    cursos = CursoExtensao.objects.all()
    return render(request, 'extensao/home.html',{'cursos': cursos})


def novos_cursos(request):
    situacao = Situacao.objects.get(id=1)
    cursos = CursoExtensao.objects.filter(situacao=situacao)
    return render(request, 'extensao/novos_cursos.html', {'cursos': cursos})


def inscricoes_abertas(request):
    situacao = Situacao.objects.get(id=2)
    cursos = CursoExtensao.objects.filter(situacao=situacao)
    return render(request, 'extensao/inscricoes_abertas.html', {'cursos': cursos})


def inscricoes_finalizadas(request):
    situacao = Situacao.objects.get(id=3)
    cursos = CursoExtensao.objects.filter(situacao=situacao)
    return render(request, 'extensao/inscricoes_finalizadas.html', {'cursos': cursos})

def concluidos(request):
    situacao = Situacao.objects.get(id=4)
    cursos = CursoExtensao.objects.filter(situacao=situacao)
    return render(request, 'extensao/concluidos.html', {'cursos': cursos})


def detalhes_curso(request, id):
    curso = CursoExtensao.objects.get(pk=id)
    context = {'curso': curso}
    return render(request, 'extensao/detalhes_curso.html', context)


#view da página inscrever-se
def signup(resquest):
    if resquest.method == 'POST':
        form = UserCreationForm(resquest.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()

    return render(resquest, 'registration/signup.html', {'form': form})


#view da página alterar senha
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

def participante(request):
    participante = Participante.objects.all()
    form = ParticipanteForm
    data = {'form': form}
    messages.warning(request, 'Para se inscrever em um curso você deve está cadastrado no sistema! ', extra_tags='cadastro20')
    return render(request, 'extensao/cadastro.html', data)


def editar(request, id):
    usuario = User.objects.get(pk=id)
    editado = Participante.objects.filter(usuario=usuario).first()

    form = EditarParticipanteForm(request.POST or None, instance=editado)
    if request.method == "POST":

       if form.is_valid():
            form.save()
            messages.warning(request, 'Alterado com sucesso! Voltar para a página inicial', extra_tags='editado10')


    else:
        form = EditarParticipanteForm(instance=editado)
        form.fields["cpf"].widget.attrs['readonly'] = True
        form.fields["usuario"].widget.attrs['readonly'] = True
        form.fields["municipio_nascimento"].widget.attrs['readonly'] = True


    return render(request, 'extensao/editar.html', {'form':form})



def participante_check(id):
    usuario = User.objects.get(pk=id)
    participante = Participante.objects.filter(usuario=usuario).first()
    if participante != None:
        return True
    else:
        return False


def participante_detalhes(request, id):
    usuario = User.objects.get(pk=id)
    participante = Participante.objects.filter(usuario=usuario).first()
    context = {'participante': participante}
    if participante_check(id=usuario.id):
        messages.warning(request, 'Você precisa está logado no sistema!', extra_tags='editado01')
        return render(request, 'extensao/participante_detalhes.html', context)
    else:
        messages.warning(request, 'Realize seu cadastro Aqui!', extra_tags='editado')
        return redirect('home')



def participante_save(request):
    form = ParticipanteForm(request.POST or None)
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
        zona = form.cleaned_data['zona']
        email = form.cleaned_data['email']
        telefone_residencial = form.cleaned_data['telefone_residencial']
        telefone_celular = form.cleaned_data['telefone_celular']


        participante = Participante(
        usuario=usuario, nome=nome, cpf=cpf, sexo=sexo, nome_mae=nome_mae,
        responsavel=responsavel, data_nascimento=data_nascimento,
        nacionalidade=nacionalidade, estado_nascimento=estado_nascimento,
        municipio_nascimento=municipio_nascimento, identidade_candidato=
        identidade_candidato, data_identidade=data_identidade, orgao_emissor=
        orgao_emissor, uf_identidade=uf_identidade, municipio_identidade=
        municipio_identidade, pais_origem=pais_origem, logradouro=logradouro,
        complemento=complemento, bairro=bairro, estado=estado, cidade_endereco=
        cidade_endereco, cep=cep, zona=zona, email=email, telefone_residencial=
        telefone_residencial, telefone_celular=telefone_celular
        )

        if participante_check(id=usuario.id):
            messages.warning(request, 'Você já possui cadastro!', extra_tags='cadastrado1')
            return redirect('home')
        else:
            participante.save()
            messages.success(request, 'Pronto para realizar inscrição! Selecione um curso!', extra_tags='cadastrado')
        return redirect('home')



def confirmar_inscricao(request, id):
    usuario = User.objects.get(username=request.user)
    if participante_check(id=usuario.id):
        curso = CursoExtensao.objects.get(pk=id)
        participante = Participante.objects.get(usuario=usuario)
        curso_extensao = CursoExtensao.objects.get(pk=id)
        inscricao = Inscricao(participante=participante, curso_extensao=curso_extensao)
        inscricao_check = Inscricao.objects.filter(participante_id=participante.id, curso_extensao_id=curso_extensao.id)
        context = {'curso': curso, 'participante': participante}
        if not inscricao_check.exists():
            return render(request, 'extensao/confirmar_inscricao.html', context)
        else:
            messages.warning(request, 'Você já está inscrito nesse curso!', extra_tags='inscricao1')
    else:
        messages.warning(request, ' Seu cadastro ainda não está completo! Clique aqui para concluir cadastro.', extra_tags='inscricao2')
    return redirect('detalhes_curso', id=id)


def inscricao_save(request, id):
        usuario = User.objects.get(username=request.user)
        curso = CursoExtensao.objects.get(pk=id)
        context = {'curso': curso}
        participante = Participante.objects.get(usuario=usuario)
        curso_extensao = CursoExtensao.objects.get(pk=id)
        inscricao = Inscricao(participante=participante, curso_extensao=curso_extensao)
        inscricao_check = Inscricao.objects.filter(participante_id=participante.id, curso_extensao_id=curso_extensao.id)
        if not inscricao_check.exists():
            inscricao.save()
            return redirect('gerar_comprovante', inscricao.id)
        else:
            messages.warning(request, 'Você já está inscrito nesse curso!', extra_tags='inscricao_save')
            return render(request, 'extensao/detalhes_curso.html', context)


def gerar_comprovante(request, id):
    inscricao = Inscricao.objects.get(pk=id)
    context = {'inscricao': inscricao}
    messages.warning(request, 'Você precisa está logado no sistema!', extra_tags='comprovante01')
    return render(request, 'extensao/gerar_comprovante.html', context)


def comprovante_inscricao(request, id):
    inscricao = Inscricao.objects.get(pk=id)
    context = {'inscricao': inscricao}
    messages.warning(request, 'Você precisa está logado no sistema!', extra_tags='comprovante02')
    return render(request, 'extensao/comprovante_inscricao.html', context)


def minhas_inscricoes(request, id):
    usuario = User.objects.get(pk=id)
    participante = Participante.objects.get(usuario=usuario)

    inscricoes = Inscricao.objects.filter(participante=participante)

    context = {'inscricoes': inscricoes}
    if inscricoes.exists():
        return render(request, 'extensao/minhas_inscricoes.html', context)
    else:
        messages.warning(request, 'Você não está inscrito em nenhum curso! Selecione um curso!', extra_tags='inscricao3')
    return render(request, 'extensao/detalhes_curso.html', context)