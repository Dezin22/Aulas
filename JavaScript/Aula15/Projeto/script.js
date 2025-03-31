{/* <div class="card">
  <div class="card-img"></div>
  <h3 class="card-title">Título do Álbum 1</h3>
  <p class="card-description">Artista</p>
  <p class="card-description">duracao</p>
<div> */}

const musicaDiv = document.querySelector("#cards-grid")

async function carregarMusica() {
  const url = 'https://67e1c8fb58cc6bf785271301.mockapi.io/api/musicas'
  const resposta = await fetch(url)
  const musicas = await resposta.json()
  musicas.forEach(musica =>{
    musicaDiv.innerHTML += `
    <div class="card">
      <div class="card-img"><img
      src = "${musica.imagem}"  alt="" class="imagens-albuns">
      </div>
      <h3 class="card-title">${musica.tituloMusica}</h3>
      <p class="card-description">${musica.artista}</p>
      <p class="card-description">${musica.duracao}</p>`
  })
}

carregarMusica()