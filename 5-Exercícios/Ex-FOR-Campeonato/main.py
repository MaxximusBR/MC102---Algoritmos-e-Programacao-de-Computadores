def pontuacao (nome_time,campeonato):
  pontos = 0
  for i in range(campeonato):
    for j in range(campeonato[0]):
      if nome_time == j:
        if j.isdigit  == True:
          if j+1 == j+3 or j+1 == j-1:
            pontos += 1
          elif j+1 > j+3 or j+1 > j-1:
            pontos += 2
          else:
            pontos += 0
  return pontos

camp = [["Havai",0,"Palmeiras",0],["Palmeiras",1,"Corinthians",0],["São Paulo",2,"Palmeiras",1],["Goiás",1,"Bahia",2]]
pontuacao_Palmeiras = pontuacao("Palmeiras",camp)
print(pontuacao_Palmeiras)