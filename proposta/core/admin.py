# -*- Mode: Python; coding: utf-8 -*-
from django import forms
from django.contrib import admin
from .models import Cliente, Motor, Produto, Proposta
from django.utils.html import format_html
from django.contrib.admin.views.main import ChangeList
from django.db.models import Sum, Avg

from django.contrib.auth.models import User

 

class TotalChangeList(ChangeList):
	fields_to_total = ['valor',]

	def get_total_values(self, queryset):
		total = Proposta()
		total.custom_alias_name = "Totals"
		for field in self.fields_to_total:
			setattr(total, field, queryset.aggregate(total=Sum('Frete')+('Valor_Instalação')+('Total'))['total'])
		return total

	def get_results(self, request):
		super(TotalChangeList, self).get_results(request)
		total = self.get_total_values(self.queryset)
		len(self.result_list)
		self.result_list._result_cache.append(total)

class MotorAdmin(admin.ModelAdmin):
	list_display = ['Modelo_Gerador', 'Fabricante_Motor',  'Modelo_Motor', 'Tanque_de_combustivel', 'Dimensoes', 'Peso']

class ProdutoInline(admin.StackedInline):
    model = Produto
    extra = 0
    
class PropostaAdmin(admin.ModelAdmin):

	def get_changelist(self, request, **kwargs):
		return TotalChangeList

	inlines = [ProdutoInline,]
	list_display = ['cliente', 'Ordem', 'data', 'imprimir']
	search_fields = ['cliente__nome']
	list_filter = ['cliente__nome', 'data', 'Ordem']
#	raw_id_fields = ['cliente']
	# list_editable = ['valor']
	list_per_page = 30
	save_on_top=True
 
	def validade_Proposta(self, obj):
		if obj.validade == 'Sessenta':
			color = 'green'
		elif obj.validade == 'Trinta':
			color = 'green'
		elif obj.validade == 'Cinco':
			color = 'red'
		elif obj.validade == 'Sete':
			color = 'red'
		else:
			color = 'orange'
		return format_html('<strong><p style="color: {}">{}</p></strong>'.format(color, obj.validade))

	validade_Proposta.allow_tags = True

class ProdutoAdmin(admin.ModelAdmin):
    pass

admin.site.register(Motor, MotorAdmin)
admin.site.register(Proposta, PropostaAdmin)
admin.site.register(Produto, ProdutoAdmin)
