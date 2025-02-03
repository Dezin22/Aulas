let usuario = []
const lista = document.querySelector("#lista")
const nome = document.querySelector("#usuario")
const botao = document.querySelector("#botao")
const listar = document.querySelector("#listar")
const deletar = document.querySelector("#deletar")
const del = document.querySelector("#del")

// Adiciona um novo usuário ao array
botao.addEventListener('click', () => {
    if (nome.value) {  // Verifica se o campo não está vazio
        usuario.push(nome.value)
        nome.value = ""  // Limpa o campo de input após adicionar
    }
})

// Exibe todos os usuários cadastrados
listar.addEventListener('click', () => {
    lista.innerHTML = ""  // Limpa a lista antes de adicionar os novos elementos
    usuario.forEach(user => {
        const li = document.createElement("li")
        li.textContent = user
        lista.appendChild(li)
    })
})

// Deleta um usuário baseado no nome digitado
deletar.addEventListener('click', () => {
    let index = usuario.indexOf(del.value)
    if (index > -1) {  // Verifica se o nome existe no array
        usuario.splice(index, 1)  // Remove o nome do array
        del.value = ""  // Limpa o campo de input
    } else {
        alert("Usuário não encontrado!")
    }
    lista.innerHTML = ""
    usuario.forEach(user => {
        const li = document.createElement("li")
        li.textContent = user
        lista.appendChild(li)
    })
})
