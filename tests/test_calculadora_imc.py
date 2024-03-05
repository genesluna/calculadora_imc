import unittest
from calculadora_imc import CalculadoraIMC


class TestCalculadoraIMC(unittest.TestCase):
    # Configuração
    def setUp(self) -> None:
        self.calc_imc = CalculadoraIMC()

    # Deve calcular o IMC corretamente para diferentes valores de peso e altura.
    def test_deve_calcular_imc_corretamente(self):
        # Ação
        resultado = self.calc_imc.calcular_imc(70, 1.75)
        # Assegurar
        self.assertAlmostEqual(resultado, 22.86, places=2)

    # Deve categorizar corretamente o IMC em categorias específicas.
    def test_deve_categorizar_imc_corretamente(self):
        self.assertEqual(self.calc_imc.categorizar_imc(17), "Abaixo do peso")
        self.assertEqual(self.calc_imc.categorizar_imc(22), "Peso normal")
        self.assertEqual(self.calc_imc.categorizar_imc(27), "Sobrepeso")
        self.assertEqual(self.calc_imc.categorizar_imc(32), "Obesidade grau 1 (Moderada)")
        self.assertEqual(self.calc_imc.categorizar_imc(37), "Obesidade grau 2 (Severa)")
        self.assertEqual(self.calc_imc.categorizar_imc(42), "Obesidade grau 3 (Mórbida)")

    # Deve calcular corretamente o IMC e a categoria do IMC para um conjunto de peso e altura dados.
    def test_deve_calcular_todos_os_resultados_corretamente(self):
        resultado = self.calc_imc.calcular(70, 1.75)
        self.assertTrue(resultado["sucesso"])
        self.assertAlmostEqual(resultado["imc"], 22.86, places=2)
        self.assertEqual(resultado["categoria_imc"], "Peso normal")

    # Deve lidar adequadamente com a entrada de valores inválidos para peso e altura.
    def test_deve_lidar_com_valores_invalidos(self):
        resultado = self.calc_imc.calcular("abc", "def")
        self.assertFalse(resultado["sucesso"])
        self.assertEqual(resultado["erro"], "Por favor, insira valores válidos para peso e altura.")

    # Deve levantar uma exceção ao lidar com uma altura menor ou igual a zero.
    def test_deve_lidar_com_altura_menor_ou_igual_a_zero(self):
        with self.assertRaises(ValueError) as context:
            self.calc_imc.calcular(80, 0)
        self.assertEqual(str(context.exception), "Altura inválida. A altura deve ser maior que zero.")

    # Deve levantar uma exceção ao lidar com um peso menor ou igual a zero.
    def test_deve_lidar_com_peso_menor_ou_igual_a_zero(self):
        with self.assertRaises(ValueError) as context:
            self.calc_imc.calcular(0, 1.85)
        self.assertEqual(str(context.exception), "Peso inválido. O peso deve ser maior que zero.")


if __name__ == "__main__":
    unittest.main()
