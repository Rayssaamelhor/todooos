palavras = []
arquivo = open("comidas.txt", "r")
for linha in arquivo:
     palavras.append(linha.strip())

  print(palavras)