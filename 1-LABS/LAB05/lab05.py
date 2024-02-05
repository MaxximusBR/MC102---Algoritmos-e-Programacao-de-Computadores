# ENTRADAS
sigla_da_moeda = str(input())
data = str(input())
valor_compra, valor_venda = map(float, input().split())
valor_min_compra = valor_compra
valor_max_venda = valor_venda
contador = 0
soma_compra = valor_compra
soma_venda = valor_venda

# REPETIÇÃO
while valor_compra != 0 and valor_venda != 0:
  valor_compra, valor_venda = map(float, input().split())
  contador = contador + 1
  soma_compra = soma_compra + valor_compra 
  soma_venda = soma_venda + valor_venda
  if valor_compra != 0:
    if valor_min_compra > valor_compra:
        valor_min_compra = valor_compra
    if valor_max_venda < valor_venda:
        valor_max_venda = valor_compra
  if contador == 4:
    media_cinco_compra = soma_compra / 5
    media_cinco_venda= soma_venda / 5

# SAIDAS
media_hist_compra = soma_compra / contador
media_hist_venda = soma_venda / contador
print("Moeda:",sigla_da_moeda)
print("Data:",data)
print("Valor minimo para compra:",format(valor_min_compra, ".4f"))
print("Valor maximo para venda:",format(valor_max_venda, ".4f"))
print("Medias das cinco cotacoes mais recentes:",format(media_cinco_compra, ".4f"),format(media_cinco_venda, ".4f"))
print("Medias do historico:",format(media_hist_compra, ".4f"),format(media_hist_venda, ".4f"))