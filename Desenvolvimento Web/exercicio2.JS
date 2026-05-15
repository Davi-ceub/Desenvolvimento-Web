const nomes = [" João ", " maria ", " Carlos ", " ana "];

// Usando map para remover espaços e transformar em maiúsculas
const nomesLimpos = nomes.map(nome => nome.trim().toUpperCase());

console.log(nomesLimpos);


// Exercicio 2
let numeros = [150.00, 45.50, 200.00, 10.99, 500.00];

let resposta = numeros.filter(n => n > 100.00);

console.log(resposta);

// Exercicio 3
clientes =  [{nome: "Ana", email:"ana@gmail.com"}, {nome: "Beto", email: ""}]
clientes.forEach(element => {
    console.log("Enviando e-mail para " + element.nome + " no endereço " + element.email)    
});

// Exercicio 4
frutas = ["maça", "banana", "manga", "uva", "abacaxi"];
frutas_filtradas = frutas.filter(f => f.includes('n'));
console.log(frutas_filtradas)