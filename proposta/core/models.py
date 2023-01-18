# -*- Mode: Python; coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.contrib import admin
from django.utils.html import format_html
from django.db.models import Sum,Avg
from localflavor.br.br_states import STATE_CHOICES
from django.utils.safestring import mark_safe
from django.contrib.admin.views.main import ChangeList
    
class Cliente(models.Model):
	nome = models.CharField(u'Nome', max_length=100, unique=True)
	cpf = models.CharField(u'CPF', blank=True, max_length=14, unique=True)
	cnpj = models.CharField(u'CNPJ', blank=True, max_length=18, unique=True)
	telefone = models.CharField(u'telefone', blank=True, max_length=18, unique=True)
	email = models.EmailField(u'email', blank=True, max_length=200)
	endereco = models.CharField(u'Endereço', blank=True, max_length=200)
	bairro = models.CharField(u'Bairro', blank=True, max_length=100)
	cidade = models.CharField(u'Cidade', blank=True, max_length=100)
	estado = models.CharField(u'Estado',max_length=2, null=True, blank=True, choices=STATE_CHOICES)

	def __str__(self):
		return self.nome

class Motor(models.Model):

	MODELO_CHOICES = [   
     #carenado
    ('Carenado', (
		('Slim 40 kVA Carenado/Silenciado',	'Slim 40 kVA Carenado/Silenciado'),
		('Slim 55 kVA Carenado/Silenciado',	'Slim 55 kVA Carenado/Silenciado'),
		('Slim 60 kVA Carenado/Silenciado',	'Slim 60 kVA Carenado/Silenciado'),
		('Slim 63 kVA Carenado/Silenciado',	'Slim 63kVA Carenado/Silenciado'),
		('Slim 75 kVA Carenado/Silenciado',	'Slim 75kVA Carenado/Silenciado'),
		('Slim 95 kVA Carenado/Silenciado',	'Slim 95 kVA Carenado/Silenciado'),
		('Slim 83 kVA Carenado/Silenciado',	'Slim 83 kVA Carenado/Silenciado'),
		('Slim 100 kVA  Carenado/Silenciado',	'Slim 100 kVA Carenado/Silenciado'),
		('Slim 110 kVA Carenado/Silenciado',	'Slim 110 kVA Carenado/Silenciado'),
		('Slim 123 kVA Carenado/Silenciado',	'Slim 123 kVA Carenado/Silenciado'),
		('Slim 125 kVA  Carenado/Silenciado',	'Slim 125 kVA Carenado/Silenciado'),
		('Slim 140 kVA Carenado/Silenciado',	'Slim 140 kVA Carenado/Silenciado'),
			
		('Slim 207 kVA Carenado/Silenciado',	'Slim 207 kVA Carenado/Silenciado'),
			
		('Slim 251 kVA Carenado/Silenciado',	'Slim 251 kVA Carenado/Silenciado'),
		('Slim 300 kVA Carenado/Silenciado',	'Slim 300 kVA Carenado/Silenciado'),
		('Slim 300 KVA  Carenado/Silenciado',	'Slim 300 KVA  Carenado/Silenciado'),
		('Slim 330 KVA  Carenado/Silenciado',	'Slim 330 KVA  Carenado/Silenciado'),
		('Slim 360 KVA  Carenado/Silenciado',	'Slim 360 KVA  Carenado/Silenciado'),
		('Slim 400 KVA  Carenado/Silenciado',	'Slim 400 KVA  Carenado/Silenciado'),
		('Slim 369 kVA Carenado/Silenciado',	'Slim 369 kVA Carenado/Silenciado'),
		('Slim 285 kVA Carenado/Silenciado',	'Slim 285 kVA Carenado/Silenciado'),
		('Slim 334 kVA Carenado/Silenciado',	'Slim 334 kVA Carenado/Silenciado'),
		('Slim 350 kVA Carenado/Silenciado',	'Slim 350 kVA Carenado/Silenciado'),

		('Slim 438 kVA Carenado/Silenciado',	'Slim 438 kVA Carenado/Silenciado'),
		('Slim 450 kVA Carenado/Silenciado',	'Slim 450 kVA Carenado/Silenciado'),
		('Slim 451 kVA Carenado/Silenciado',	'Slim 451 kVA Carenado/Silenciado'),
		('Slim 500 kVA Carenado/Silenciado',	'Slim 500 kVA Carenado/Silenciado'),
		('Slim 501 kVA Carenado/Silenciado',	'Slim 501 kVA Carenado/Silenciado'),
		('Slim 550 kVA Carenado/Silenciado',	'Slim 550 kVA Carenado/Silenciado'),
		('Slim 625 kVA Carenado/Silenciado',	'Slim 625 kVA Carenado/Silenciado'),
		('Slim 650 kVA Carenado/Silenciado',	'Slim 650 kVA Carenado/Silenciado'),

		('Slim 550 kVA Carenado/Silenciado',	'Slim 550 kVA Carenado/Silenciado'),
		('Slim 625 kVA Carenado/Silenciado',	'Slim 625 kVA Carenado/Silenciado'),
			
		('Slim 563 kVA Carenado/Silenciado',	'Slim 563 kVA Carenado/Silenciado'),
		('Slim 642 kVA Carenado/Silenciado',	'Slim 642 kVA Carenado/Silenciado'),
		('Slim 700 kVA Carenado/Silenciado',	'Slim 700 kVA Carenado/Silenciado'),

		('Slim 720 kVA Carenado/Silenciado',	'Slim 720 kVA Carenado/Silenciado'),
		('Slim 752 kVA Carenado/Silenciado',	'Slim 752 kVA Carenado/Silenciado'),
		('Slim 770 kVA Carenado/Silenciado',	'Slim 770 kVA Carenado/Silenciado'),
		('Slim 800 kVA Carenado/Silenciado',	'Slim 800 kVA Carenado/Silenciado'),
		('Slim 800 kVA Carenado/Silenciado',	'Slim 800 kVA Carenado/Silenciado'),
			
		('Slim 1100 kVA Carenado/Silenciado',	'Slim 1100 kVA Carenado/Silenciado'),
		('Slim 1250 kVA Carenado/Silenciado',	'Slim 1250 kVA Carenado/Silenciado'),
			
		('Slim 1000 kVA Carenado/Silenciado',	'Slim 1000 kVA Carenado/Silenciado'),
		('Slim 1100 kVA Carenado/Silenciado',	'Slim 1100 kVA Carenado/Silenciado'),
		('Slim 1250 kVA Carenado/Silenciado',	'Slim 1250 kVA Carenado/Silenciado'),
		('Slim 1400 kVA Carenado/Silenciado',	'Slim 1400 kVA Carenado/Silenciado'),
		('Slim 1500 kVA Carenado/Silenciado',	'Slim 1500 kVA Carenado/Silenciado'),
		('Slim 1600 kVA Carenado/Silenciado',	'Slim 1600 kVA Carenado/Silenciado'),
		('Slim 1600 kVA Carenado/Silenciado',	'Slim 1600 kVA Carenado/Silenciado'),
	)
	),
 # alvenaria 
	('Alvenaria',(
        ('Slim 40 kVA Alvenaria' ,'Slim 40 kVA Alvenaria'), 
		('Slim 55 kVA Alvenaria' , 'Slim 55 kVA Alvenaria'),     
		('Slim 60 kVA Alvenaria', 'Slim 60 kVA Alvenaria') ,
		('Slim 63kVA Alvenaria','Slim 63kVA Alvenaria'),
		('Slim 75kVA Alvenaria','Slim 75kVA Alvenaria'),
		('Slim 75 kVA Alvenaria','Slim 75 kVA Alvenaria'),
		('Slim 95 kVA Alvenaria','Slim 95 kVA Alvenaria'),
		('Slim 83 kVA Alvenaria','Slim 83 kVA Alvenaria'),
		('Slim 100 kVA Alvenaria', 'Slim 100 kVA Alvenaria'),
		('Slim 110 kVA Alvenaria', 'Slim 110 kVA Alvenaria'),
		('Slim 123 kVA Alvenaria','Slim 123 kVA Alvenaria'),
		('Slim 125 kVA Alvenaria', 'Slim 125 kVA Alvenaria'),
		('Slim 140 kVA Alvenaria','Slim 140 kVA Alvenaria'),
		('Slim 207 kVA Alvenaria','Slim 207 kVA Alvenaria'),
  
  		('Slim 251 kVA Alvenaria',	'Slim 251 kVA Alvenaria,'),
		('Slim 300 kVA Alvenaria',	'Slim 300 kVA Alvenaria,'),
		('Slim 300 KVA  Alvenaria',	'Slim 300 KVA  Alvenaria,'),
		('Slim 330 KVA  Alvenaria',	'Slim 330 KVA  Alvenaria,'),
		('Slim 360 KVA  Alvenaria',	'Slim 360 KVA  Alvenaria,'),
		('Slim 400 KVA  Alvenaria',	'Slim 400 KVA  Alvenaria,'),
		('Slim 369 kVA Alvenaria',	'Slim 369 kVA Alvenaria,'),
		('Slim 285 kVA Alvenaria',	'Slim 285 kVA Alvenaria,'),
		('Slim 334 kVA Alvenaria',	'Slim 334 kVA Alvenaria,'),
		('Slim 350 kVA Alvenaria',	'Slim 350 kVA Alvenaria,'),

		('Slim 438 kVA Alvenaria',	'Slim 438 kVA Alvenaria,'),
		('Slim 450 kVA Alvenaria',	'Slim 450 kVA Alvenaria,'),
		('Slim 451 kVA Alvenaria',	'Slim 451 kVA Alvenaria,'),
		('Slim 500 kVA Alvenaria',	'Slim 500 kVA Alvenaria,'),
		('Slim 501 kVA Alvenaria',	'Slim 501 kVA Alvenaria,'),
		('Slim 550 kVA Alvenaria',	'Slim 550 kVA Alvenaria,'),
		('Slim 625 kVA Alvenaria',	'Slim 625 kVA Alvenaria,'),
		('Slim 650 kVA Alvenaria',	'Slim 650 kVA Alvenaria,'),
  
		('Slim 550 kVA Alvenaria',	'Slim 550 kVA Alvenaria,'),
		('Slim 625 kVA Alvenaria',	'Slim 625 kVA Alvenaria,'),

		('Slim 563 kVA Alvenaria',	'Slim 563 kVA Alvenaria,'),
		('Slim 642 kVA Alvenaria',	'Slim 642 kVA Alvenaria,'),
		('Slim 700 kVA Alvenaria',	'Slim 700 kVA Alvenaria,'),

		('Slim 720 kVA Alvenaria',	'Slim 720 kVA Alvenaria,'),
		('Slim 752 kVA Alvenaria',	'Slim 752 kVA Alvenaria,'),
		('Slim 770 kVA Alvenaria',	'Slim 770 kVA Alvenaria,'),
		('Slim 800 kVA Alvenaria',	'Slim 800 kVA Alvenaria,'),
		('Slim 800 kVA Alvenaria',	'Slim 800 kVA Alvenaria,'),

		('Slim 1100 kVA Alvenaria',	'Slim 1100 kVA Alvenaria,'),
		('Slim 1250 kVA Alvenaria',	'Slim 1250 kVA Alvenaria,'),

		('Slim 1000 kVA Alvenaria',	'Slim 1000 kVA Alvenaria,'),
		('Slim 1100 kVA Alvenaria',	'Slim 1100 kVA Alvenaria,'),
		('Slim 1250 kVA Alvenaria',	'Slim 1250 kVA Alvenaria,'),
		('Slim 1400 kVA Alvenaria',	'Slim 1400 kVA Alvenaria,'),
		('Slim 1500 kVA Alvenaria',	'Slim 1500 kVA Alvenaria,'),
		('Slim 1600 kVA Alvenaria',	'Slim 1600 kVA Alvenaria,'),
		('Slim 1600 kVA Alvenaria',	'Slim 1600 kVA Alvenaria,'),
	)
	),
	]
	Modelo_Gerador = models.CharField(blank=True, max_length=200, choices = MODELO_CHOICES)

	MARCA_CHOICES = (
		('Perkins','Perkins'),
		('FPT','FPT'),
		('CUMMINS','CUMMINS'),
		('MWM','MWM'),
		('Scania','Scania'),
		('Volvo','Volvo'),
		)
	Fabricante_Motor = models.CharField(blank=True,max_length=200, choices = MARCA_CHOICES)

	Modelo_Motor = models.CharField(u'Modelo Motor', max_length=100)
 
	ICAMENTO_CHOICES = (
		('Único','Único'),
		('Duplo','Duplo'),
		)
	Içamento = models.CharField(u'Içamento', max_length=100 , choices = ICAMENTO_CHOICES, default='Único')

	Tanque_de_combustivel = models.CharField(u'Tanque de combustivel', max_length=100)
	Dimensoes = models.CharField(u'Dimensões',blank=True, max_length=100)
	Peso = models.CharField(u'Peso',blank=True, max_length=100)

	class Meta:
		verbose_name = u'Motor'
		verbose_name_plural = u'Motores'

	def __str__(self):
	    return self.Modelo_Gerador

