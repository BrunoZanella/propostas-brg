from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.db.models import Sum

from proposta.core.models import Cliente, Proposta, Motor, Produto

# Proposta
@login_required(redirect_field_name='redirect_to')
def proposta(request, id, *args, **kwargs):

    # Recupera a proposta específica
    proposta = Proposta.objects.get(id=id)
    # Recupera os produtos associados à proposta
    produtos = Produto.objects.filter(proposta=proposta)
    clientes = Cliente.objects.filter(proposta=proposta)
    motores = Motor.objects.all()

    # Inicializa a variável para armazenar a soma
    soma_total = 0
    soma_frete = 0
    soma_instalacao = 0
    soma_gerador = 0
    soma_gera = 0
    
    # Itera sobre os objetos de Produto e soma o valor de cada um
    for produto in produtos:
        soma_gera += produto.quantidade_Gerador * produto.valor_gerador
        soma_gerador += soma_gera
            
    # Soma o valor do frete e da instalação à soma total
    soma_total = soma_gera + proposta.Frete + proposta.Valor_Instalação
    soma_frete += soma_gera + proposta.Frete
    soma_instalacao += soma_gera + proposta.Valor_Instalação

    contexto = {'proposta':proposta,
                'produtos':produtos,
                'clientes':clientes,
                'motores':motores,
                'soma_total':soma_total,
                'soma_gera':soma_gera,
                'soma_frete':soma_frete,
                'soma_gerador':soma_gerador,
                'soma_instalacao':soma_instalacao,
                }
    
    return render(request, "proposta.html", contexto)
