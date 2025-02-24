const img = document.querySelector("#img")

function ligar(){
    return img.setAttribute("src","./img/ligada.jpg")
}
function desligada(){
    return img.setAttribute("src", "./img/desligada.jpg")
}