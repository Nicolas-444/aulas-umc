# escolha entre o  bis, cachorro e o teclado...
# informe o valor do item e % de desconto que o mesmo tem
# cada item tem um desconto diferente
# depois da escolha, calcule o valor do desconto no valor do produto
# exiba o valor final para ser pago

# entrada de dados
import os

tit = '''
=========================================
Valores dos produtos:

Bis: R$10.00, desconto de 35%

Cachorro: R$250.00, desconto de 43%

Teclado: R$180.00, desconto de 67%
=========================================
'''
print(tit)


escolha = int(input('Escolha: (1)Bis - (2Cachorro - (3)Teclado: '))

#processamento
valor_bis = 10.00
desconto_bis = 35.00
valor_desconto_bis = valor_bis /100 * desconto_bis
valor_final_bis = valor_bis - valor_desconto_bis


valor_cachorro = 250.00
desconto_cachorro = 43.00
valor_desconto_cachorro  = valor_cachorro / 100 * desconto_cachorro
valor_final_cachorro = valor_cachorro - valor_desconto_cachorro

valor_teclado = 180.00
desconto_teclado = 67.00
valor_desconto_teclado = valor_teclado /100 * desconto_teclado
valor_final_teclado = valor_teclado - valor_desconto_teclado


#saida de dados
if escolha == 1:
    input('Você escolheu a opção "Bis", Pressione "Enter" para ver o valor Final')
    print(f'O valor final do Bis ficou: R${valor_final_bis:.2f}') 

elif escolha == 2: 
    input('Você escolheu a opção "Cachorro", Pressione "Enter" para ver o valor Final')
    print(f'O valor final do cachorro ficou R${valor_final_cachorro:.2f}')

elif escolha == 3:
    input('Você escolheu a opção "Teclado", Pressione "Enter" para ver o valor Final')
    print(f'O valor final do teclado ficou: R${valor_final_teclado:.2f}')

else:
    print('ERROR')

    



