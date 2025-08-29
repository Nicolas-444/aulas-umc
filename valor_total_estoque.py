# Leia a quantidade de unidadades e o valor unitario
# calcule o valor total do estoque
# exiba o valor total do estoque
import os
#entrada
tit = '''
=============================
Quantidade de item no estoque
e valor total.
=============================
'''
print(tit)


quant_itens = 8
valor_unico = 85.00

#processamento
valor_total = quant_itens * valor_unico

input('Pressione "Enter" para ver o relatório')

print(f'No estoque tem {quant_itens} unidades')
print(f'O valor de estoque é R${valor_total:.2f}.')


