

const produtoDiv = document.querySelector("#products-container")
const categoria = document.querySelector("#categoria")

function formatPrice(price) {
    if (typeof price === 'number') {
        price = parseFloat(price);
    }
    return `R$ ${price.toFixed(2)}`
}

async function carregarProduto() {
    const url = 'https://fakestoreapi.com/products'
    const resposta = await fetch(url)
    const produto = await resposta.json()
    const maxProductsToShow = 8;
    const productsToShow = produto.slice(0, maxProductsToShow)
    productsToShow.forEach(produto =>{
        const formattedPrice = formatPrice(produto.price)
        produtoDiv.innerHTML += `
              <div class="product-card">
                <div ><img src="${produto.image}" alt="" class="product-image"></div>
                <h3>${produto.title}</h3>
                <p class="product-price">${formattedPrice}</p>
                <button class="add-to-cart">Add to Cart</button>
              </div>
          </div>`
    })
    
  }
  
async function adionarProduro() {
    const nomeProduto = document.querySelector("#nomeProduto").value
    const precoProduto = document.querySelector("#nomeProduto").value
    const imagemProduto = document.querySelector("#nomeProduto").value

    const url = 'https://fakestoreapi.com/products'
    const request = await fetch(url,{
        method:"POST",
        headers:{
            "Content-Type":"application/json"
        },
        body:JSON.stringify(objeto)
    })
    fecharFormulario()
}

  carregarProduto()

  