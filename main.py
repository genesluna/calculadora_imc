from os import system, name
from calculadora_imc import CalculadoraIMC


def limpar_tela():
    # Limpa a tela do console de acordo com o sistema operacional
    if name == "nt":  # Se for Windows
        system("cls")
    else:  # Se for Mac ou Linux
        system("clear")


def main():
    # Cria uma instância da CalculadoraIMC
    calc_imc = CalculadoraIMC()

    # Limpa a tela antes de exibir a calculadora
    limpar_tela()

    # Apresenta o cabeçalho da calculadora
    print("=" * 40)
    print(f"{'Calculadora de IMC':^40}")
    print("=" * 40, end="\n\n")

    # Solicita ao usuário que insira o peso e a altura
    peso = input("Digite o seu peso em quilogramas: ")
    altura = input("Digite a sua altura em metros: ")

    try:
        # Tenta calcular o IMC com os valores fornecidos
        resultado = calc_imc.calcular(peso, altura)

        if resultado["sucesso"]:
            # Exibe os resultados se o cálculo for bem-sucedido
            print(f"\nSeu IMC é: {str(resultado['imc']).replace('.', ',')}")
            print(f"Categoria IMC: {resultado['categoria_imc']}\n")
        else:
            # Exibe mensagens de erro se o cálculo não for bem-sucedido
            print(resultado["erro"])

    except ValueError as e:
        # Exibe mensagem de erro caso ocorra uma exceção durante o cálculo
        print(f"\nErro: {e}\n")


if __name__ == "__main__":
    # Executa a função main() quando o script é executado diretamente
    main()
