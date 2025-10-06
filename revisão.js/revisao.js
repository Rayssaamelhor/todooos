// 1)
const nome = "Rayssa Milena Correia Fagundes";
let numeroChamada = 23

// 2)
const jogos = ["FIFA 23", "Among Us", "Minecraft"];

// 3)
console.log("### exercicio 3 ###")
let i = 0;
console.log("Jogos favoritos de " + nome + " são:");
while (i < jogos.length) {
    console.log(jogos[i]);
    i++;
}
// 4)
const serieFavorito = {
    nome: nome, 
    nomeserie: "South Park",
    anoLancamento:1997 ,
    notaIMDb:8.7
};

//console.log(serieFavorito);

// 5) 
console.log("### exercicio5 ###")
if (serieFavorito.notaIMDb <= 4.0) {
    console.log("O filme possui uma nota considerada baixa.");
} else if (serieFavorito.notaIMDb > 4.0 && serieFavorito.notaIMDb <= 7.0) {
    console.log("O filme é considerado razoável.");
} else {
    console.log("O filme é muito bom!");
}

// 6)
console.log("### exercicio6 ###")
function verificaChuva(previsaoTempo) {
    console.log("Clima para essa semana:");
    for (let i = 0; i < previsaoTempo.length; i++) {
        const dia = previsaoTempo[i];
        if (dia.chanceDeChuva > 50) {
            console.log(`${dia.dia}: levar guarda-chuva`);
        } else {
            console.log(`${dia.dia}: tempo agradável`);
        }
    }
}
const previsaoTempo = [
    {
        dia: "segunda",
        temperaturaMin: 14,
        temperaturaMax: 19,
        chanceDeChuva: 10
    },
    {
        dia: "terça",
        temperaturaMin: 13,
        temperaturaMax: 20,
        chanceDeChuva: 10
    },
    {
        dia: "quarta",
        temperaturaMin: 15,
        temperaturaMax: 22,
        chanceDeChuva: 80
    },
    {
        dia: "quinta",
        temperaturaMin: 13,
        temperaturaMax: 18,
        chanceDeChuva: 60
    },
    {
        dia: "sexta",
        temperaturaMin: 12,
        temperaturaMax: 16,
        chanceDeChuva: 40
    }
]

verificaChuva(previsaoTempo);

