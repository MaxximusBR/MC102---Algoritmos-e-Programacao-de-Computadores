# SOLUÇÃO 1
'''txt = input("Digite uma frase: ")
txt = txt.lower()
txt = txt.replace(" ","")
i = 0
j = len(txt)-1
palindromo = True
while i < j:
  if txt[i] == txt[j]:
    i = i + 1
    j = j - 1
  else:
    palindromo = False
    break
if palindromo:
  print("É um palíndromo!")
else:
  print("Não é um palíndromo!")

# SOLUÇÃO 2
txt = input("Digite uma frase: ")
txt = txt.lower()
txt = txt.replace(" ","")
i = 0
j = len(txt)-1
palindromo = True
while i < j:
    if txt[i] != txt [j]:
      palindromo = False
    i = i + 1
    j = j -1
if palindromo:
  print("É um palíndromo!")
else:
  print("Não é um palíndromo!")'''

# SOLUÇÃO 3
txt = input("Digite uma frase: ")
txt = txt.lower()
txt = txt.replace(" ","")
if txt == txt [::-1]:
  print("É um palíndromo!")
else:
  print("Não é um palíndromo!")
