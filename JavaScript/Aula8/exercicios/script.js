let obj = {
    nome: "JOSE DO CAMINHÃO",
    idade: 65,
    endereco: "rua teste bairro teste",
    telefone: 3197614946
}

console.log(obj.nome)
console.log(obj.idade)
console.log(obj.endereco)
console.log(obj.telefone)


const nome = document.querySelector("#nome")
const idade = document.querySelector("#idade")
const tel = document.querySelector("#tel")
const bt = document.querySelector("#bt")
const lista = document.querySelector("#lista")
let pessoa = {}
bt.addEventListener('click',()=>{
   
    let pessoa = {
        nome : nome.value,
        idade : idade.value,
        tel : tel.value
    }
    nome.value = ""
    idade.value = ""
    tel.value = ""
    console.log(pessoa)
    console.log(JSON.stringify(pessoa))
    pessoa.innerHTML = pessoa
})


