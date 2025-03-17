// localStorage.clear();
const nome = document.querySelector("#nome")
const lista = document.querySelector("#lista")
const usuarios = Array(localStorage.getItem("cliente"))
function cadastrarCliente(){
    let valor_nome = nome.value
    if (valor_nome){
        usuarios.push(valor_nome)
        
    }else{
        inputNome.setAttribute("placeholder","Valor Obrigatório")
    }
    lista.innerHTML = ""
    localStorage.setItem("cliente", (usuarios))
    mostrarUsuarios()
    nome.value = ""

}

function mostrarUsuarios(){
    let usuarios = localStorage.getItem("cliente").split(",") 
    console.log(usuarios)
    usuarios.forEach(usuario=>{
    lista.innerHTML += `<li>${usuario}</li>`
})}
mostrarUsuarios()
console.log(usuarios)
// const objeto = {
//     nome: "Andre"
// }
// const objetoJSON = JSON.stringify(objeto)
// localStorage.setItem("cliente", objetoJSON)

// let objeto2 = localStorage.getItem("cliente")

// console.log(objeto2)