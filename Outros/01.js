////////////////////////// Questao 1 //////////////////////////

let INDICE = 13;
let SOMA = 0;
let K = 0;

while (K < INDICE) {
    K = K + 1;
    SOMA = SOMA + K;
}

console.log(SOMA); // Resultado: 91


////////////////////////// Questao 2 //////////////////////////

function isFibonacci(num) {
    let a = 0, b = 1;
    while (b < num) {
        [a, b] = [b, a + b];
    }
    return b === num;
}

const numero = parseInt(prompt("Informe um número:"));
if (isFibonacci(numero)) {
    console.log(`O número ${numero} pertence à sequência de Fibonacci.`);
} else {
    console.log(`O número ${numero} não pertence à sequência de Fibonacci.`);
}

////////////////////////// Questao 3 //////////////////////////

// Exemplo de dados de faturamento (substitua por um JSON real)
const faturamento = [1000, 0, 2000, 1500, 0, 3000, 2500, 0, 4000, 3500, 0, 5000];

// Filtrando dias sem faturamento (valores 0)
const faturamentoFiltrado = faturamento.filter(valor => valor > 0);

// Calculando o menor e o maior valor de faturamento
const menor = Math.min(...faturamentoFiltrado);
const maior = Math.max(...faturamentoFiltrado);

// Calculando a média mensal
const media = faturamentoFiltrado.reduce((acc, valor) => acc + valor, 0) / faturamentoFiltrado.length;

// Contando os dias em que o faturamento foi superior à média
const diasAcimaMedia = faturamentoFiltrado.filter(valor => valor > media).length;

console.log(`Menor valor de faturamento: ${menor}`);
console.log(`Maior valor de faturamento: ${maior}`);
console.log(`Número de dias com faturamento acima da média: ${diasAcimaMedia}`);

////////////////////////// Questao 4 //////////////////////////

const faturamento = {
    SP: 67836.43,
    RJ: 36678.66,
    MG: 29229.88,
    ES: 27165.48,
    Outros: 19849.53
};

const total = Object.values(faturamento).reduce((acc, valor) => acc + valor, 0);

for (const [estado, valor] of Object.entries(faturamento)) {
    const percentual = (valor / total) * 100;
    console.log(`${estado}: ${percentual.toFixed(2)}%`);
}

////////////////////////// Questao 5 //////////////////////////

function inverterString(str) {
    let invertida = '';
    for (let i = str.length - 1; i >= 0; i--) {
        invertida += str[i];
    }
    return invertida;
}

const string = prompt("Informe uma string:");
console.log(`String invertida: ${inverterString(string)}`);