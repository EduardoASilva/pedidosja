function adicionar(){
    const info = document.querySelectorAll('.informacoes')[0].children
    $('#addItem').empty();

    for (item of info) {
        if (item.className === 'nome'){
            document.getElementById('nomeCliente').value = item.children[0].value
        }
        if (item.className === 'sabor'){
            let forName = item.children[0].value
            let valueProd = item.children[2].value
            let html =
                `<div class="produto-pedidos">
                    <label for="${forName}" class="" >${forName.toUpperCase()}</label>
                    <input id="${forName}" name="${forName}" class="" value="${valueProd}">
                </div>`

            let elementHtml = document.getElementById('addItem')
            elementHtml.innerHTML += html
        }
    }
}

function somar(opcao){
    let valueInput = document.getElementById(`${opcao}`)

    let valueReal = parseInt(valueInput.value)
    valueInput.value = valueReal + 1
}

function subtrair(opcao) {
    let valueInput = document.getElementById(`${opcao}`)

    if (valueInput.value !== '0'){
        let valueReal = parseInt(valueInput.value)
        valueInput.value = valueReal - 1
    }
}

function editar(id_pedido) {
    let input = document.querySelectorAll(`.produto-pedidos${id_pedido}`)[0].children

    for (item of input) {
        if (item.localName === 'input') {
            item.removeAttribute('disabled')
        }
    }
    let buttonEditar = document.getElementById(`buttonEditar${id_pedido}`)
    buttonEditar.style.display = `none`;
    let buttonSalvar = document.getElementById(`buttonSalvar${id_pedido}`)
    buttonSalvar.style.display = 'block';
}