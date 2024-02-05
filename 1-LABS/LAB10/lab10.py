# FUNÇÃO ENTRADA
def funcao_entrada():
  id_pag = input() # ENTRADA ÍNDICE PÁGINA
  id_pag = id_pag.split() # DIVIDE ÍNDICE PÁGINA
  origem = {}
  destino = {}
  for a in id_pag:
    origem[a] = []
    destino[a] = []
  while True:    
    id_pag_link = input()  # ENTRADA LINKS
    if id_pag_link.isdigit(): 
      n = int(id_pag_link) # nº REPETIÇÔES
      break
    else:
      id_pag_link = id_pag_link.split() # DIVIDE ENTRADA LINKS
      id_pag_origem = id_pag_link[0]
      id_pag_destino = id_pag_link[2]      
      if not id_pag_destino in origem[id_pag_origem] and id_pag_origem != id_pag_destino:
        origem[id_pag_origem].append(id_pag_destino)    
      if not id_pag_origem in destino[id_pag_destino] and id_pag_origem != id_pag_destino:
        destino[id_pag_destino].append(id_pag_origem)
  return origem,destino,id_pag,n

# IMPRESSÃO ENTRADA
origem, destino, id_pag,n = funcao_entrada() 
for i in sorted(id_pag):
  if i in origem:
    print(i,"->",origem[i])
  else:
    print(i,"->","[]")
  if i in destino:
    print(destino[i],"->",i)
  else:
    print("[]","->",i)

# PAGE RANK
PR = {}
PR_futuro = {}
d = 0.875
constante = (1-d)/len(id_pag)
print("PageRank (passo 0)")
for i in sorted(id_pag):
  PR[i] = 1/(len(id_pag))  
  print(i+":",format(PR[i],'.3f'))
for j in range(n):
  print("PageRank (passo",j+1,end=")\n")
  for k in sorted(id_pag):
    soma = 0
    for l in destino[k]:
      soma+= PR[l]/len(origem[l])
    soma = soma * d
    PR_futuro[k] = soma + constante 
    print(k+":",format(PR_futuro[k],'.3f'))
  for chave in PR:
    PR[chave] = PR_futuro[chave]