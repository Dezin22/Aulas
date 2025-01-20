print("  ")
print("1 - Faça um Programa que leia um vetor de 5 números inteiros e mostre-os.")
print("  ")
print("  ")

numeros = [ ]
for i in range(5):
    numero = int(input(f"Digite o {i + 1}º número inteiro: "))
    numeros.append(numero)

print("Números digitados:", numeros)


print("2 - Faça um Programa que leia um vetor de 10 números reais e mostre-os na ordem inversa.")
print("  ")
print("  ")

numeros_reais = []
for i in range(10):
    numero = float(input(f"Digite o {i + 1}º número real: "))
    numeros_reais.append(numero)

print("Números na ordem inversa:", numeros_reais[::-1])


print("3 = Faça um Programa que leia 4 notas, mostre as notas e a média na tela.")
print("  ")
print("  ")

notas = []
for i in range(4):
    nota = float(input(f"Digite a {i + 1}ª nota: "))
    notas.append(nota)

media = sum(notas) / len(notas)
print("Notas digitadas:", notas)
print("Média:", media)


print("4 - Faça um Programa que leia um vetor de 10 caracteres, e diga quantas consoantes foram lidas. Imprima as consoantes.")
print("  ")
print("  ")

caracteres = []
consoantes = []
vogais = 'aeiouAEIOU'

for i in range(10):
    caractere = input(f"Digite o {i + 1}º caractere: ")
    if caractere.isalpha():
        caracteres.append(caractere)
        if caractere not in vogais:
            consoantes.append(caractere)

print("Consoantes lidas:", consoantes)
print("Quantidade de consoantes:", len(consoantes))


print("5 - Faça um Programa que leia 20 números inteiros e armazene-os num vetor.")
print("  ")
print("  ")

numeros = []
pares = []
impares = []

for i in range(20):
    numero = int(input(f"Digite o {i + 1}º número inteiro: "))
    numeros.append(numero)
    if numero % 2 == 0:
        pares.append(numero)
    else:
        impares.append(numero)

print("Todos os números:", numeros)
print("Números pares:", pares)
print("Números ímpares:", impares)


print("Armazene os números pares no vetor PAR e os números IMPARES no vetor impar. Imprima os três vetores.#==")
print("  ")
print("  ")