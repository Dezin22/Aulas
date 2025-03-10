function cadastrarCliente(){
    const nome = document.querySelector("#nome").value
    const email = document.querySelector("#email").value
    const telefone = document.querySelector("#telefone").value
    const tabela = document.querySelector("#tabela")
    tabela.innerHTML += `<tr>
            <th scope="row">${nome} </th>
            <td>${email}</td>
            <td>${telefone}</td>
        </tr>`
}