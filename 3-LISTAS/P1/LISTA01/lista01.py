# EXERCÍCIO 1
idade_pessoa_anos = int(input())
area_quintal_m2 = float(input())
media_chuva_fev = float(input())
n_estrelas_galaxia = int(input())

# EXERCÍCIO 2
a = 10          # a = 10
b = a           # b = 10
c = 9           # c = 9
d = c           # d = 9
c = c + 1       # c = 10

# EXERCÍCIO 3
x = float(input("Digite um inteiro"))
f_x = x**0.5 + x/2 + x**x
print("f(",x,") =",f_x)

# EXERCÍCIO 4
x = int(input("Digite o valor x: "))
y = int(input("Digite o valor y: ")) 
x = x + y
y = x - y
x = x - y
print("x =",x)
print("y =",y)

# EXERCÍCIO 5
a = int(input("Digite o lado a: "))
b = int(input("Digite o lado b: ")) 
c = int(input("Digite o lado c: "))
s = (a+b+c)/2
A = (s*(s-a)*(s-b)*(s-c))**0.5
if a == b == c:
  print("Triângulo equilátero")
  print("Área do triângulo: ",A)
elif a != b != c != a: 
  print("Triângulo escaleno")
  print("Área do triângulo: ",A)
else:
  print("Triângulo isósceles")
  print("Área do triângulo: ",A)

# EXERCÍCIO 6
# ERRADO
print("Digite um número:")
a = int(input())
if a % 2 == 0 and a < 100:
  print("O número é par e menor do que 100")
else:
  if a >= 100:
    print("O número é par e maior do que 100")
if a % 2 != 0 and a < 100:
  print("O número é ímpar e menor do que 100")
else:
  if a >= 100:
    print("O número é ímpar e maior ou igual que 100")
# CORRIGIDO
a = int(input("Digite um número:"))
if a % 2 == 0:
  if a < 100:
    print("O número é par e menor do que 100")
  else:  
    print("O número é par e maior ou igual a 100")
elif a % 2 != 0:
  if a < 100:
    print("O número é ímpar e menor do que 100")
  else:
    print("O número é ímpar e maior ou igual a 100")

# EXERCÍCIO 7
U = str(input("Digite a unidade de medida de temperatura: "))
T = float(input("Digite os graus: "))
if U == "C":
  C = T
  F = C*1.8 + 32
  print("Temperatura",C,"Graus Celsius")
  print("Temperatura",format(F,'.2f'),"Graus Fahrenheit")
elif U == "F":
  F = T
  C = (5/9)*(F - 32)
  print("Temperatura",F,"Graus Fahrenheit")
  print("Temperatura",format(C,'.2f'),"Graus Celsius")

# EXERCÍCIO 8
ano = int(input("Digite o ano: "))
if ano%4==0 and ano%100!=0 or ano%400==0:
  print(ano,"é ano bissexto")
else:
  print(ano,"NÃO é ano bissexto")

# EXERCÍCIO 9
sexo = str(input("Digite seu sexo: "))
idade = int(input("Digite sua idade: "))
t_cont = int(input("Digite seu tempo de contribuição: "))
if sexo == "M":
  if idade >= 65 and t_cont >= 10:
    print("Aposentável")
  elif idade >= 63 and t_cont >= 15:
    print("Aposentável")
  else:
    print("Não aposentável")
elif sexo == "F":
  if idade >= 63 and t_cont >= 10:
    print("Aposentável")
  elif idade >= 61 and t_cont >= 15:
    print("Aposentável")
  else:
    print("Não aposentável")

# EXERCÍCIO 10
a = int(input("Digite o primeiro número: "))
b = int(input("Digite o segundo número: "))
c = str(input("Digite o operador: "))
if c == "+":
  print("Resultado:",a+b)
elif c == "-":
  print("Resultado:",a-b)
elif c == "*":
  print("Resultado:",a*b)
elif c == "/":
  print("Resultado:",a/b)


