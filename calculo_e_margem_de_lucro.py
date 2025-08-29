# exiba o valor de venda e o valor de custo
# calcule o lucro obtido
# calcule a margem de lucro em porcentagem
# exiba o lucro e margem de lucro

#entrada de dados
tit = '''
====================================
NK_Oversized (camisetas Oversized)
Valor da camiseta: R$85.00
Valor do custo: R$35.00
====================================
'''
print(tit)

camisa_valor = 85.00
custo_camisa = 35.00

#processamento
lucro = camisa_valor - custo_camisa
margem = (lucro / custo_camisa) * 100

input ('Pressione "Enter" para ver o lucro e a margem de lucro...')

#saida de dados
print(f'O lucro obtido foi de R${lucro:.2f}')
print(f'A margem de lucro foi de {margem:.2f}%')
