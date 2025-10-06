 const listaNumeros = [20, 50, 100, 10, 30];
 const listaStrings = ["maça", "amora", "morango", "melancia"];
 
 //ordenando uma lista:
 const frutasOrdenadas = listaStrings.sort();
 console.log(listaStrings)
 console.log(frutasOrdenadas)
 const numOrdenado = listaNumeros.sort((a,b) => {
     if (a < b){
        return -1;
     }
    if (a > b){
        return 1
    }
    return 0

 });
 console.log(numOrdenado)

 const celulares = [
    {nome: " Apple iphone 11", preco: 2500,qualidade: "vitrine"},
    {nome: "Motorola G53", preco: 1500, qualidade: "novo"},
    {nome: "samsung S23", preco: 2000, qualidade: "bom"},
    {nome: "Apple iphone 11",preco: 2300,qualidade: "marcas de uso"},
 ]
