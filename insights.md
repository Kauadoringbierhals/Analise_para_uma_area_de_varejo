### ❓Pergunta 1: Maior valor de venda pela categoria "OFFICE SUPPLIES"? 
**Consulta Python utilizada:**
```python
df_dsa_p1 = df_dsa[df_dsa["Categoria"] == "Office Supplies"]
print(df_dsa_p1)
df_dsa_p1_total = df_dsa_p1.groupby("Cidade")["Valor_Venda"].sum()
print ("-=-" * 55)
print(df_dsa_p1_total.head())
cidade_maior_venda = df_dsa_p1_total.idxmax()
print(f"Cidade com maior valor de venda para Office Supplies: {cidade_maior_venda}")
```
------------------------------------------------------------------------------------------------------------------------------------
### ❓Pergunta 2: Qual o total de vendas por data do pedido e a maior venda em um único dia?
**Consulta Python utilizada:**
```python
df_dsa_p2 = df_dsa.groupby("Data_Pedido")["Valor_Venda"].sum()
print(df_dsa_p2)
print ("-=-" * 55)
data_com_maior_venda = df_dsa_p2.idxmax()
print(f"A data que obteve o maior valor de venda foi: {data_com_maior_venda}")
```
------------------------------------------------------------------------------------------------------------------------------------
### ❓Pergunta 3: Qual é o total de vendas por estado?
**Consulta Python utilizada:**
``` python
df_dsa_p3 = df_dsa.groupby("Estado")["Valor_Venda"].sum().reset_index()
print(f"\033[32mO total de vendas por estado é:\033[m\n {df_dsa_p3}")
```
------------------------------------------------------------------------------------------------------------------------------------
### ❓Pergunta 4: Quais são as 10 cidades com maior total de vendas?
**Consulta Python utilizada:**
``` python
print(" As 10 cidades com maior valor de venda são:")
df_dsa_p4 = df_dsa.groupby("Cidade")["Valor_Venda"].sum().reset_index().sort_values(by = "Valor_Venda", ascending = False).head(10)
print(df_dsa_p4.head(10))
```
------------------------------------------------------------------------------------------------------------------------------------
### ❓Pergunta 5: Qual segmento teve o maior total de vendas?
**Consulta Python utilizada:**
``` python
print("Qual segmento obteve o maior total de vendas:")
df_dsa_p5 = df_dsa.groupby("Segmento")["Valor_Venda"].sum().reset_index().sort_values(by = "Valor_Venda", ascending= False)
print(df_dsa_p5.head())
print("O segmento que obteve o maior total de venda foi o de consumer.")
```
------------------------------------------------------------------------------------------------------------------------------------
### ❓Pergunta 6: Qual o total de vendas por ano e por ano?
**Consulta Python utilizada:**
```python
print("O valor de vendas por ano foi:")
df_dsa["Data_Pedido"] = pd.to_datetime(df_dsa["Data_Pedido"], dayfirst = True)
df_dsa["Ano"] = df_dsa["Data_Pedido"].dt.year
df_dsa_p6 = df_dsa.groupby(["Ano", "Segmento"])["Valor_Venda"].sum().reset_index()
print(df_dsa_p6)
```
------------------------------------------------------------------------------------------------------------------------------------
### ❓Pergunta 7: Quantas vendas receberam 15% de descontos?
**Consulta Python utilizada:**
``` python
print("Se o valor_Venda for maior que 1000 recebe 15% de desconto, se o valo_Venda for menor que 1000 recebe 10% de desconto.")
df_dsa["Desconto"] = np.where(df_dsa["Valor_Venda"] > 1000, 0.15, 0.10)
print(df_dsa)
print("Ao total, quantos foram de 15% e 10%:")
print(df_dsa["Desconto"].value_counts())
print("No total 457 vendas receberiam desconto de 15%")
```
------------------------------------------------------------------------------------------------------------------------------------
### ❓Pergunta 8: Qual seria a média do valor de venda antes e depois dos desconto?
**Consulta Python utilizada:**
```python
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
```
------------------------------------------------------------------------------------------------------------------------------------
### ❓Pergunta 9: Qual o total por categoria e subcategoria, considerando somente as top 12 subcategorias?
**Consulta Python utilizada:**
```python
print("Total de vendas por categoria e SubCategoria, considerando somente as Top 12 SubCategorias:")
df_dsa_p9 = df_dsa.groupby(["Categoria", "SubCategoria"]).sum("Valor_Venda").sort_values("Valor_Venda", ascending = False).head(12)
df_dsa_p9 = df_dsa_p9[["Valor_Venda"]].astype(int).sort_values(by = "Categoria").reset_index()
print(df_dsa_p9)
df_dsa_p9_cat = df_dsa_p9.groupby('Categoria').sum(numeric_only = True).reset_index()
print ("-=-" * 55)
print("Valores por categoria:")
print(df_dsa_p9_cat)
```
