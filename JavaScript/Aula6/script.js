const numero = document.querySelector("#nmb")
const botao = document.querySelector("#botao")
const resultado = document.querySelector("#resultado")
let resulpnn;
botao.addEventListener("click",()=>{
    let valor_numero = numero.value

    if (valor_numero > 0){
        resulpnn = "Positivo"
    }
    else if(valor_numero < 0){
        resulpnn = "Negativo"
    }
    else{
        resulpnn = "Nulo"
    }
    resultado.innerHTML = resulpnn
})