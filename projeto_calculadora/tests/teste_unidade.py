import unittest
import sys



from src.calculadora import Calculadora

class TestCalculadora(unittest.TestCase):

    # Teste extra para soma
    def test_soma_negativos_e_zero(self):
        calc = Calculadora()
        resultado = calc.somar(-3, 0)
        self.assertEqual(resultado, -3)
        self.assertEqual(calc.obter_ultimo_resultado(), -3)


    def test_entrada_saida_soma(self):
        calc = Calculadora()
        resultado = calc.somar(5, 3)
        self.assertEqual(resultado, 8)
        self.assertEqual(calc.obter_ultimo_resultado(), 8)

    #Implementado_inicio
    def test_entrada_saida_subtracao(self):
            calc = Calculadora()
            resultado = calc.subtrair(5, 3)
            self.assertEqual(resultado, 2)
            self.assertEqual(calc.obter_ultimo_resultado(), 2)

    def test_entrada_saida_divisao(self):
        calc = Calculadora()
        resultado = calc.dividir(6, 3)
        self.assertEqual(resultado, 2)
        self.assertEqual(calc.obter_ultimo_resultado(), 2)

    def test_entrada_saida_multiplicacao(self):
        calc = Calculadora()
        resultado = calc.multiplicar(5, 3)
        self.assertEqual(resultado, 15)
        self.assertEqual(calc.obter_ultimo_resultado(), 15)

    def test_multiplicacao_negativos(self):
        calc = Calculadora()
        resultado = calc.multiplicar(-4, -5)
        self.assertEqual(resultado, 20)
    #Implementado_fim


    def test_tipagem_invalida(self):
        calc = Calculadora()
        with self.assertRaises(TypeError):
            calc.somar("5", 3) # String no lugar de numero
        with self.assertRaises(TypeError):
            calc.dividir(10, None) # None no lugar de numero
        #Implementado_inicio
        with self.assertRaises(TypeError):
            calc.multiplicar([10], None) # List no lugar de numero
        with self.assertRaises(TypeError):
            calc.subtrair(True, None) # boolean no lugar de numero
        #Implementado_fim





    def test_consistencia_historico(self):
        calc = Calculadora()
        calc.somar(2, 3)
        calc.multiplicar(4, 5)
        self.assertEqual(len(calc.historico), 2)
        self.assertIn("2 + 3 = 5", calc.historico)
        self.assertIn("4 * 5 = 20", calc.historico)

    def test_inicializacao(self):
        calc = Calculadora()
        self.assertEqual(calc.resultado, 0)
        self.assertEqual(len(calc.historico), 0)

    def test_modificacao_historico(self):
        calc = Calculadora()
        calc.somar(1, 1)
        self.assertEqual(len(calc.historico), 1)
        calc.limpar_historico()
        self.assertEqual(len(calc.historico), 0)

    def test_limite_inferior(self):
        calc = Calculadora()
        self.assertEqual(calc.somar(0, 5), 5)
        self.assertEqual(calc.multiplicar(-1e-10, 2), -2e-10)
        #Implementado_inicio
        min_float = sys.float_info.min

        resultado = calc.subtrair(min_float, 1e-308)
        # deve continuar representando um número válido (não zero)
        self.assertNotEqual(resultado, 0.0)
        #Implementado_fim

    def test_limite_superior(self):
        calc = Calculadora()
        max_float = sys.float_info.max
        self.assertEqual(calc.somar(1e10, 1e10), 2e10)

        # Teste: somar algo pequeno ao limite ainda funciona (não vira inf)
        resultado = calc.somar(max_float, 0.0)
        self.assertEqual(resultado, max_float)

        # Teste: somar o limite com ele mesmo deve resultar em inf (overflow)
        resultado_inf = calc.somar(max_float, max_float)
        self.assertTrue(resultado_inf == float("inf"))

        # Teste: multiplicar por 2 também deve resultar em inf
        resultado_mul = calc.multiplicar(max_float, 2)
        self.assertTrue(resultado_mul == float("inf"))


    def test_divisao_por_zero(self):
        calc = Calculadora()
        with self.assertRaises(ValueError):
            calc.dividir(10, 0)

    def test_fluxos_divisao(self):
        calc = Calculadora()
        self.assertEqual(calc.dividir(10, 2), 5)
        with self.assertRaises(ValueError):
            calc.dividir(10, 0)

    def test_mensagens_erro(self):
        calc = Calculadora()
        with self.assertRaises(ValueError) as contexto:
            calc.dividir(5, 0)
        self.assertEqual(str(contexto.exception), " Divisao por zero nao permitida ")
