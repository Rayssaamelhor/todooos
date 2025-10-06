
#1
nome = "Rayssa Milena Correia Fagundes" 
numero_chamada = 23
#2
print("Olá, seja bem-vindo(a) ao sistema! sistema criado por",nome,",N chamada:",numero_chamada)

# 3) Definição das variáveis
altura = 1.75  # Substitua pela sua altura em metros
musica_favorita = "Nome da Música"  # Substitua pelo nome da sua música favorita
filme_favorito = "Nome do Filme"  # Substitua pelo nome do seu filme favorito
nota_filme_favorito = 8.5  # Substitua pela nota do filme no IMDb

# 4) Pedindo a altura do usuário e comparando
altura_usuario = float(input("Digite sua altura em metros: "))

if altura_usuario > altura:
    print("Você é mais alto(a) que eu!")
elif altura_usuario < altura:
    print("Você é mais baixo(a) que eu!")
else:
    print("Temos a mesma altura!")

# 5) Pedindo ao usuário três músicas favoritas e verificando se ele gosta da sua música favorita
musicas_usuario = []
contador = 0

while contador < 3:
    musica = input(f"Digite a música favorita {contador + 1}: ")
    musicas_usuario.append(musica)
    contador += 1

if musica_favorita in musicas_usuario:
    print("Você também gosta da minha música favorita!")
else:
    print("Parece que temos gostos musicais diferentes.")

# 6) Pedindo ao usuário três filmes e suas notas no IMDb
filmes_usuario = []
notas_usuario = []

for i in range(3):
    filme = input(f"Digite o nome do filme {i + 1}: ")
    nota = float(input(f"Digite a nota do filme {i + 1} no IMDb: "))
    filmes_usuario.append(filme)
    notas_usuario.append(nota)

# Comparando os filmes do usuário com o filme favorito
for i in range(3):
    if notas_usuario[i] > nota_filme_favorito:
        print(f"O filme {filmes_usuario[i]} tem uma nota maior que {filme_favorito}.")
    elif notas_usuario[i] < nota_filme_favorito:
        print(f"O filme {filmes_usuario[i]} tem uma nota menor que {filme_favorito}.")
    else:
        print(f"O filme {filmes_usuario[i]} tem a mesma nota que {filme_favorito}.")
