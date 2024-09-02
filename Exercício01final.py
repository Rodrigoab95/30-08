def contar_pares(lista_numeros):
    return len([num for num in lista_numeros if num % 2 == 0])

def listar_impares(lista_numeros):
    return [num for num in lista_numeros if num % 2 != 0]

def encontrar_maior_numero(lista_numeros):
    return max(lista_numeros)

def encontrar_menor_numero(lista_numeros):
    return min(lista_numeros)

def calcular_media(lista_numeros):
    return sum(lista_numeros) / len(lista_numeros)

valores = []
continuar = True

while continuar:
    valor = int(input("Digite um número (ou digite 0 para parar): "))
    
    if valor == 0:
        continuar = False
    else:
        valores.append(valor)

print("Quantidade de números pares:", contar_pares(valores))
print("Números ímpares:", listar_impares(valores))
print("Maior número:", encontrar_maior_numero(valores))
print("Menor número:", encontrar_menor_numero(valores))
print("Média dos números:", calcular_media(valores))
