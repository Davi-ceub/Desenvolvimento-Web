function calcular_media(nota1,nota2,nota3){
    return (nota1 + nota2 + nota3)/3;
}

const checar_aprovacao = nota => {
    if (nota >= 7) {
        return "Aprovado";
    }else{
        return "Reprovado";
    }
};

let media = calcular_media(5,7,9);
console.log(media, checar_aprovacao(media));