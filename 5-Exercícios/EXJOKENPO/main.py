P1 = str(input())
P2 = str(input())

if P1 == "pedra" and P2 == "pedra":
  print("Empate")
elif P1 == "pedra" and P2 == "papel":
  print("P2 é o vencedor")
elif P1 == "pedra" and P2 == "tesoura":
  print("P1 é o vencedor")
elif P1 == "papel" and P2 == "papel":
  print("Empate")
elif P1 == "papel" and P2 == "pedra":
  print("P1 é o vencedor")
elif P1 == "papel" and P2 == "tesoura":
  print("P2 é o vencedor")
elif P1 == "tesoura" and P2 == "tesoura":
  print("Empate")
elif P1 == "tesoura" and P2 == "pedra":
  print("P2 é o vencedor")
elif P1 == "tesoura" and P2 == "papel":
  print("P1 é o vencedor")