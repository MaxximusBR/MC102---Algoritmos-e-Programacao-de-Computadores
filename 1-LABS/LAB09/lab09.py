# FUNÇÃO CONSTRUIR ENTRADA
def construir_entrada():
  # ENTRADAS
  diagrama_entrada = [] # MATRIZ  
  palavras = []  
  # REPETIÇÃO
  while True :
    l = input()
    if l.isdigit():
      n = int(l)
      break
    else:
      l = l.split()
      diagrama_entrada.append(l)
  return diagrama_entrada, n

# FUNÇÃO CONTAR PALAVRAS
def contar_palavras(n):
  palavras = []
  for m in range(n):
    palavra = input()
    palavras.append(palavra)
  return palavras

# FUNÇÕES PERCORRER DIREÇÕES
# Horizontal direita
def horizontal_direita(diag, posx, posy, palavra):
  lista = []
  if len(palavra) <= (len(diag[0]) - posy+1):
    for i in range(len(palavra)):
      if len(diag) and diag[posx][posy+ i]==palavra[i]:
        lista.append((posx,posy + i))
      else:
        lista = []
        break
  return lista

# Horizontal esquerda
def horizontal_esquerda(diag, posx, posy, palavra):
  lista = []
  if len(palavra)  <= posy+1:
    for i in range(len(palavra)):
      if diag[posx][posy - i] == palavra[i]:
        lista.append((posx,posy - i))
      else:
        lista = []
        break
  return lista

# Vertical cima
def vertical_cima(diag, posx, posy, palavra):
  lista = []
  if len(palavra)  <= posx+1:
    for i in range(len(palavra)):
      if diag[posx - i][posy] == palavra[i]:
        lista.append((posx - i,posy))
      else:
        lista = []
        break
  return lista

# Vertical baixo
def vertical_baixo(diag, posx, posy, palavra):
  lista = []  
  if len(palavra) <= (len(diag) - posx+1):
    for i in range(len(palavra)):
      if diag[posx + i][posy] == palavra[i]:
        lista.append((posx + i,posy))
      else:
        lista = []
        break
  return lista

# Diagonal superior direita
def diagonal_sup_dir(diag, posx, posy, palavra):
  lista = []
  if len(palavra) <= posx+1 and len(palavra) <= (len(diag[0]) - posy+1):    
    for i in range(len(palavra)):      
      if diag[posx - i][posy + i] == palavra[i]:
        lista.append((posx - i, posy + i))        
      else:
        lista = []
        break
  return lista 

# Diagonal superior esquerda
def diagonal_sup_esq(diag, posx, posy, palavra):
  lista = []
  if len(palavra) <= posy+1  and len(palavra) <= posx+1:
    for i in range(len(palavra)):
      if diag[posx - i][posy - i] == palavra[i]:
        lista.append((posx - i, posy - i))
      else:
        lista = []
        break
  return lista

# Diagonal inferior direita
def diagonal_inf_dir(diag, posx, posy, palavra):
  lista = []
  if len(palavra) <= (len(diag[0]) - posy+1) and len(palavra) <= len(diag) - posx+1:
    for i in range(len(palavra)):      
      if diag[posx + i][posy + i] == palavra[i]:
        lista.append((posx + i, posy + i))
      else:
        lista = []
        break
  return lista 

# Diagonal inferior esquerda
def diagonal_inf_esq(diag, posx, posy, palavra):
  lista = []
  if len(palavra) <= posy+1 and len(palavra) <= len(diag) - posx+1 :
    for i in range(len(palavra)):      
      if diag[posx + i][posy - i] == palavra[i]:
        lista.append((posx + i, posy - i))
      else:
        lista = []
        break
  return lista 

# FUNÇÃO BUSCA PALAVRAS
def busca_palavra(diag, palavra):
  lista =[]
  altura = len(diag)
  largura = len(diag[0])
  contagem = 0
  for i in range(altura):
    for j in range(largura):
      if diag[i][j] == palavra[0]:
        l = horizontal_direita(diag, i, j, palavra)
        if l != []:          
          contagem += 1
        lista += l
        l = horizontal_esquerda(diag, i, j, palavra)
        if l != []:
          contagem += 1
        lista += l
        l = vertical_cima(diag, i, j, palavra)
        if l != []:
          contagem += 1
        lista += l
        l = vertical_baixo(diag, i, j, palavra)
        if l != []:
          contagem += 1
        lista += l
        l = diagonal_sup_dir(diag, i , j, palavra)
        if l != []:
          contagem += 1
        lista += l
        l = diagonal_sup_esq(diag, i, j, palavra)
        if l != []:
          contagem += 1
        lista += l
        l = diagonal_inf_dir(diag, i, j, palavra)
        if l != []:
          contagem += 1
        lista += l
        l = diagonal_inf_esq(diag, i, j, palavra)
        if l != []:
          contagem += 1
        lista += l            
  return lista, contagem

# FUNÇÃO PRINT DIAGRAMA
def print_diagrama(diag, lista):
  diagrama_saida = [["." for x in range(len(diag[0]))] for y in range(len(diag))]
  for i in range(len(lista)):
    x = lista[i][0]
    y = lista[i][1]
    diagrama_saida[x][y] = diag[x][y]
  for i in range(len(diagrama_saida)):
    for j in range(len(diagrama_saida[0])):
      if j == len(diagrama_saida[0])-1:
        print(diagrama_saida[i][j])
      else:
        print(diagrama_saida[i][j],"",end="")

# IMPRESSÃO DIAGRAMA
diag, num = construir_entrada()
lista_palavras = contar_palavras(num)
lista = []
lista_final= []
dicionario = {}
for palavra in lista_palavras:
  lista, contagem = busca_palavra(diag, palavra)
  lista_final += lista
  dicionario[palavra] = contagem
print_diagrama(diag,lista_final)
for palavra in sorted(dicionario):
  print(palavra,": ",dicionario[palavra],sep="")