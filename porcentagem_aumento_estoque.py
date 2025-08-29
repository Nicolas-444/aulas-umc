# leia o estoque atual e a porcentagem de aumento
# calcule o novo estoque
# exiba o novo estoque

#entrada de dados
tit = '''
O estoque atual está com 35.468 unidades
e na próxima segunda-feira vai receber
um aumento de 43% de aumento no número de
unidades.

'''
print(tit)
quant_atual = 35468
porcent = 43.00

# processamento

novo_estoque = quant_atual + (quant_atual * porcent) / 100
print(f' A quantidade do novo estoque é de {novo_estoque:.0f} unidades.')
