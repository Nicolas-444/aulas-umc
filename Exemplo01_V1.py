# UMC 
# Programador
# Exemplo 01
import os
Tit= '''
===================
Portal do Professor
===================
'''
Inst='''
Notas com duas casa decimais.
Escala de 0 a 10
Separador decimal é o ponto
'''
print (Tit)
print (Inst)
# Entrada de Dados
NM=input ("Entre com o nome: ")
N1=float(input (f"Entre com a primeira nota do aluno(a) {NM}: "))
N2=float(input (f"Entre com a segunda nota do aluno(a) {NM}: "))
input (" Pressione enter para gerar o relatório")
# Processamento
MS= (N1+2*N2)/3 # Media com N2 tendo peso 2
# Saida
os.system("cls")
print (Tit)
print (f"Nome do aluno: {NM}")
print (f"N1=: {N1:.2f}")
print (f"N2=: {N2:.2f}")
print (f"MS=: {MS:.2f}")