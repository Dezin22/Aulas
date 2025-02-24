const num1 = document.querySelector("#num1")
const num2 = document.querySelector("#num2")
const botao = document.querySelector("#botao")
const result = document.querySelector("#result")


botao.addEventListener('click',()=>{
    const somar = Number(num1.value) + Number(num2.value)
    result.innerHTML = `= ${somar}`
})