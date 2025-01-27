const numero1 = document.querySelector('#n1')
const numero2 = document.querySelector('#n2')
const result = document.querySelector('#result')
const result2 = document.querySelector('#resultado2')
function somar(){
    let valor_numero1 = Number(numero1.value)
    let valor_numero2 = Number(numero2.value)
    let soma = valor_numero1 + valor_numero2
    result.innerHTML += soma
    result2.value = soma
}

