# EXERCÍCIO 1
'''a = [input("Digite uma string: ")]
a = a.reverse()
print(a)
# EXERCÍCIO 2
a = input("Digite uma string: ")
a = a.replace(" ","")
print(a)
a = 1
while a <= 11:
  if a % 3 == 0:
    print(a)
  a = a+1
'''

n = int(input())
for i in range(n+2):
  for j in range(n-i+2):
    if i == 0:
      print(j,end="")
    elif i == 1:
      print(n-j+1,end="")
    else:
      print(n-j,end="")
  print()