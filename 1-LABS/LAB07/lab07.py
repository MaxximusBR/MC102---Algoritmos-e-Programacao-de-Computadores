# ENTRADAS
notas_ac = [float(x) for x in input().split()]
def tupla_float_int(x) :
  x = x[1:-1]      
  x = x.split(",") 
  f = float(x[0])
  i = int(x[1])
  return (f,i)
notas_lab = [tupla_float_int(x) for x in input().split()]
prova1, teste, prova2 = map(float,input().split())
freq = float(input())

# SOMAS
soma_notas_ac = 0
soma_notas_lab = 0
soma_pesos = 0
soma_notas_ae = 0

# REPETIÇÃO
for i in notas_ac:
  soma_notas_ac = soma_notas_ac + float(i)
for notas in notas_lab:
  mult_notas_lab = notas[0]*notas[1]
  soma_pesos = soma_pesos + notas[1]
  soma_notas_lab = soma_notas_lab + mult_notas_lab
p1_teste_p2 = prova1*2 + teste*1 + prova2*4

# MÉDIAS
MAC = soma_notas_ac / len(notas_ac)
ML = soma_notas_lab/soma_pesos
MP = p1_teste_p2/7

# CONDIÇÕES
if freq >= 75:
  if MP >= 5 and ML >= 5:
    Mfinal = 	max(5.0, 0.6 * MP + 0.3 * ML + 0.1 * MAC) 
    print("Media das atividades conceituais:",format(MAC,".1f"))
    print("Media das tarefas de laboratorio:",format(ML,".1f"))
    print("Media das avaliacoes escritas:",format(MP,".1f"))
    print("Frequencia: ",freq,"%",sep="")    
    print("Aprovado(a) por nota e frequencia.")
    print("Media final:",format(Mfinal,".1f"))
  elif MP >= 2.5 and ML >= 2.5:
    exame = float(input())
    MPreliminar = min(4.9, 0.6 * MP + 0.3 * ML + 0.1 * MAC)
    Mfinal = (MPreliminar + exame)/2
    if Mfinal >= 5.0:
      print("Media das atividades conceituais:",format(MAC,".1f"))
      print("Media das tarefas de laboratorio:",format(ML,".1f"))
      print("Media das avaliacoes escritas:",format(MP,".1f"))
      print("Frequencia: ",freq,"%",sep="")    
      print("Media preliminar:",format(MPreliminar,".1f"))
      print("Nota no exame:",exame)
      print("Aprovado(a) por nota e frequencia.")
      print("Media final:",format(Mfinal,".1f"))   
    else:
      print("Media das atividades conceituais:",format(MAC,".1f"))
      print("Media das tarefas de laboratorio:",format(ML,".1f"))
      print("Media das avaliacoes escritas:",format(MP,".1f"))
      print("Frequencia: ",freq,"%",sep="") 
      print("Media preliminar:",format(MPreliminar,".1f"))
      print("Nota no exame:",exame)    
      print("Reprovado(a) por nota.")
      print("Media final:",format(Mfinal,".1f"))
  elif MP < 2.5 or ML < 2.5:
    Mfinal = min(MP, ML)
    print("Media das atividades conceituais:",format(MAC,".1f"))
    print("Media das tarefas de laboratorio:",format(ML,".1f"))
    print("Media das avaliacoes escritas:",format(MP,".1f"))
    print("Frequencia: ",freq,"%",sep="") 
    print("Reprovado(a) por nota.")
    print("Media final:",format(Mfinal,".1f"))
elif freq < 75:
  Mfinal = min(MP, ML)
  print("Media das atividades conceituais:",format(MAC,".1f"))
  print("Media das tarefas de laboratorio:",format(ML,".1f"))
  print("Media das avaliacoes escritas:",format(MP,".1f"))
  print("Frequencia: ",freq,"%",sep="")  
  print("Reprovado(a) por frequencia.")
  print("Media final:",format(Mfinal,".1f"))