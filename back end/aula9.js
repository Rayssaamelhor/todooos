//1)
let numero =3;
for(let c = 1; c<11; c++){
    resultado = numero * c ;
    console.log(numero + "x"+ c+"="+resultado);
}
// 2)
let idades = [10,35,15,20,27,17,18,54,65,12];
let maiores =0
for(let a = 0; a<10; a++){
    // console.log(idades[a]);
    if (idades[a]>=18){
        maiores++;
    }
} 
let porc = maiores/idades.length*100
console.log(porc+"%");

//3) 
let tamanho_quadrado = 3; 
let linha = ""
for (let b =0 ;b< tamanho_quadrado; b++){
     linha=linha+"#"
}
for (let b=0;b< tamanho_quadrado; b++){
    console.log(linha);
}

//4)
let tamanho_tri =10;
let linha_tri=""
for (let b =0;b<= tamanho_tri; b++){
   for(let d=1; d<=b;d++){
    linha_tri=linha_tri+"# "
   }
       linha_tri=linha_tri+"\n"
}
console.log(linha_tri)