class Produto(models.Model):

#	proposta = models.ForeignKey("Proposta", on_delete=models.CASCADE)
#	cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
	produto = models.ForeignKey(Motor, on_delete=models.CASCADE)
	imagem = models.ImageField(upload_to='produtos', default= '/produtos/gerador.png')
 
	TENSAO_CHOICES = (

        ('220/127 V ','220/127 V '),
        ('380/220 V','380/220 V'),
        ('440/254 V','440/254 V'),
        ('440/220 V - Monofásico','440/220 V - Monofásico'),
		)
	Tensão_Gerador = models.CharField( max_length=200, choices = TENSAO_CHOICES)
 
	AUT_MAN_CHOICES = (
		('AUTOMATICO','Automático'),
		('MANUAL','Manual'),
		)
	aut_man_Gerador = models.CharField(max_length=200, choices = AUT_MAN_CHOICES)
 
	QTA_CHOICES = (
		('Transferência em rampa','Transferência em rampa'),
		('Transferência a seco','Transferência a seco'),
		)
	QTA_Gerador = models.CharField(blank=True, max_length=200, choices = QTA_CHOICES)

	Controlador_CHOICES = (
		('AGC150','AGC150'),
    	('AGC150 CORE','AGC150 CORE'),
		('AGC150 HIBRIDY','AGC150 HIBRIDY'),
		('AGC200','AGC200'),
		('CGC400','CGC400'),
		('4510','4510'),
		('4520','4520'),
		('7420','7420'),
		('8620','8620'),
		('8620','8620'),
		('8620','8620'),
		)
	Controlador_Gerador = models.CharField(blank=True, max_length=200, choices = Controlador_CHOICES, default='CGC400')
	
