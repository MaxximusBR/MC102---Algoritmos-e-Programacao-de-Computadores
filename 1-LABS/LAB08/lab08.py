# ENTRADAS
texto = input()
pontuacao = [",",".","...",":","(",")","!","?","-"]
vocabulario = {}

# PONTUAÇÃO
while not texto.startswith("---"):
  for p in pontuacao:
    if p == "-":
      texto = texto.replace(p," ")
    else:
      texto = texto.replace(p,"")
  # Vocabulario
  texto = texto.lower()
  texto = texto.split()  
  for palavra in texto:
    if palavra in vocabulario:
      vocabulario[palavra] = vocabulario[palavra] + 1
    else:
      vocabulario[palavra] = 1
  texto = str(input())

# IMPRESSÃO
print("Vocabulario:")
for (chave,valor) in sorted(vocabulario.items()):
  print(chave,valor,sep=" (",end=")")
  print()

# SUGESTÕES
print("Sugestoes:")
sugestao = input()
sugestao = sugestao.lower()
lista_sug = []
while not sugestao.startswith("---"):
  for palavra in vocabulario:
    if palavra.startswith(sugestao) and palavra != sugestao:
      lista_sug.append(palavra)
      lista_sug.sort()            
  print(sugestao,end=":")
  for elemento in lista_sug:
    if elemento == lista_sug[-1]:
      print(" "+elemento,end="")
    else:
      print(" "+elemento,end="")    
  print()
  sugestao = input()
  sugestao = sugestao.lower()
  lista_sug = []