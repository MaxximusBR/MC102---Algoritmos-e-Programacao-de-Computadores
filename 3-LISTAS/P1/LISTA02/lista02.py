"""
# EXERCÍCIO 1
print("1 - Pizza Marguerita")
print("2 - Pizza de Calabresa")
print("3 - Pizza de Pepperoni")
print("4 - Pizza de Mussarela")
print("5 - Sair")
n = int(input("Escolha um número de 1 a 5: "))
while n < 5:
  n = int(input("Escolha um número de 1 a 5: "))
  if n == 5:
    break

# EXERCÍCIO 2
n = int(input())
lista = []
for i in range(n):
  lista.append(int(input()))
  lista.sort(reverse=False)
print(lista)
if lista[0] > lista[-1]:
  print("Ordenação decrescente")
elif lista[0] < lista[-1]:
  print("Ordenação crescente")

# EXERCÍCIO 3
m = int(input("Digite o primeiro número: "))
n = int(input("Digite o segundo número: "))
while n!=0 :
  n = m%n
  if n == 0:
    MDC = m
    m = n
print("MDC =",n,m,)

# EXERCÍCIO 5
x = 8
y = 0
while True:
  y = (x % 2) + 10 * y
  x = x // 2
  print('x =', x, 'y =', y)    
  if x == 0:                   # x = 4 y = 0  
  break                        # x = 2 y = 0
while y != 0:                  # x = 1 y = 0
  x = y % 100                  # x = 0 y = 1
  y = y // 10                  # x = 1 y = 0
  print('x =', x, 'y =',y)

# EXERCÍCIO 6
# RESOLUÇÃO COM LISTAS
lista1 = []
lista2 = []
lista3 = []
lista4 = []
c1 = 0
c2 = 0
c3 = 0
c4 = 0
for i in range(26):
  lista1.append(i)
for i in range(26,51):
  lista2.append(i)
for i in range(51,76):
  lista3.append(i)
for i in range(76,101):
  lista4.append(i)
n = int(input())
for i in range(n):
  x = int(input())
  if x in lista1:
    c1 = c1+1
  if x in lista2:
    c2 = c2+1
  if x in lista3:
    c3 = c3+1
  if x in lista4:
    c4 = c4+1
print("[0,25]:",c1)
print("[26,50]:",c2)
print("[51,75]:",c3)
print("[76,100]:",c4)
# SOLUÇÃO SEM LISTAS
n = int(input())
c1 = 0
c2 = 0
c3 = 0
c4 = 0
for i in range(n):
  x = int(input())
  if x >= 0 and x <= 25:
    c1 = c1+1
  elif x > 25 and x <= 50:
    c2 = c2+1
  elif x > 50 and x <= 75:
    c3 = c3+1
  elif x > 75 and x <= 100:
    c4 = c4+1
print("[0,25]:",c1)
print("[26,50]:",c2)
print("[51,75]:",c3)
print("[76,100]:",c4)

# EXERCÍCIO 8
# ERRADO
valor = int(input("Digite um número: "))
fatorial = n = valor
if n >= 0:
  while n > 0:
    n = n - 1
    fatorial = fatorial*n  
  print("O fatorial de", valor, "é igual a:", fatorial)
print("Não existe fatorial de", valor)
# CORRIGIDO
valor = int(input("Digite um número: "))
fatorial = 1
if valor >= 0:
  for i in range(1,valor+1):
    fatorial = fatorial*i  
  print("O fatorial de", valor, "é igual a:", fatorial)
else:
  print("Não existe fatorial de", valor)

# EXERCÍCIO 9
C = int(input())

# EXERCÍCIO 11
n = int(input())
for i in range(n):
  if i == 0:
    print(i+1,end="")
  else:
    print(" "*(i-1),i+1,end="")
  print()
"""
# EXERCÍCIO 12
n = int(input())
for i in range(n):
  for j in range(i+1):
    print(j+1,end="")
  print()
"""
# EXERCÍCIO 13
# SEM LAÇOS ANINHADOS
n = int(input())
for i in range(n):
  print("*"*i,"+","*"*(n-i-1),sep="")

# COM LAÇOS ANINHADOS
n = int(input())
for i in range(n):
  for j in range(n):
    if j == i:
      print("+",end="")
    else:
      print("*",end="")
  print()
"""