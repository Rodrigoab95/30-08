def calcular_imc():
    try:
        peso = float(input("Digite o peso da pessoa em quilogramas: "))
        altura = float(input("Digite a altura da pessoa em metros: "))
        
        if peso <= 0 or altura <= 0:
            raise ValueError("O peso e a altura devem ser valores positivos.")
        
        imc = peso / (altura ** 2)
        print("O IMC da pessoa é: {:.2f}".format(imc))
        
    except ValueError as e:
        print("Erro: {}".format(e))
    
    finally:
        continuar = input("Deseja continuar? (s/n): ")
        if continuar.lower() == 's':
            calcular_imc()

calcular_imc()
