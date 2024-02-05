# ENTRADAS
n = int(input()) # índice de 2**n
p = int(input()) # número de subdivisões
char_preto = input() # caractere de preenchimento do triangulo base
altura= 2**n
largura = 2 * altura - 1

# FUNÇÕES
# CRIAR TELA
def criar_tela():
  tela = [ [" " for j in range(largura)] for i in range(altura)]
  return tela
tela = criar_tela()

# IMPRIMIR TELA
def imprime_tela():
  for linha in tela:
    print("".join(linha))

# TRIÂNGULO PRETO   
for i in range(altura):  
  j = (altura-i-1) # posição 1º caractere  
  for l in range(2*i-1+2):    
    tela[i][j] = char_preto
    j = j + 1

# IMPRIMIR MOLDURA
def imprime_moldura(tela,n):
  x = 2*altura+1
  print("+","-"*x,"+",sep='')
  print("|"+" "*x+"|")
  for i in range(altura):
    print("| ",end='')
    for j in tela[i]:
      print(j,end='')
    print(" |")
  print("|"+" "*x+"|")
  print("+","-"*x,"+",sep='')

# TRIÂNGULO BRANCO
def recursao(altura_TB,ponto_i,ponto_j,profundidade):
  if profundidade == 0:
    return  
  j = 0 # posição 1º caractere  
  largura_TB = altura_TB*2-1  
  for i in range(ponto_i,ponto_i-altura_TB,-1):  
    for l in range(largura_TB//2-j,largura_TB//2+j+1):    
      tela[i][l+ponto_j-(altura_TB)+1] = " "
    j = j + 1    
# CHAMADAS RECURSIVAS
# ESQUERDA
  recursao(altura_TB//2,ponto_i,ponto_j-largura_TB//2-1,profundidade-1)
# DIREITA
  recursao(altura_TB//2,ponto_i,ponto_j+largura_TB//2+1,profundidade-1)
# SUPERIOR
  recursao(altura_TB//2,ponto_i-largura_TB//2-1,ponto_j,profundidade-1)
# CHAMADAS FUNÇÕES RECURSÃO E IMPRIME MOLDURA
recursao(altura//2,altura-1,largura//2,p)
imprime_moldura(tela,n)