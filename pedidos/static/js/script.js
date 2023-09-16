function finalizar(){

    const comprador = document.getElementById("nome");
    const produto = document.getElementById("produto");
    const quantidade = document.getElementById("quantidade");


    
    const value = comprador.value;
    const qtd = quantidade.value;
    const item = produto.value;

    document.getElementById("comprador").innerHTML = value;
    document.getElementById("sabores").innerHTML = item;
    document.getElementById("numero").innerHTML = qtd;

    


}