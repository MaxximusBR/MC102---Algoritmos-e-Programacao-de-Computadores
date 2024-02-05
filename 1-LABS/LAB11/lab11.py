# IMPORTAR CSV E ABRIR ARQUIVO CSV
import csv
dados = csv.reader(open("dados.csv"))

# ENTRADAS
A = int(input())
B = int(input())

# REPETIÇÃO
for linha in dados:
  temp = float(linha[0])
  pressao_m = float(linha[1])
  pressao_e = float(linha[2])  
  delta_pressao = pressao_m - pressao_e
  ln_pressao_e = float(linha[3])
  A_B_temp = A + B/temp
  delta_ln_temp = A_B_temp - ln_pressao_e
  print('"',format(temp,'.2f'),'",','"',format(pressao_m,'.2f'),'",','"',format(pressao_e,'.2f'),'",','"',format(delta_pressao,'.2f'),'",','"',format(ln_pressao_e,'.2f'),'",','"',format(A_B_temp,'.2f'),'",','"',format(delta_ln_temp,'.2f'),'"',sep="")