// Componentes (Elementos HTML)
function Tarefa(tarefa) {
    // Construindo LI
    const liTarefa = document.createElement("li");
    // liTarefa.textContent = `${tarefa} - ${descricao} -> `
  
    const h2Tarefa = document.createElement("h2");
    h2Tarefa.textContent = tarefa.nome;
  
    const pDescricao = document.createElement("p");
    pDescricao.textContent = tarefa.descricao;
  
    const divInfo = document.createElement("div");
    divInfo.appendChild(h2Tarefa);
    divInfo.appendChild(pDescricao);
  
    const checkboxTarefa = document.createElement("input");
    checkboxTarefa.type = "checkbox";
    checkboxTarefa.checked = tarefa.completa;
  
    liTarefa.appendChild(divInfo);
    liTarefa.appendChild(checkboxTarefa);
    liTarefa.classList.add("tarefa");
  
    return liTarefa;
  }
  
  // Lógica da Tela
  let tarefasState = [
    {
      nome: "Estudar AWS",
      descricao: "Realizar curso do mauro tanana",
      completa: true,
    },
    {
      nome: "Nginx para Deploy",
      descricao: "Na marra",
      completa: false,
    },
  ];
  
  // Listar Tarefas
  function listarTarefas(tarefas) {
    const ulTarefas = document.getElementById("tarefas");
    ulTarefas.textContent = "";
    
    if (tarefas.length == 0) {
      ulTarefas.textContent = "Não foram encontrados resultados...";
      return
    }
  
    tarefas.map((tarefa) => {
      const liTarefa = Tarefa(tarefa);
      ulTarefas.appendChild(liTarefa);
    });
  }
  
  function handleListarTarefas() {
      // Logica para buscar as tarefas de outro lugar.
      listarTarefas(tarefasState);
  }
  
  window.addEventListener("load", handleListarTarefas)
  
  // Pesquisar Tarefas
  const inputPesquisar = document.getElementById('pesquisar')
  
  function handlePesquisarTarefas() {
      let pesquisa = inputPesquisar.value.toLowerCase()
      
      let resultado = tarefasState.filter((tarefa) => tarefa.nome.toLowerCase().includes(pesquisa))
      
      listarTarefas(resultado)
  }
  
  inputPesquisar.addEventListener("input", handlePesquisarTarefas)
  
  // Adicionar Nova Tarefa
  const formulario = document.getElementById("form-tarefa");
  
  function handleAdicionarTarefa(event) {
    event.preventDefault();
  
    // Capturando do Formulaŕio
    let novaTarefa = {
      nome: formulario.tarefa.value,
      descricao: formulario.descricao.value,
      completa: false,
    };
  
    tarefasState.push(novaTarefa);
    listarTarefas(tarefasState);
}