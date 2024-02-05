# ENTRADAS
tipo_do_objeto = str(input())
caractere = str(input())

# QUADRADO
if tipo_do_objeto == "Q":
  medida_do_lado = int(input())
  if medida_do_lado < 3:
    print("Dimensao invalida.") 
  else:
    for i in range(medida_do_lado):
      for j in range(medida_do_lado):
        if i != 0 and i != medida_do_lado-1:
          if j != 0 and j != medida_do_lado-1:
            print(" ",end="")
          else:
            print(caractere, end="")      
        else:
          print(caractere, end="")
      print() 

# RETÂNGULO
elif tipo_do_objeto == "R":
  medida_da_largura = int(input())
  medida_da_altura = int(input())
  if medida_da_largura < 3 or medida_da_altura < 3:
    print("Dimensao invalida.")
  else:
    for i in range(medida_da_altura):
      for j in range(medida_da_largura):
        if i != 0 and i != medida_da_altura-1:
          if j != 0 and j != medida_da_largura-1:
            print(" ",end="")
          else:
            print(caractere, end="")      
        else:
          print(caractere, end="")
      print() 

# TRIÂNGULO RETÂNGULO
elif tipo_do_objeto == "TR":  
  medida_da_altura = int(input())
  if medida_da_altura < 3:
    print("Dimensao invalida.")
  else:
    for i in range(medida_da_altura):
      for j in range(i+1):
        if i == medida_da_altura-1:
          print(caractere, end="")
        elif j == 0 or j == i:
          print(caractere, end="")
        else:
          print(" ", end="")
      print()

# TRIÂNGULO ISÓSCELES
elif tipo_do_objeto == "TI":  
  medida_da_altura = int(input())
  base = 2 * medida_da_altura - 1  
  if medida_da_altura < 3:
    print("Dimensao invalida.")
  else:
    print((medida_da_altura-1)*" ", end="")
    print(caractere)    
    for i in range(1,medida_da_altura-1):
      print((medida_da_altura-i-1)*" ", end="")
      print(caractere, end="")
      print((2*i-1)*" ", end="")
      print(caractere)
    print(base*caractere)

# HEXÁGONO
elif tipo_do_objeto == "H":  
  medida_do_lado = int(input())  
  if medida_do_lado < 3:
    print("Dimensao invalida.")
  else:  
    for i in range(-(medida_do_lado-1), medida_do_lado):  
      if i == (-(medida_do_lado-1)) or i == (medida_do_lado-1):
        print(" "*(medida_do_lado-1), end="")
        print(medida_do_lado*caractere)
      else:
        print(abs(i)*" ", end="")
        print(caractere, end="")
        print((medida_do_lado+2*(medida_do_lado-2-abs(i)))*" ", end="")
        print(caractere)      

# QUADRICULADO
elif tipo_do_objeto == "QQ":    
  medida_do_lado = int(input())
  medida_da_largura = int(input())
  medida_da_altura = int(input())
  if medida_da_largura < 1 or medida_da_altura < 1:
    print("Dimensao invalida.")
  else:
    for i in range(medida_do_lado*medida_da_altura-medida_da_altura+1):
      for j in range(medida_do_lado*medida_da_largura-medida_da_largura+1):
        if not ((i + medida_do_lado-1) % (medida_do_lado-1)):
          print(caractere, end="")
        elif not ((j + medida_do_lado-1) % (medida_do_lado-1)):
          print(caractere, end="")
        else:
          print(" ", end="")        
      print() 

#XADREZ
elif tipo_do_objeto == "X":
  medida_do_lado = int(input())
  medida_da_largura = int(input())
  medida_da_altura = int(input())
  if medida_da_largura < 1 or medida_da_altura < 1:
    print("Dimensao invalida.")
  else:
    for i in range(medida_do_lado*medida_da_altura-medida_da_altura+1):
      if i == 0 or i%(medida_do_lado-1) == 0:              
        print(caractere*(medida_do_lado*medida_da_largura-medida_da_largura+1))
      else:
        for j in range(medida_da_largura):
          if ((i+medida_do_lado-1)//(medida_do_lado-1))%2 == 0:
            if j%2 == 0:
              print(caractere*(medida_do_lado-1), end="")   
            else:
              print(caractere, end="")
              print(" "*(medida_do_lado-2), end="")
          else:
            if j%2 == 0:
              print(caractere, end="")
              print(" "*(medida_do_lado-2), end="")
            else:
              print(caractere*(medida_do_lado-1), end="")
        print(caractere)          

else:
  print("Identificador invalido.")