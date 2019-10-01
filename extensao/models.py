from django.db import models
from django.contrib.auth.models import User


sexo_opções = (
    ('M', 'Masculino'),
    ('F', 'Feminino'),
    ('Outros', 'Outros')
)

orgao_emissor_opções =(
	('SSP',' Secretaria de Segurança Pública'),
	('Cartório Civil','Cartório Civil '),
	('Polícia Federal ','Polícia Federal '),
	('Detran','Detran'),
	('Outros','Outros')
)

uf_opções = (
	('AC','Acre'),
	('AL','Alagoas'),
	('AP','Amapá'),
	('AM','Amazonas'),
	('BA','Bahia'),
	('CE','Ceará'),
	('DF','Distrito Federal'),
	('ES','Espírito Santo'),
	('GO','Goiás'),
	('MA','Maranhão'),
	('MT','Mato Grosso'),
	('MS','Mato Grosso do Sul'),
	('MG','Minas Gerais'),
	('PA','Pará'),
	('PB','Paraíba'),
	('PR','Paraná'),
	('PE','Pernambuco'),
	('PI','Piauí'),
	('RJ','Rio de Janeiro'),
	('RN','Rio Grande do Norte'),
	('RS','Rio Grande do Sul'),
	('RO','Rondônia'),
	('RR','Roraima'),
	('SC','Santa Cantaria'),
	('SP','São Paulo'),
	('SE','Sergipe'),
	('TO','Tocantins'),
)


class Situacao(models.Model):
	situacao = models.CharField('Situação', max_length=50)

	class Meta:
		verbose_name = 'Situação'
		verbose_name_plural = 'Situação'

	def __str__(self):
		return self.situacao


class EquipeParticipante(models.Model):
	nome_participante = models.CharField('Nome', max_length=100)
	matricula = models.CharField('Matrícula', max_length=20)
	telefone = models.CharField('Telefone', max_length=15)
	bolsista = models.CharField('Bolsista', max_length=200)
	titulacao = models.CharField('Titulação', max_length=200)

	class Meta:
		verbose_name = 'Equipe'
		verbose_name_plural = 'Equipe'

	def __str__(self):
		return self.nome_participante


class Participante(models.Model):
	usuario = models.OneToOneField(User, related_name='usuario', on_delete=models.PROTECT)
	nome = models.CharField('Nome Completo', max_length=100)
	cpf = models.CharField('CPF', max_length=11)
	sexo = models.CharField('Sexo', choices=sexo_opções, max_length=9)
	nome_mae = models.CharField('Filiação - Nome da Mãe', max_length=100)
	responsavel = models.CharField('Filiação - Outro Responsável',
								   max_length=100)
	data_nascimento = models.DateField('Data de Nascimento', )
	nacionalidade = models.CharField('Nacionalidade', max_length=100)
	estado_nascimento = models.CharField('Estado Nascimento',
										 choices=uf_opções, max_length=100)
	municipio_nascimento = models.CharField('Minicípio de Nascimento',
											max_length=100)
	identidade_candidato = models.CharField('Identidade do candidato',
											max_length=100)
	titulo = models.CharField('Título de Eleitor', max_length=12)
	reservista = models.CharField('Carteira de Reservista', max_length=12)
	data_identidade = models.DateField('Data de Emissão Identidade')
	orgao_emissor = models.CharField('Órgão Emissor',
									 choices=orgao_emissor_opções, max_length=100)
	uf_identidade = models.CharField('UF da Identidade',
									 choices=uf_opções, max_length=100)
	municipio_identidade = models.CharField('Município da Identidade',
											max_length=100)
	pais_origem = models.CharField('País de Origem', max_length=100, blank=True)
	logradouro = models.CharField('Logradouro', max_length=100)
	complemento = models.CharField('Complemento', max_length=100, blank=True)
	bairro = models.CharField('Bairro', max_length=100)
	estado = models.CharField('Estado', max_length=100)
	cidade_endereco = models.CharField('Cidade deste endereço', max_length=100)
	cep = models.CharField('CEP', max_length=9)
	email = models.EmailField('E-Mail', max_length=100)
	telefone_residencial = models.CharField('Telefone Residencial', max_length=15, blank=True)
	telefone_celular = models.CharField('Telefone Celular', max_length=15)
	foto_perfil =models.ImageField(upload_to='media', blank=True)
	criado = models.DateTimeField(auto_now_add=True)
	modificado = models.DateTimeField(auto_now=True)


	def __str__(self):
		return self.nome


class CursoExtensao(models.Model):
	nome_curso = models.CharField('Nome do Curso', max_length=100)
	resumo_curso = models.TextField('Resumo do Curso')
	area_tematica = models.CharField('Área Temática', max_length=100)
	data_inicio = models.DateField('Período de Execução Inicial')
	data_final = models.DateField('Período de Execução Final')
	data_inscricoes_inicial = models.DateField('Período Inicial das Inscrições')
	data_inscricoes_final = models.DateField('Período Final das Inscrições')
	area_conhecimento = models.CharField('Área de Conhecimento',max_length=100)
	tema = models.CharField('Tema', max_length=100)
	possui_cunho_social = models.CharField('Possui Cunho Social',max_length=100)
	vagas_participantes = models.CharField('Vagas Participantes', max_length=5)
	publico_alvo = models.CharField('Público Alvo', max_length=100)
	carga_horaria = models.CharField('Carga Horária', max_length=10)
	turno = models.CharField('Turno', max_length=20)
	periodo_letivo = models.CharField('Ano Letivo', max_length=100)
	equipe_participante = models.ManyToManyField(EquipeParticipante)
	situacao = models.ForeignKey(Situacao,on_delete=models.PROTECT, default=1)
	foto_curso = models.ImageField(default='default.png', blank=True, upload_to='media')
	criado = models.DateTimeField(auto_now_add=True)
	modificado = models.DateTimeField(auto_now=True)

	class Meta:
		verbose_name_plural = 'Cursos'

	def __str__(self):
		return self.nome_curso


class Arquivo(models.Model):
	arquivo = models.FileField(upload_to='media', blank=True)
	nome_arquivo = models.CharField("Nome do Arquivo", max_length=100)
	descricao = models.TextField('Descrição do Arquivo')
	curso = models.ForeignKey(CursoExtensao, related_name='arquivo', on_delete=models.PROTECT)
	criado = models.DateTimeField(auto_now_add=True)
	modificado = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.nome_arquivo


class SituacaoInscricao(models.Model):
	situacao_inscricao = models.CharField('Situação da Inscrição', max_length=50)

	class Meta:
		verbose_name = 'Situação da Inscrição'
		verbose_name_plural = 'Situação da Inscrição'

	def __str__(self):
		return self.situacao_inscricao

class Inscricao(models.Model):
	curso_extensao = models.ForeignKey(CursoExtensao, on_delete=models.PROTECT)
	participante = models.ForeignKey(Participante, on_delete=models.PROTECT)
	criado = models.DateTimeField(auto_now_add=True)
	modificado = models.DateTimeField(auto_now=True)
	situacao_inscricao = models.ForeignKey(SituacaoInscricao, on_delete=models.PROTECT, default=1)


	class Meta:
		verbose_name_plural = 'Inscrições'

	def __str__(self):
		 return str(self.participante)
