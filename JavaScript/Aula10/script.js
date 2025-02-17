//MAP

const num = [1,2,3,4,5]
console.log(num)
const dobro = num.map((numb)=>{return numb*2})
console.log(dobro)

const nomes = ["andre","lucas","matheus"]
console.log(nomes)
const soletrar = nomes.map((nome)=>{return nome.length})//map faz uma função de for mapeando todos conteudos da array e passando um por um
console.log(soletrar)

/////////////////////////////////////////////////////////////////////////////////////////////////////////

//EVERY

let num1 = [1,2,3,4]
console.log(num1.every((numero)=>{return numero%2 == 0}))// retorna um valor booleano se a condição esta no array

//////////////////////////////////////////////////////////////////////////////////////////////////////////

//SOME

let num2 = [1,2,3,4]
console.log(num2.some((numero)=>{return numero%2 == 1}))//retorna um valor booleano se a condição existe no array

//////////////////////////////////////////////////////////////////////////////////////////////////////////

//FIND && findIndex

let num3 = [1,2,3,4,5,6,7,8,9,10]
console.log(num2.find((numero)=>{return numero%2 == 1}))//retorna o primeiro valor que esta na condição
console.log(num2.findIndex((numero)=>{return numero%2 == 1}))//retorna o index do primeiro valor que esta na condição

//////////////////////////////////////////////////////////////////////////////////////////////////////////

//FILTER

let num4 = [1,2,3,4]
let novo_num = num4.filter((numero)=>{return numero%2 == 1})// filtra e cria outra array com os conteudos que estao na condição
console.log(novo_num)

///////////////////////////////////////////////////////////////////////////////////////////////////////////

//REDUCE

let num5 = [1,2,3,4,5,6,7,8,9,10]
let novo_num2 = num5.reduce((accumulator, currentValue)=>{
    return accumulator + currentValue;
})
console.log(novo_num2)

///////////////////////////////////////////////////////////////////////////////////////////////////////////

//FOREACH