#	CARENAGEM_CHOICES = (
#		('CARENADO','CARENADO'),
#		('ALVENARIA','ALVENARIA'),
#		)
#	CARENAGEM_Gerador = models.CharField(blank=True, max_length=200, choices = CARENAGEM_CHOICES)

	Silenciador_CHOICES = (
		('Silencioso Hospitalar','Silencioso Hospitalar'),
		('Silencioso Industrial','Silencioso Industrial'),
		)
	Silenciador_Gerador = models.CharField(blank=True, max_length=200, choices = Silenciador_CHOICES)

	RUIDO_CHOICES = (
		('65 dB(A) @ 1,5 metros ou 55 dB(A) @ 7,0 metros de distância','65 dB(A) @ 1,5 metros ou 55 dB(A) @ 7,0 metros de distância'),
		('70 dB(A) @ 1,5 metros ou 60 dB(A) @ 7,0 metros de distância','70 dB(A) @ 1,5 metros ou 60 dB(A) @ 7,0 metros de distância'),
		('75 dB(A) @ 1,5 metros ou 65 dB(A) @ 7,0 metros de distância','75 dB(A) @ 1,5 metros ou 65 dB(A) @ 7,0 metros de distância'),
		('80 dB(A) @ 1,5 metros ou 70 dB(A) @ 7,0 metros de distância','80 dB(A) @ 1,5 metros ou 70 dB(A) @ 7,0 metros de distância'),
		('85 dB(A) @ 1,5 metros ou 75 dB(A) @ 7,0 metros de distância','85 dB(A) @ 1,5 metros ou 75 dB(A) @ 7,0 metros de distância'),
		)
	Nivel_de_ruído = models.CharField(u'Nivel de ruído', max_length=100, choices = RUIDO_CHOICES , default= '85 dB(A) @ 1,5 metros ou 75 dB(A) @ 7,0 metros de distância')

	quantidade_Gerador = models.DecimalField(blank=True, max_digits=15, decimal_places=0)
	valor_gerador = models.DecimalField(max_digits=15, decimal_places=2)
 
	def soma_gerador(self):
		return self.valor_gerador*self.quantidade_Gerador
	soma_gerador.description = 'Total_Gerador'

	def __str__(self):
	    return self.produto.Modelo_Gerador
	
