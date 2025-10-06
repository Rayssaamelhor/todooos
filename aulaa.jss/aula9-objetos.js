let livros = require("./livros.json")
function mostraLivros(){
    livros.forEach((Livro) => {
        console.log(Livro.titulo + "_" +
                    Livro.autor + "ano:" +
                    Livro.ano + "páginas:" +
                    Livro.páginas + "preço: R$ " +
                    Livro.preco)
                    
    })

}
function adicionalivro(titulo,autor,editora,ano,sinopse,paginas,genero,preco){
      livros.push({
        titulo: titulo,
        autor: autor,
        editora: editora,
        ano: ano,
        sinopse: sinopse,
        paginas: paginas,
        genero: genero,
        preco: preco
    });
     console.log("livro adicionado com sucesso!");
}

adicionalivro("A Paciente Silenciosa","Alex Michaelides","Record",2019,
     "Uma mulher assassinou o marido e nunca mais falou",336,["Mistério","Thriller Psicológico"],39.99);
// JSON = JavaScript Object Notation
// GERA UM ARQUIVO JSON DOS LIVROS
function criarArquivo() {
    let livrosTexto = JSON.stringify(livros);
    const fs = require ('fs');
    fs.writeFileSync("livros.json", livrosTexto);
}

//criarArquivo()
mostraLivros();