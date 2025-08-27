#valor do produto e a porcentagem de desconto
#calcule o valor de desconto
#calcule o valor final a ser pago
#exiba o valor de desconto e o valor final
import os

title = '''
====================
Camiseta Oversized
====================
'''
print(title)

#entrada de dados
valor_camiseta = 85.00
porcentagem_desconto = 20

#processamento
valor_descontado = valor_camiseta /100 * porcentagem_desconto
valor_final_pagar = valor_camiseta - valor_descontado

#saida de dados
print(f'Com o desconto de 20%, Você economizara R${valor_descontado:.2f}')
print(f'Com isso o valor total fica: R${valor_final_pagar:.2f}')


