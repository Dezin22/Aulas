let nome = document.querySelector("#nome")
let botao = document.querySelector("#botao")
let print = document.querySelector("#print")

botao.addEventListener("click", ()=>{
    print.innerHTML = `Olá ${nome.value}! Seja Bem Vindo!!`
})
