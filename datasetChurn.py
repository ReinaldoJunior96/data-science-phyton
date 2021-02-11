import pandas as pd
import seaborn as sbr
import statistics as sts
import matplotlib.pyplot as plt

dataset = pd.read_csv('Churn.csv', sep=";")
# Alterar nome das colunas para melhorar a identificação de cada coisa
dataset.columns = ["Id", "Score", "Estado", "Genero", "Idade", "Patrimonio", "Saldo", "Produtos", "TemCartCredito",
                   "Ativo", "Salario", "Saiu"]

# print(dataset.groupby(['Estado']).size())
# print(dataset['Score'].describe())
# print(dataset['Idade'].describe())
# dataset['Saldo'].describe()
# dataset['Salario'].describe()

#      ***** Tratamento de Genero ******      #
# Problema: Titulo dos dados repetidos, só que de forma diferente
# print("********** Dados sem tratamento *********")
# print(dataset.groupby(['Genero']).size())
# print("****************")
# Verifica registro nulo
# print("Quantidade de NAN: " + str(dataset['Genero'].isnull().sum()))
# print("****************")
# Faz a substituição dos NAN
dataset['Genero'].fillna('Masculino', inplace=True)
# print("Quantidade de NAN: " + str(dataset['Genero'].isnull().sum()))
# print("****************")
# Remover os inconsistência dos dados "F, Fem, M" alterar apenas para Masculino e Feminino
dataset.loc[dataset['Genero'] == "M", "Genero"] = "Masculino"
dataset.loc[dataset['Genero'] == "F", "Genero"] = "Feminino"
dataset.loc[dataset['Genero'] == "Fem", "Genero"] = "Feminino"
# print("********** Dados Tratados *********")
# print(dataset.groupby(['Genero']).size())

#      ***** Tratamento de Idade ******      #
# Problema: Idades negativas, Idades Zeradas e Idades fora do comum (exemplo pessoas com 140 anos)
print(dataset['Idade'].describe())
dataset.loc[dataset['Idade'] <= 0, "Idade"] = sts.median(dataset['Idade'])
dataset.loc[dataset['Idade'] > 100, "Idade"] = sts.median(dataset['Idade'])
print(dataset['Idade'].describe())
