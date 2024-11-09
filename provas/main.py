def usuario():
        total_media = 0
        nome = input("Digite o nome do aluno: ")
            
        
        nota1 = float(input("Digite a nota 1: "))
        nota2 = float(input("Digite a nota 2: "))
        nota3 = float(input("Digite a nota 3: "))
            
        
        media = (nota1 + nota2 + nota3) / 3
        total_media += media
            
    
        if media >= 7.0:
            status = "Aprovado"
        else:
            status = "Reprovado"
        
        print(f"\nAluno: {nome}")
        print(f"Média: {media:.2f}")
        print(f"Status: {status}")

