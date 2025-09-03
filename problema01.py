# Cálculo de Porcentagem sobre Produto

import os
roxo = '\033[35m\033m'
fim = '\033[0m'
Tit = '''
================
APP de Desconto
================
'''

Inst = '''
=================================
Insira o nome do produto
A porcentagem de desconto
insira apenas numeros decimais
insira '.' ao invés de ',' 
ex: 30.25
=================================

'''
#Entrada de Dados
nome_produto = input ('Digite o nome do produto: ')

V = float (input('Insira o valor do produto:R$'))
P = float (input('Insira o valor da porcentagem(%)'))


#Processamento de Dados
    
VD = V * P/100
VT = V - VD
input (f'Digite {roxo}ENTER {fim} para gerar o relatório')

#Saída
os.system ('cls')
print (f'Nome do produto: {nome_produto}')
print (f'O desconto foi de R$:{VD:.2f}')
print (f'O Valor com desconto será de: {roxo}R${VT:.2f} {fim}')

