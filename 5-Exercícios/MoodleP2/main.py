# Moodle P2
# LISTAS- AC06
'''# Ex1
lista = [1, 2]
lista.append("palavra")
print(lista)

# Ex2
lista = [1, 2]
lista.append([3, 4])
print(lista)

# Ex3
lista = [1, 2]
lista = lista + [3, 4]
print(lista)

# Ex4
A = [1, 2, 3]
B = A
B[0] = 0
print(A)

# Ex5
A = [1, 2, 3]
B = A + [4]
print(A)
print(B)

# Ex6
lista = [1, [2, 3], 4, 5]
sublista = lista[1]
sublista[0] = 0
print(lista[1])

-----------------------------------------------------------
# DICIONÁRIOS - AC08
# Ex1 - O que será escrito pelo programa? 
dd = {0: "Campinas", "1": "Valinhos", 2.0: "Ubatuba"}
print(dd[1])

# Ex2 - O que será escrito pelo programa? 
dd = {[0]: "Campinas", ["1"]: "Valinhos", (2): "Ubatuba"}
print(dd[1])

# Ex3 - O que será escrito pelo programa? 
dd = {0: "Campinas", 1: "Valinhos", 2: "Ubatuba"}
dd[1] = dd[2]
print(dd[1])

# Ex4 - O que será escrito pelo programa? 
dd = {0: "Campinas", 1: "Valinhos", 0: "Ubatuba"}
print(dd[0])

# Ex5 - O que será escrito pelo programa? 



# Ex6 - O que será escrito pelo programa? 
dd = {0: "Campinas", 1: "Valinhos", 2: "Ubatuba"}
dd[0] = dd[2]
del(dd[0])
print(dd[0])

# Ex7 - O que será escrito pelo programa? 
dd = {0: "Campinas", 1: "Valinhos", 2: "Ubatuba"}
dd[4] = "Vinhedo"
print(dd[3])

# Ex8 - O que será escrito pelo programa? 
dd = {0: "Campinas", 1: "Valinhos", 2: "Ubatuba"}
dd[-1] = "Sumaré"
print(dd[-1])

# Ex9 - O que será escrito pelo programa? 
num_letra = {0: "A", 1: "B", 2: "C", 3: "D", 4: "E"}
for num in range(5):
    if num % 2 == 0:
        print(num_letra[num])

# Ex10 - O que será escrito pelo programa? 
num_letra = {0: "A", 2: "C", 5:"F", 10:"J"}
for num in range(1, 4):
    print(num_letra[num])

# Ex11 - O que será escrito pelo programa? 
letra_num = {"A":0, "B":1, "C":2, "D":3, "E":4}
for num in range(len(letra_num)):
    if num % 2 == 0:
         print(letra_num[num])

# Ex12 - O que será escrito pelo programa? 
letra_num = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4}
num_letra = {0: "A", 1: "B", 2: "C", 3: "D", 4: "E"}
print(letra_num[num_letra[0]] == 0)

----------------------------------------------------------
# FUNÇÕES - AC07
# Ex1
def soma(a, b):
   print(a + b)
c = 10
d = 5	
soma(c, d)

# Ex2
def soma(a, b):
   return a + a
c = 10
d = 5	
r = soma(c, d)
print("resultado =", r)

# Ex3
def soma(a, b):
   return a + b
r = soma(10, 5)
print("resultado =", r)

# Ex4
def soma(a, b, c):
   return a + b + c
d = 10
e = 5	
r = soma(d, e)
print("resultado =", r)
# TypeError: soma() missing 1 required positional argument: 'c'

# Ex5
def soma(a, b, c):
   return a + b + c
d = 10
e = 5	
r = soma(d, e, e)
print("resultado =", r)

# Ex8
def soma(a, b):
   return a + b
def subtrai(a, b):
   return a - b
print(soma(soma(10,5), subtrai(8,3)))

# Ex9
def soma(a, b):
   c = a + b
c = 10
d = 5	
soma(c, d)
print(c)

# Ex10
def funcao(lista):
   lista = [80, 90, 100]   
lista = [10, 20, 30]
funcao(lista)
print(lista)

# Ex11
def funcao(lista):
  lista[0] = 5
lista = [10, 20, 30]
funcao(lista)
print(lista)

# Ex12
def funcao(lista):
   lista[0] = 5
lista = [10, 20, 30]
funcao(lista[0:])
print(lista)

-----------------------------------------------------
# USO E ESCOPO DE PARÂMETROS

# Ex1
def quadrado(a):
    b = a*a
    return b
def metade(a):
    c = a/2
    return c
a = float(input())
d = quadrado(a) + metade(a)
print(d)

# Ex2
# O retorno de uma função é: valor de retorno de uma função, o qual pode ser utilizado pela função ou módulo que a chamou

# Ex3
def soma1(a):
  c = a + 1
  return c
def sub1(b):
  d = b - 1
  return d
var = soma1(3)*sub1(3)
print(var)

# Ex4
def medArit(a,b):
  c = (a+b)/2
  return c
a = float(input())
b = float(input())
#print(medArit(a,b)) FUNCIONA!
#x = medArit(b,a)
#print(x) FUNCIONA!
#medArit(a,b)
#print(a,b) NÃO FUNCIONA!
#resultado = medArit(a,b)
#print(resultado) FUNCIONA!

# Ex5
# INCORRETA: Uma função pode ou nãoter um valor de retorno

# Ex6
def fuu():
   var = 5
var = 3
fuu()
print (a) # 'a' não está definido
# A função apresenta erros de sintaxe, pois não possui parâmetros.

# Ex7
#def soma(a,b):
#  return a + b
a = 2
b = 3 
print(soma (a, b))

# Ex8
def fatorial(a):
   # Linha 2 - NÃO É NECESSÁRIO INSERIR NENHUM CÓDIGO
   fat = 1
   while a > 0:
      fat = fat * a      
      a -= 1
   return fat
print(fatorial(4))

# Ex9
#Escopo é a característica que determina onde uma variável pode ser utilizada como um identificador em um programa, como por exemplo dentro de uma função.
-----------------------------------------------------------

# RECURSÃO
# Ex1
def fat(n):
   return 1 * fat(n-1)
print("fat =", fat(5))

# Ex2
def fat(n):
  if n == 1:
    return 0
  return n * fat(n-1)
print("fat =", fat(5))

# Ex3
def fat(n):
   if n == 1:
     return 1
   return n * fat(n-1)
print("fat =", fat(5))

# Ex4
def enesimo_fibo(n):
   if n == 1 or n == 2:
      return  1
   return enesimo_fibo(n-1) + enesimo_fibo(n-2)
print("enésimo_fibo =" , enesimo_fibo(5))

# Ex5
def rec(n):
  print("Recursão foi chamada com n =",n)
  if n == 10:
    return  1
  else:
    resposta = 1 + rec(n+1)
    print("resultado intermediário para 1 +","rec(" ,n+1, "): ", resposta)
    return resposta
print("rec =", rec(5))
#Recursão foi chamada com n = 5
#Recursão foi chamada com n = 6
#Recursão foi chamada com n = 7
#Recursão foi chamada com n = 8
#Recursão foi chamada com n = 9
#Recursão foi chamada com n = 10
#resultado intermediário para 1 + rec( 10 ):  2
#resultado intermediário para 1 + rec( 9 ):  3
#resultado intermediário para 1 + rec( 8 ):  4
#resultado intermediário para 1 + rec( 7 ):  5
#resultado intermediário para 1 + rec( 6 ):  6
#rec = 6

# Ex6
def rec(n):
   print(n)
   if n == 0:
      return 
   rec(n-1)
rec(4

# Ex7
def rec(n):
   if n == 0:
     return 
   rec(n-1)
   print(n)
rec(4)

# Ex8
def expr_soma(lista):
   if len(lista) == 1:
     print(lista[0], end="")
     return 
   print("(", lista[0], " + ", sep="", end="")
   expr_soma(lista[1:])
   print(")", end="")
expr_soma([1,3,5,7])

# Ex9
def expr_soma(lista):
   if len(lista) == 1:
     print(lista[0], end="")
     return 
   print("(", end="")
   expr_soma(lista[:-1])
   print("+", lista[-1], ")", sep="", end="")
expr_soma([1,3,5,7])

# Ex10
def expr_soma(lista):
   if len(lista) == 1:
     print(lista[0], end="")
     return 
   print("(", end="")
   expr_soma(lista[:-1])
   print("+", lista[-1], ")", sep="", end="")
expr_soma([1,3,5,7])'''

# Ex11
def expr_soma(lista):
   n = len(lista)
   if n == 1:
      print(lista[0], end="")
      return 
   print("(", end="")
   expr_soma(lista[:n // 2])
   print("+", end="")
   expr_soma(lista[n // 2:])
   print(")", end="")
expr_soma([1,3,5,7])
