# -*- coding: utf-8 -*-
"""Análise de Dados 1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1EGlmFekK6DRXn3aumfMzt2ClRSnfKuYf
"""

import pandas as pd

# from google.colab import files
# uploaded = files.upload()

clientesBanco = pd.read_csv('ClientesBanco.csv', encoding = 'latin-1')

clientesBanco.head()

display(clientesBanco)

clientesBancoSemNumCliente = clientesBanco.drop('CLIENTNUM', axis = 1)

display(clientesBancoSemNumCliente)

clientesCom3Dependentes = clientesBancoSemNumCliente.drop(1, axis = 0)

clientesCom3Dependentes.head()

somaLimiteDisponivel = clientesBancoSemNumCliente['Limite Disponível'].sum()
print(somaLimiteDisponivel)

somaLimiteDisponivelEducacao = clientesBancoSemNumCliente[['Educação', 'Limite Disponível']].groupby('Educação').sum()
display(somaLimiteDisponivelEducacao)

contadorTodasColunas = pd.DataFrame(clientesBanco)

print(contadorTodasColunas.count())

countEducacao = clientesBanco['Educação'].value_counts()
print(countEducacao)

media = pd.DataFrame()

describeEdu = clientesBanco['Educação'].describe()
display(describeEdu)

# somaLimiteDisponivelEducacao = clientesBancoSemNumCliente[['Educação', 'Limite Disponível']].groupby('Educação').sum()

somaDoutorado = clientesBancoSemNumCliente['Educação']=='Doutorado'
soma = somaDoutorado.sum()
print(soma)

# variavel = clientesBancoSemNumCliente.sort_values("Educação", inplace )
# Calculo media
limite = clientesBancoSemNumCliente['Limite Disponível']
eduDoutorado = clientesBancoSemNumCliente['Educação']
filtro = clientesBancoSemNumCliente.where(limite, eduDoutorado, inplace = True)
print(filtro)

