import unittest
from src.calculadora import Calculadora

class TestCalculadora(unittest.TestCase):

    def test_operacoes_sequenciais(self):
        calc = Calculadora()
        calc.somar(2, 3)
        calc.multiplicar(calc.obter_ultimo_resultado(), 4)
        calc.dividir(calc.obter_ultimo_resultado(), 2)
        self.assertEqual(calc.obter_ultimo_resultado(), 10)
        self.assertEqual(len(calc.historico), 3)

    def test_integracao_historico_resultado(self):
        calc = Calculadora()
        calc.potencia(2, 3)
        calc.somar(calc.obter_ultimo_resultado(), 2)
        self.assertEqual(calc.obter_ultimo_resultado(), 10)
        self.assertEqual(len(calc.historico), 2)
        self.assertIn("2 ^ 3 = 8", calc.historico)
        self.assertIn("8 + 2 = 10", calc.historico)


if __name__ == "__main__":
    unittest.main()
