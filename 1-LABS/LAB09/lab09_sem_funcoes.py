# ENTRADAS
diagrama_entrada = [] # MATRIZ
dicionario = {}
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

diagrama_saida = [["." for x in range(len(diagrama_entrada[0]))] for y in range(len(diagrama_entrada))]

# CAÇA-PALAVRAS

for m in range(n):
  palavra = input()
  palavras.append(palavra)

for palavra in palavras:  
  for i in range(len(diagrama_entrada)):
    for j in range(len(diagrama_entrada[0])):
      k = j      
      letras1 = []    
      for p in palavra:            
        if p == diagrama_entrada[i][k]:
          if k == (len(diagrama_entrada[0]) - 1):
            break
          else:
            k = k + 1
            letras1.append(p)
      if palavra == ("".join(letras1)):
        k = j
        for p in palavra:        
          diagrama_saida[i][k] = p
          k = k + 1
  for i in range(len(diagrama_entrada)):
      for j in range(len(diagrama_entrada[0])):
        print(diagrama_saida[i][j],end="")
      print()
  