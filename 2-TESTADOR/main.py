# -*- coding: utf-8 -*-

# Script para testar tarefas de laboratÃ³rio de MC102 em ambiente GNU/Linux.

# Uso: python3 executa-testes.py lab<x>.py

# O programa lab<x>.py serÃ¡ testado com todos os arquivos arq<i>.in
# encontrados no diretÃ³rio corrente. Os testes serÃ£o iniciados com i
# igual a 1 e serÃ£o interrompidos quando arq<i>.in nÃ£o for encontrado.

# As saÃ­das serÃ£o comparadas com os arquivos arquivos arq<i>.res. 

# Durante o processamento serÃ£o criados e posteriormente removidos
# arquivos arq<i>.out e arq<i>.diff. 

import os
import sys

#if len(sys.argv) < 2 :
#    print("Uso: python3 executa-testes.py labXX.py")
#    sys.exit()

print("1 - Executar todos os testes")
print("2 - Executar apenas o arquivo lab.py")
whichfile = input("Escolha sua opÃ§Ã£o: ")

if whichfile == '2':
  os.system("python3 lab.py")
else:
  labfile = "lab.py"
  if not os.path.exists(labfile) :
      print("Arquivo", labfile, "nÃ£o encontrado.")
      sys.exit()
      
  i = 1
  testfile = "arq" + str(i) +".in"

  while (os.path.exists(testfile)) :
      resfile = "arq" + str(i) +".res"
      if not os.path.exists(resfile) :
        print("Arquivo", resfile, "nÃ£o encontrado.")
        sys.exit()
        
      outfile = "arq" + str(i) +".out"
      if (os.path.exists(outfile)) :
        answer = input("Arquivo " + outfile + " existente. Pode ser sobrescrito (S/n) ?")
        if answer == "n" or answer == "N" :
          sys.exit()
          
      difffile = "arq" + str(i) +".diff"
      if (os.path.exists(difffile)) :
        answer = input("Arquivo " + difffile + " existente. Pode ser sobrescrito (S/n) ?")
        if answer == "n" or answer == "N" :
          sys.exit()
          
      os.system("python3 " + labfile + " < " + testfile + " > " + outfile)
      if os.system("diff " + outfile + " " + resfile + " > " + difffile) == 0 :
        print("Teste ", str(i), ": resultado correto")
      else: 
        print("Teste ", str(i), ": resultado incorreto")
        os.system("cat " + difffile)
      os.remove(outfile)      
      os.remove(difffile)
      i += 1
      testfile = "arq" + str(i) +".in"