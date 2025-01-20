// //Entrada
// let numero = prompt('Digite um numero')
// //Processamento

// if (numero % 2 == 0){
//     resultado = 'Este numero é par!'
// }else{
//     resultado = 'Este numero é impar!'
// }

// // Saida

// alert(resultado)

// Faça um sistema de login
// que receba do usuario nome E senha
// se o nome E  a senha for admin e 1234 respectivamente
// exiba na tela e no terminal "LOGIN EFETUADO COM SUCESSO"
// caso contrário
// EXIBA "ACESSO NEGADO"




// Entrada

let login = prompt('Digite seu Usuario!')
let senha = prompt('Digite sua senha!')

// Processamento
if(login == 'admin' && senha == '1234'){
    resul = 'LOGIN EFETUADO COM SUCESSO'
}else{
    resul = 'ACESSO NEGADO'
}

// Saida

alert(resul)
console.log(resul)