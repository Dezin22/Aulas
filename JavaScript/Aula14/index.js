
const tabela = document.querySelector("#tb");



async function carregarDados(){
    const cep = document.querySelector("#cep").value;
    const url = `https://viacep.com.br/ws/${cep}/json/`;
    const response = await fetch(url);
    const data = await response.json();
    tabela.innerHTML = "";
    console.log(data);
    tabela.innerHTML = `
    <tr>
    <td>Rua:</td>
    <td>${data.logradouro}</td></tr>
    <tr>
    <td>Bairro: </td>
    <td>${data.bairro}</td></tr>
    <tr>
    <td>Cidade: </td>
    <td>${data.localidade}</td></tr>
    <tr>
    <td>Estado: </td>
    <td>${data.uf}</td></tr>
    `;
}
async function carregarProdutos(){
    const url = `https://67e1c8fb58cc6bf785271301.mockapi.io/api/product`;
    const response = await fetch(url);
    const data = await response.json();
    console.log(data);
}