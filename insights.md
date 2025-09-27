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
🧠 **Descoberta:** 

``      ID_Pedido Data_Pedido ID_Cliente     Segmento           Pais           Cidade      Estado       ID_Produto        Categoria SubCategoria  Valor_Venda
2     CA-2017-138688  12/06/2017   DV-13045    Corporate  United States      Los Angeles  California  OFF-LA-10000240  Office Supplies       Labels       14.620
4     US-2016-108966  11/10/2016   SO-20335     Consumer  United States  Fort Lauderdale     Florida  OFF-ST-10000760  Office Supplies      Storage       22.368
6     CA-2015-115812  09/06/2015   BH-11710     Consumer  United States      Los Angeles  California  OFF-AR-10002833  Office Supplies          Art        7.280
8     CA-2015-115812  09/06/2015   BH-11710     Consumer  United States      Los Angeles  California  OFF-BI-10003910  Office Supplies      Binders       18.504
9     CA-2015-115812  09/06/2015   BH-11710     Consumer  United States      Los Angeles  California  OFF-AP-10002892  Office Supplies   Appliances      114.900
...              ...         ...        ...          ...            ...              ...         ...              ...              ...          ...          ...
9693  CA-2015-144281  10/06/2015   HK-14890    Corporate  United States          Detroit    Michigan  OFF-LA-10003930  Office Supplies       Labels      491.550
9695  CA-2018-154116  15/12/2018   KM-16660     Consumer  United States        Inglewood  California  OFF-PA-10004569  Office Supplies        Paper       22.830
9696  CA-2018-154116  15/12/2018   KM-16660     Consumer  United States        Inglewood  California  OFF-AP-10000027  Office Supplies   Appliances       54.320
9698  CA-2017-105291  30/10/2017   SP-20920     Consumer  United States  San Luis Obispo  California  OFF-FA-10003059  Office Supplies    Fasteners        3.620
9699  CA-2018-147032  31/07/2018   LB-16795  Home Office  United States       Wilmington    Delaware  OFF-PA-10003256  Office Supplies        Paper       11.540
``
------------------------------------------------------------------------------------------------------------------------------------
