let numero = document.querySelector("#nmb")
let botao = document.querySelector("#botao")

botao.addEventListener("click",()=>{
    let valor_numero = numero.value

    if (valor_numero > 0){
        console.log("Este numero é positivo")
    }
    else if(valor_numero < 0){
        console.log("Este numero é negativo")
    }
    else{
        console.log("Este numero é nulo")
    }

})
