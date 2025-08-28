# leia o valor em reais e o custo de um dolar
# calcule a quantidade de dolares que o viajante receberá
# exiba o valor em dolares

#entrada
custo_dolar = '''
=========================================
O valor do dolar atualmente está R$5,42
=========================================
'''
print(custo_dolar)

real = float(input ('Quantos reais Você tem? '))
print(f'Você tem R${real:.2f}')
input('Pressione "enter" para converter em dolares')

#processo
converter_dolar = real / 5.42

#saida
print(f'Convertendo, você tem US${converter_dolar:.2f}')