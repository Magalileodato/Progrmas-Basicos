# O código gera e analisa uma sequência de números inteiros com base em três valores de entrada: i, j, e k.
# Logo, exibe a sequência gerada, os números pares encontrados, e os pares que são quadrados perfeitos. 
# Caso não haja elementos pares ou quadrados perfeitos, mensagens de erro são exibidas.


import math

# Responsável por gerar uma sequência com os primeiros i elementos. 
# Caso os dois primeiros elementos são j e k, e cada elemento subsequente é a soma dos dois anteriores.
def GerarSequencia(i, j, k):
    # Inicializa a lista com os dois primeiros elementos fornecidos
    sequencia = [j, k]

    # Gera a sequência até o i-ésimo elemento
    for _ in range(2, i):
        # O próximo elemento é a soma dos dois anteriores
        ProximoElemento = sequencia[-1] + sequencia[-2]
        # Adiciona o próximo elemento à lista
        sequencia.append(ProximoElemento)

    return sequencia

# Responsável por filtrar e retornar os elementos pares da sequência.
def EncontrarPares(sequencia):
    # Filtra apenas os elementos pares da sequência
    pares = [num for num in sequencia if num % 2 == 0]
    return pares

# Responsável por  filtrar e retornar os elementos que são quadrados perfeitos dentre os elementos pares.
def EncontrarQuadradosPerfeitos(pares):
    # Filtra apenas os números que são quadrados perfeitos
    QuadradosPerfeitos = [num for num in pares if math.isqrt(num) ** 2 == num]
    return QuadradosPerfeitos

# Responsável por lê os valores de entrada i, j, k,  gerando a sequência, encontrando os pares e, 
# dentre os pares, os quadrados perfeitos. 
def main():
    # Lê os valores de entrada i, j, k
    i = int(input("Digite o valor de i: "))
    j = int(input("Digite o valor de j: "))
    k = int(input("Digite o valor de k: "))

    # Gera a sequência com base nos valores fornecidos
    sequencia = GerarSequencia(i, j, k)
    print(f"Os {i} elementos da sequência são {sequencia}.")

    # Encontra os elementos pares na sequência
    pares = EncontrarPares(sequencia)
    if pares:
        print(f"Os elementos pares da sequência são {pares}.")
        
        # Encontra os quadrados perfeitos entre os pares
        QuadradosPerfeitos = EncontrarQuadradosPerfeitos(pares)
        if QuadradosPerfeitos:
            print(f"Dentre esses, os que são quadrado perfeito são {QuadradosPerfeitos}.")
        else:
            print("Não há elemento par quadrado perfeito.")
    else:
        print(f"Não há elementos pares na sequência até a posição {i}.")

# Executa a função principal
if __name__ == "__main__":
    main()
