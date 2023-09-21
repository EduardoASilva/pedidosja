function adicionar(){
    const info = document.querySelectorAll('.informacoes')[0].children

    for (item of info) {
        if (item.className === 'nome'){
            let nome = item.children[0].value
            document.getElementById('nomeCliente').innerText = nome
        }
        if (item.className === 'sabor'){
            if (item.children[2].value !== '0'){
                let forName = item.children[0].value
                let valueProd = item.children[2].value
                let html =
                    `<label for="${forName}" class="" >${forName.toUpperCase()}</label>
                    <input id="${forName}" name="${forName}" class="" value="${valueProd}">`

                let elementHtml = document.getElementById('addItem')
                elementHtml.innerHTML += html
            }
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
