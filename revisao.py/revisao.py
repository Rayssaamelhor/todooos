#1
nome = "Rayssa Milena Correia Fagundes" 
numero_chamada = 23
#2
print("Olá, seja bem-vindo(a) ao sistema! sistema criado por",nome,",N chamada:",numero_chamada)
#3
altura_usuario = 1.65 
musica_favorita = "so menina linda"  
filme_favorito = "Breaking Bad"  
nota_imdb_favorito = 9.5

# 4) 
altura_input = float(input("Por favor, digite sua altura em metros: "))
if altura_input > altura_usuario:
    print("Você é maior que eu.")
elif altura_input < altura_usuario:
    print("Você é menor que eu.")
else:
    print("Você tem a mesma altura que eu.")

# 5) 
musicas_usuario = []
contador = 0

while contador < 3:
    musica = input("Digite uma música que você gosta: ")
    musicas_usuario.append(musica)
    contador += 1
if musica_favorita in musicas_usuario:
    print("Você gosta da minha música favorita!")
else:
    print("Você não gosta da minha música favorita.")

# 6) 
filmes = []
notas = []

for i in range(3):
    filme = input("Digite o nome de um filme que você gosta: ")
    nota = float(input(f"Qual a nota do filme {filme} no IMDb? "))
    filmes.append(filme)
    notas.append(nota)

for i in range(len(filmes)):
    if notas[i] > nota_imdb_favorito:
        print(f"O filme '{filmes[i]}' tem uma nota maior que o meu filme favorito.")
    elif notas[i] < nota_imdb_favorito:
        print(f"O filme '{filmes[i]}' tem uma nota menor que o meu filme favorito.")
    else:
        print(f"O filme '{filmes[i]}' tem a mesma nota que o meu filme favorito.")
