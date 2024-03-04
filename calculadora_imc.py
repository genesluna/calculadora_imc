class CalculadoraIMC:

    def calcular_imc(self, peso, altura):
        # Calcula o Índice de Massa Corporal (IMC) usando a fórmula: peso / (altura ** 2)
        imc = peso / (altura**2)
        # Arredonda o resultado para duas casas decimais
        return round(imc, 2)

    def categorizar_imc(self, imc):
        # Classifica o IMC em categorias de acordo com os intervalos especificados
        if imc < 18.5:
            return "Abaixo do peso"
        elif 18.5 <= imc < 24.9:
            return "Peso normal"
        elif 25 <= imc < 29.9:
            return "Sobrepeso"
        elif 30 <= imc < 34.9:
            return "Obesidade grau 1 (Moderada)"
        elif 35 <= imc < 39.9:
            return "Obesidade grau 2 (Severa)"
        else:
            return "Obesidade grau 3 (Mórbida)"

    def calcular(self, peso, altura):
        # Remove espaços e substitui vírgulas por pontos, se existirem.
        altura, peso = (str(altura).strip().replace(",", "."), str(peso).strip().replace(",", "."))

        # Cria um dicionário para armazenar os resultados
        resultado = {}

        # Tenta converter os valores de entrada em Decimal. Se não der certo, retorna uma mensagem de erro.
        try:
            altura, peso = (float(altura), float(peso))
        except ValueError:
            resultado["sucesso"] = False
            resultado["erro"] = "Por favor, insira valores válidos para peso e altura."
            return resultado

        # Verifica se a altura é menor ou igual a zero, levanta uma exceção se for o caso.
        if altura <= 0:
            raise ValueError("Altura inválida. A altura deve ser maior que zero.")

        # Verifica se o peso é menor ou igual a zero, levanta uma exceção se for o caso.
        if peso <= 0:
            raise ValueError("Peso inválido. O peso deve ser maior que zero.")

        # Calcula o IMC, categoriza e armazena os resultados no dicionário
        resultado["imc"] = self.calcular_imc(peso, altura)
        resultado["categoria_imc"] = self.categorizar_imc(resultado["imc"])
        resultado["sucesso"] = True

        return resultado
