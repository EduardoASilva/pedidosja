function finalizar(){

    const comprador = document.getElementById("nome");
    const produto = document.getElementById("produto");
    const quantidade = document.getElementById("quantidade");
    const carne = document.getElementById("carne");
    const qcarne = document.getElementById("quantidadecarne");
    const acai = document.getElementById("acai");
    const qacai = document.getElementById("quantidadeacai");


    const value = comprador.value;
    const qtd = quantidade.value;
    const item = produto.value;
    const item1 = carne.value;
    const qitem1 = quantidadecarne.value;
    const item2 = acai.value;
    const qitem2 = quantidadeacai.value;




    document.getElementById("comprador").innerHTML = value;
    document.getElementById("sabores").innerHTML = item;
    document.getElementById("numero").innerHTML = qtd;
    document.getElementById("scarne").innerHTML = item1;
    document.getElementById("qtdcarne").innerHTML = qitem1;
    document.getElementById("sacai").innerHTML = item2;
    document.getElementById("qtdacai").innerHTML = qitem2;

}

function process_geral(quant){
    var classValue = parseInt(document.querySelector('.quanti').value);
    classValue+=quant;
    //console.log(classValue);
    if(classValue < 1){
        document.querySelector("input.quanti").value = 0;
    }else{
        document.querySelector("input.quanti").value = classValue;
    }
}

function process_geral(quantcarne){
    var classValue = parseInt(document.querySelector('.quanticarne').value);
    classValue+=quant;
    //console.log(classValue);
    if(classValue < 1){
        document.querySelector("input.quanticarne").value = 0;
    }else{
        document.querySelector("input.quanticarne").value = classValue;
    }
}

function somar(opcao){

}

function subtrair(opcao) {
    // let ops = opcao
    let valueInput = document.getElementById(`#${opcao}`)

    if (!valueInput.value === '0'){
        let valueReal = parseInt(valueInput.value)
        valueInput.value = valueReal - 1
    }


}
