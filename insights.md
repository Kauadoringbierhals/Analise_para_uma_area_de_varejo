### ❓Pergunta 1: Maior valor de venda pela categoria "OFFICE SUPPLIES"? 
**Consulta SQL utilizada:**
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
**Consulta SQL utilizada:**
```python
print("Total de vendas por data do pedido e a maior venda em um único dia:")
df_dsa_p2 = df_dsa.groupby("Data_Pedido")["Valor_Venda"].sum()
print(df_dsa_p2)
print ("-=-" * 55)
data_com_maior_venda = df_dsa_p2.idxmax()
print(f"A data que obteve o maior valor de venda foi: {data_com_maior_venda}")
```
------------------------------------------------------------------------------------------------------------------------------------
