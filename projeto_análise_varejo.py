# ANÁLISE EXPLORATÓRIA DE DADOS EM LINGUAGEM PYTHON PARA ÁREA DE VAREJO 

import numpy as np
import pandas as pd
df_dsa = pd.read_csv('dataset.csv')
print(df_dsa)
print ("-=-" * 55)
print("Colunas do DataSet:")
print(df_dsa.columns)
print ("-=-" * 55)
print("Verificando o tipo de cada coluna:")
print(df_dsa.dtypes)
print ("-=-" * 55)
print("Resumo estatístico da coluna com o valor de venda:")
print(df_dsa["Valor_Venda"].describe)
print ("-=-" * 55)
print("Verificando se há valores duplicados:")
print(df_dsa.duplicated())
print ("-=-" * 55)
print("Verificando se há valores ausentes:")
print(df_dsa.isnull().sum)
print ("-=-" * 55)

#  MAIOR VALOR DE VENDA PELA CATEGORIA "OFFICE SUPPLIES"     pergunta 1
print("Maior valor de venda em uma cidade pela categoria OFFICE SUPPLIES:")
df_dsa_p1 = df_dsa[df_dsa["Categoria"] == "Office Supplies"]
print(df_dsa_p1)
df_dsa_p1_total = df_dsa_p1.groupby("Cidade")["Valor_Venda"].sum()
print ("-=-" * 55)
print(df_dsa_p1_total.head())
cidade_maior_venda = df_dsa_p1_total.idxmax()
print(f"Cidade com maior valor de venda para Office Supplies: {cidade_maior_venda}")
print ("-=-" * 55)

# QUAL O TOTAL DE VENDAS POR DATA DO PEDIDO E A MAIOR VENDA EM UM ÚNICO DIA     pergunta 2

print ("-=-" * 55)
print("Total de vendas por data do pedido e a maior venda em um único dia:")
df_dsa_p2 = df_dsa.groupby("Data_Pedido")["Valor_Venda"].sum()
print(df_dsa_p2)
print ("-=-" * 55)
data_com_maior_venda = df_dsa_p2.idxmax()
print(f"A data que obteve o maior valor de venda foi: {data_com_maior_venda}")
print ("-=-" * 55)

# QUAL O TOTAL DE VENDAS POR ESTADO?    pegunta 3 

print ("-=-" * 55)
df_dsa_p3 = df_dsa.groupby("Estado")["Valor_Venda"].sum().reset_index()
print(f"\033[32mO total de vendas por estado é:\033[m\n {df_dsa_p3}")
print ("-=-\033[m" * 55)

# QUAIS SÃO AS 10 CIDADES COM MAIOR TOTAL DE VENDAS    pergunta 4

print ("-=-" * 55)
print(" As 10 cidades com maior valor de venda são:")
df_dsa_p4 = df_dsa.groupby("Cidade")["Valor_Venda"].sum().reset_index().sort_values(by = "Valor_Venda", ascending = False).head(10)
print(df_dsa_p4.head(10))
print ("-=-" * 55)

# QUAL SEGMENTO TEVE O MAIOR TOTAL DE VENDAS?    pergunta 5 
print ("-=-" * 55)
print("Qual segmento obteve o maior total de vendas:")
df_dsa_p5 = df_dsa.groupby("Segmento")["Valor_Venda"].sum().reset_index().sort_values(by = "Valor_Venda", ascending= False)
print(df_dsa_p5.head())
print ("-=-" * 55)
print("O segmento que obteve o maior total de venda foi o de consumer.")
print ("-=-" * 55)

# QUAL O TOTAL DE VENDAS POR ANO E POR SEGMENTO?    pergunta 6

print ("-=-" * 55)
print("O valor de vendas por ano foi:")
df_dsa["Data_Pedido"] = pd.to_datetime(df_dsa["Data_Pedido"], dayfirst = True)
df_dsa["Ano"] = df_dsa["Data_Pedido"].dt.year
df_dsa_p6 = df_dsa.groupby(["Ano", "Segmento"])["Valor_Venda"].sum().reset_index()
print(df_dsa_p6)
print ("-=-" * 55)

# DESCONTOS      pergunta 7

print ("-=-" * 55)
print("Se o valor_Venda for maior que 1000 recebe 15% de desconto, se o valo_Venda for menor que 1000 recebe 10% de desconto.")
df_dsa["Desconto"] = np.where(df_dsa["Valor_Venda"] > 1000, 0.15, 0.10)
print(df_dsa)
print("Ao total, quantos foram de 15% e 10%:")
print(df_dsa["Desconto"].value_counts())
print("No total 457 vendas receberiam desconto de 15%")
print ("-=-" * 55)

# MAIS DESCONTOS    pergunta 8

print ("-=-" * 55)
print("Caso decidam conceder desconto de 15%, qual seria o valor antes e depois desse desconto.")
df_dsa["Valor_Venda_Desconto"] = df_dsa["Valor_Venda"] - (df_dsa["Valor_Venda"] * df_dsa["Desconto"])
print(df_dsa)
df_dsa_p8_vendas_antes_desconto = df_dsa.loc[df_dsa["Desconto"] == 0.15, "Valor_Venda"]
df_dsa_p8_vendas_depois_desconto = df_dsa.loc[df_dsa["Desconto"] == 0.15, "Valor_Venda_Desconto"]
media_vendas_antes_desconto =  df_dsa_p8_vendas_antes_desconto.mean()
media_vendas_depois_desconto = df_dsa_p8_vendas_depois_desconto.mean()
print("Média de vendas antes e depois dos descontos:")
print(f"Média das vendas antes do desconto de 15%: {media_vendas_antes_desconto:.2f}")
print(f"Média das vendas depois do desconto de 15%: {media_vendas_depois_desconto:.2f}")
print ("-=-" * 55)


# QUAL O TOTAL POR CATEGORIA E SUBCATEGORIA, CONSIDERANDO SOMENTE AS TOP 12 SUBCATEGORIAS     pergunta 9

print ("-=-" * 55)
print("Total de vendas por categoria e SubCategoria, considerando somente as Top 12 SubCategorias:")
df_dsa_p9 = df_dsa.groupby(["Categoria", "SubCategoria"]).sum("Valor_Venda").sort_values("Valor_Venda", ascending = False).head(12)
df_dsa_p9 = df_dsa_p9[["Valor_Venda"]].astype(int).sort_values(by = "Categoria").reset_index()
print(df_dsa_p9)
df_dsa_p9_cat = df_dsa_p9.groupby('Categoria').sum(numeric_only = True).reset_index()
print ("-=-" * 55)
print("Valores por categoria:")
print(df_dsa_p9_cat)