class Proposta(models.Model):
	cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
	Ordem = models.CharField(u'Número da proposta',max_length=20, unique=True)
	revisão = models.CharField(u'Revisão',max_length=20, default='001')
	produto = models.ForeignKey('Produto', on_delete=models.CASCADE)
#	Motor = models.ForeignKey(Motor, on_delete=models.CASCADE)
	data = models.DateTimeField(auto_now_add=True ) # hora que fez a proposta

#	QUANTIDADE_CHOICES = (
#	("1" , "1"),
#	("2" , "2"),
#	("3" , "3"),
#	("4" , "4"),
#	("5" , "5"),
#	("6" , "6"),
#	("7" , "7"),
#	("8" , "8"),
#	("9" , "9"),
#	("10" , "10"),
#	("11" , "11"),
#	("12" , "12"),
#	("13" , "13"),
#	("14" , "14"),
#	("15" , "15"),
#	("16" , "16"),
#	("17" , "17"),
#	("18" , "18"),
#	("19" , "19"),
#	("20" , "20"),
#	("21" , "21"),
#	("22" , "22"),
#	("23" , "23"),
#	)
#	quantidade_Gerador = models.CharField(max_length=200, choices = QUANTIDADE_CHOICES)
 
#	POTENCIA_CHOICES = (
#        ('40KVA','40KVA'),
#        ('60KVA','60KVA'),
#        ('63KVA','63KVA'),
#        ('75KVA','75KVA'),
#        ('83KVA','83KVA'),
#        ('100KVA','100KVA'),
#        ('110KVA','110KVA'),
#        ('123KVA','123KVA'),
#		)
#	Potencia_Gerador = models.CharField(blank=True, max_length=200, choices = POTENCIA_CHOICES)
 

