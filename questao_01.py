
# O código exibe a soma total e a lista de números primos encontrados,
# proporcionando uma prática interessante do uso de recursividade em Python
# para manipulação de listas e a soma.


# Responsável por converter a string de entrada em uma lista de inteiros
def ConverteStrEmInteiros(s):
    return list(map(int, s.split()))


# Responsável por realizar a soma da lista de forma recursiva
def SomaLista(lst):
    if not lst:  # Caso base: lista vazia
        return 0
    return lst[0] + SomaLista(lst[1:])  # Soma o primeiro elemento com o restante da lista


# Responsável por verificar se um número é primo
def VerificaNumeroPrimo(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


# Retorna os números primos em uma lista de inteiros de forma recursiva
def RetornaNumerosPrimos(lst):
    if not lst:  # Caso base: lista vazia
        return []
    primeiro = lst[0]
    # Recursão no restante da lista
    RestoPrimos = RetornaNumerosPrimos(lst[1:])  
    # Adicionando o número primo encontrado
    if VerificaNumeroPrimo(primeiro):
        return [primeiro] + RestoPrimos  
    else:
          return RestoPrimos  

# Usuário fornece os números
entrada = input("Escreva aqui sua sequência de inteiros: ")

# Confirmando os números fornecidos
print(f"Os números fornecidos foram: {entrada}")

# Convertendo a entrada para uma lista de inteiros
ListaInteiros = ConverteStrEmInteiros(entrada)

# Calculando a soma utilizando a função recursiva
soma = SomaLista(ListaInteiros)

# Encontrando os números primos na lista de forma recursiva
primos = RetornaNumerosPrimos(ListaInteiros)

# Exibindo os resultados
print(f"A soma da sequência {entrada} é: {soma}")

if primos:
    print(f"Os números primos na sequência {entrada} são: {primos}")
else:
    print(f"Não há elementos primos em {entrada}")
