function definir_par(numero){
    let resultado
    if (numero % 2 == 0){
        resultado = "esse numero é par"
    }
    else{
        resultado = "esse numero é impar"
    }
    return resultado
}

console.log(definir_par(8))
console.log(definir_par(7))

function somar_numero(num1,num2){
    let res = num1 + num2
    return res
}

function sub_numero(num1,num2){
    let res = num1 - num2
    return res
}

function mult_numero(num1,num2){
    let res = num1 * num2
    return res
}

function div_numero(num1,num2){
    let res = num1 / num2
    return res
}


function calcular(a,b){
    let somar = a+b
    let sub = a-b
    let mult = a*b
    let div = a/b
    let calculos = [somar,sub,mult,div]
    return calculos
}

let num1 = Number(prompt("Digite um numero"))
let num2 = Number(prompt("Digite outro numero"))

console.log(calcular(num1,num2))