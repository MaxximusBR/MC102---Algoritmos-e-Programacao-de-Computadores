# ENTRADAS
peso = float(input())
idade = int(input())
if 16 < idade < 18:     
  documento_de_autorizacao = str(input())
boa_saude = str(input())
uso_drogas_injetaveis = str(input())
primeira_doacao = str(input())
if primeira_doacao == "N": 
  meses_desde_ultima_doacao = int(input())
  doacoes_ultimos_12_meses = int(input())
sexo_biologico = str(input())
if sexo_biologico == "F":
  gravidez = str(input())
  amamentando = str(input())
  if amamentando == "S":
    meses_bebe = int(input())

# FLAG
flag = True

# SAÍDAS PRIMEIRA PARTE
print("Peso:",peso)
print("Idade:",idade)
if 16 < idade < 18:
  print("Documento de autorizacao:",documento_de_autorizacao)
print("Boa saude:",boa_saude)
print("Uso drogas injetaveis:",uso_drogas_injetaveis)
print("Primeira doacao:",primeira_doacao)
if primeira_doacao == "N":
  print("Meses desde ultima doacao:",meses_desde_ultima_doacao)
  print("Doacoes nos ultimos 12 meses:",doacoes_ultimos_12_meses)
print("Sexo biologico:",sexo_biologico)
if sexo_biologico == "F":
  print("Gravidez:",gravidez)
  print("Amamentando:",amamentando)
  if amamentando == "S":
    print("Meses bebe:", meses_bebe)

# SAÍDAS SEGUNDA PARTE
if peso < 50:
  print("Impedimento: abaixo do peso minimo.")
  flag = False
if idade < 16:
  print("Impedimento: menor de 16 anos.")
  flag = False
elif 16 <= idade < 18 and documento_de_autorizacao == "N":
  print("Impedimento: menor de 18 anos, sem consentimento dos responsaveis.")
  flag = False
elif idade > 60 and primeira_doacao == "S":
  print("Impedimento: maior de 60 anos, primeira doacao.")
  flag = False
elif idade > 69:
  print("Impedimento: maior de 69 anos.")
  flag = False
if boa_saude == "N":
  print("Impedimento: nao esta em boa saude.")
  flag = False
if uso_drogas_injetaveis == "S":
  print("Impedimento: uso de drogas injetaveis.")
  flag = False
if sexo_biologico == "M" and primeira_doacao == "N":
  if meses_desde_ultima_doacao < 2:
    print("Impedimento: intervalo minimo entre as doacoes nao foi respeitado.")
    flag = False
  if doacoes_ultimos_12_meses >= 4:
    print("Impedimento: numero maximo de doacoes anuais foi atingido.")
    flag = False
if sexo_biologico == "F" and primeira_doacao == "N":
  if meses_desde_ultima_doacao < 3 :
    print("Impedimento: intervalo minimo entre as doacoes nao foi respeitado.")
    flag = False
  if doacoes_ultimos_12_meses >= 3:
    print("Impedimento: numero maximo de doacoes anuais foi atingido.")
    flag = False
if sexo_biologico == "F":
  if gravidez == "S":
    print("Impedimento: gravidez.")
    flag = False
  if amamentando == "S" and meses_bebe < 12:
    print("Impedimento: amamentacao.")
    flag = False
if flag:
  print("Procure um hemocentro para triagem completa.")