#	CATEGORY_CHOICES = (
#			('Atrasado','Atrasado'),
#			('AVencer','Á Vencer'),
#			('Pago','Pago'),
#			)
#	situacao = models.CharField(u'Situação', max_length=200, choices = CATEGORY_CHOICES)
	
	CONDICOES_PAGAMENTO_CHOICES = (
		('1x sem juros','1x sem juros'),
		('2x sem juros','2x sem juros'),
		('3x sem juros','3x sem juros'),
		('4x sem juros','4x sem juros'),
		('5x sem juros','5x sem juros'),
		('6x (2,3% juros ao mês)','6x (2,3% juros ao mês)'),
		('7x (2,3% juros ao mês)','7x (2,3% juros ao mês)'),
		('8x (2,3% juros ao mês)','8x (2,3% juros ao mês)'),
		('9x (2,3% juros ao mês)','9x (2,3% juros ao mês)'),
		('10x (2,3% juros ao mês)','10x (2,3% juros ao mês)'),
		('11x (2,3% juros ao mês)','11x (2,3% juros ao mês)'),
		('12x (2,3% juros ao mês)','12x (2,3% juros ao mês)'),
		)
	Condições_de_Pagamento = models.CharField(max_length=100, choices = CONDICOES_PAGAMENTO_CHOICES)

#	CONDICOES_CHOICES = (
#		('FOB','FOB'),
#		('CIF','CIF'),
#		)	
#	Condições_de_entrega = models.CharField(blank=True, max_length=20, choices = CONDICOES_CHOICES, default='CIF')
	
	VALIDADE_CHOICES = (
		('Cinco','5 (Cinco dias)'),
		('Sete','7 (Sete dias)'),
		('Quinze','15 (Quinze dias)'),
		('Trinta','30 (Trinta dias)'),
		('Sessenta','60 (Sessenta dias)'),
		)
	validade = models.CharField(u'Validade da proposta', blank=True, max_length=200, choices = VALIDADE_CHOICES, default= 'Sete') 

#	Instalação = models.BooleanField(default=False)
	CIF = models.BooleanField(u'CIF - frete e o seguro são pagos pelo fornecedor',default=False)
#	FOB = models.BooleanField(default=False)
 
	VALIDADE_CHOICES = (
		('Imediato','Imediato'),
		('Sete','7 (Sete) dias'),
		('Quinze','15 (Quinze) dias'),
		('Vinte','20 (Vinte) dias'),
		('Trinta','30 (Trinta) dias'),
		('Sessenta','60 (Sessenta) dias'),
		)
	Prazo_de_Entrega = models.CharField(blank=True, max_length=200, choices = VALIDADE_CHOICES, default='Sete')

	Frete = models.DecimalField(blank=True, max_digits=15, decimal_places=2, default='0.00')

	INSTALAÇÃO = models.BooleanField(default=False)

	Valor_Instalação = models.DecimalField(blank=True, max_digits=15, decimal_places=2, default='0.00')
#	Total = models.DecimalField(max_digits=15, decimal_places=2)

	def soma_Total(self):
#		return self.Frete+self.Valor_Instalação
		return self.Frete+self.Valor_Instalação+self.produto.valor_gerador*self.produto.quantidade_Gerador
	soma_Total.description = 'Total'
      
	def soma_instalacao(self):
#		return self.Frete+self.Valor_Instalação
		return self.Valor_Instalação+self.produto.valor_gerador*self.produto.quantidade_Gerador
	soma_instalacao.description = 'soma_instalacao'
 
	def imprimir(self):
		return mark_safe("""<a href=\"/proposta/%s/\" target="_blank"><img src=\"/static/images/b_print.png\"></a>""" % self.id)

	class Meta:
		ordering = ['-data']
		verbose_name = u'Proposta'
		verbose_name_plural = u'Propostas'
  
	def __str__(self):
		return self.Ordem + self.cliente.nome 
    #        else:
    #            return self.custom_alias_name

