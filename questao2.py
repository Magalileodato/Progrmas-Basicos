# O código fornece uma interface simples para que o usuário possa gerenciar e 
# realizar cálculos básicos em uma lista de números inteiros, 
# tudo dentro de um loop contínuo que só termina quando o usuário decide sair.

# Adiciona um número à lista
def AdicionarNumero(lista):
    while True:
        numero = input("Digite um número inteiro: ")
        try:
            # Converter a entrada para um número inteiro
            numero = int(numero)
            lista.append(numero)  # Adiciona o número à lista
            print("Número adicionado com sucesso!")
            break
        except ValueError:
            # Mensagem de erro para entradas que não são números inteiros
            print("Entrada inválida. Por favor, digite um número inteiro.")

# Permite visualizar os números na lista
def VisualizarNumeros(lista):
    if lista:
        print(f"Números na lista: {lista}")  
    else:
        print("A lista está vazia.")  

# Permite calcular a média dos números na lista
def CalcularMedia(lista):
    if lista:
        # Calcula a média dos números na lista
        media = sum(lista) / len(lista)  
        print(f"A média dos números na lista é: {media:.2f}")  
    else:
        print("Não há números na lista para calcular a média.")  

# Permite calcular a soma dos números na lista
def CalcularSoma(lista):
     # Calcula a soma dos números na lista
    if lista:
        soma = sum(lista)  # Calcula a soma dos números na lista
        print(f"A soma dos números na lista é: {soma}")  
    else:
        print("Não há números na lista para calcular a soma.")  

# Permite exibir o menu de opções
def ExibirMenu():
    print("\n1. Adicionar Número")
    print("2. Visualizar Números")
    print("3. Calcular Média")
    print("4. Calcular Soma")
    print("5. Sair")

# Programa principal 
def main():
    ListaNumeros = []  
    while True:
        # Exibe o menu de opções
        ExibirMenu() 
        opcao = input("Escolha uma opção: ")
        
        # Executa a operação correspondente com base na escolha do usuário
        if opcao == '1':
            AdicionarNumero(ListaNumeros)
        elif opcao == '2':
            VisualizarNumeros(ListaNumeros)
        elif opcao == '3':
            CalcularMedia(ListaNumeros)
        elif opcao == '4':
            CalcularSoma(ListaNumeros)
        elif opcao == '5':
            print("Saindo do programa...")
            break  # Encerra o loop e sai do programa
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")  

# Programa principal
if __name__ == "__main__":
    main()
