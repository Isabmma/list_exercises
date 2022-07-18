"""07.07.02 Exercícios Listas.ipynb

## 1. Faturamento do Melhor e do Pior Mês do Ano

Qual foi o valor de vendas do melhor mês do Ano?
E valor do pior mês do ano?
"""

meses = ['jan', 'fev', 'mar', 'abr', 'mai', 'jun',
         'jul', 'ago', 'set', 'out', 'nov', 'dez']

vendas_1sem = [25000, 29000, 22200, 17750, 15870, 19900]

vendas_2sem = [19850, 20120, 17540, 15555, 49051, 9650]

vendas_ano = vendas_1sem + vendas_2sem

index_maior_valor = vendas_ano.index(max(vendas_ano))
index_menor_valor = vendas_ano.index(min(vendas_ano))

"""## 2. Continuação

Agora relacione as duas listas para printar 'O melhor mês do ano foi {} com {} vendas' e o mesmo para o pior mês do ano.

Calcule também o faturamento total do Ano e quanto que o melhor mês representou do faturamento total.

Obs: Para o faturamento total, pode usar a função sum(lista) que soma todos os itens de uma lista
"""

maior_mes = f"O melhor mês de vendas do ano foi em {meses[index_maior_valor]} com R${vendas_ano[index_maior_valor]}"
menor_mes = f"O pior mês de vendas do ano foi em {meses[index_menor_valor]} com R${vendas_ano[index_menor_valor]}"
print(maior_mes)
print(menor_mes)

faturamento_total = sum(vendas_ano)
print(f"O faturamento total anual foi de R${faturamento_total}")

"""## 3. Crie uma lista com o top 3 valores de vendas do ano (sem fazer "no olho")

Dica: o método remove retira um item da lista.
"""
copy_vendas_ano = vendas_ano.copy()
top_tres = []

count = 3
n = 1 

while n <= 3 :
  index_maior_valor_copy = copy_vendas_ano.index(max(copy_vendas_ano))
  pop_maior_valor = copy_vendas_ano.pop(index_maior_valor_copy)

  top_tres.append(pop_maior_valor)

  n += 1

print (top_tres)