tarefas = []

function add_tarefa(){
    const tarefa = document.querySelector("#tarefa").value
    tarefas.push(tarefa)
    const lista = document.querySelector("#lista")
    lista.innerHTML = ""
    tarefas.forEach(tarefa => {
        lista.innerHTML += `<li>${tarefa}</li>`
    });
}