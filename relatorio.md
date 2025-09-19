# Relatório de Testes -   Calculadora

Testes rodados sem implementar nada: 12

- testes rodados com sucesso: 11
- testes rodados com falha: 1
> Erro identificado
- get: "Divisao por zero nao permitida"
- expected: " Divisao por zero nao permitida "


Testes rodados após primeira correção sem a implementação adicional: 12

- testes rodados com sucesso: 12
- testes rodados com falha: 0


### Complete os exemplos: Implemente os testes marcados como “Implemente” seguindo os padrões mostrados.

#### Implemente: Teste similar para subtração, multiplicação e divisão.

-
      def test_entrada_saida_subtracao(self):  
            calc = Calculadora()  
            resultado = calc.subtrair(5, 3)  
            self.assertEqual(resultado, 2)  
            self.assertEqual(calc.obter_ultimo_resultado(), 2)

-
      def test_entrada_saida_divisao(self):
            calc = Calculadora()
            resultado = calc.dividir(6, 3)
            self.assertEqual(resultado, 2)
            self.assertEqual(calc.obter_ultimo_resultado(), 2)

-
      def test_entrada_saida_multiplicacao(self):
            calc = Calculadora()
            resultado = calc.multiplicar(5, 3)
            self.assertEqual(resultado, 15)
            self.assertEqual(calc.obter_ultimo_resultado(), 15)

Testes rodados: 15
- testes rodados com sucesso: 15
- testes rodados com falha: 0

### Implemente: Teste tipagem para todas as operações matemáticas

-
      with self.assertRaises(TypeError):
        calc.multiplicar([10], None) # List no lugar de numero
-
      with self.assertRaises(TypeError):
        calc.subtrair(True, None) # Bool no lugar de numero



Testes rodados: 15
- testes rodados com sucesso: 15
- testes rodados com falha: 0


### Implemente: Teste com valores próximos ao limite de float do Python.


-
      #Teste: somar algo pequeno ao limite ainda funciona (não vira inf)
        resultado = calc.somar(max_float, 0.0)
        self.assertEqual(resultado, max_float)

-
      #Teste: somar o limite com ele mesmo deve resultar em inf (overflow)
        resultado_inf = calc.somar(max_float, max_float)
        self.assertTrue(resultado_inf == float("inf"))

-
      #Teste: multiplicar por 2 também deve resultar em inf
        resultado_mul = calc.multiplicar(max_float, 2)
        self.assertTrue(resultado_mul == float("inf"))



Testes rodados: 15
- testes rodados com sucesso: 15
- testes rodados com falha: 0

### Adicione testes extras: Para cada categoria, crie pelo menos um teste adicional não mostrado nos exemplos.

Teste extra para soma

-
      def test_soma_negativos_e_zero(self):
          calc = Calculadora()
          resultado = calc.somar(-3, 0)
          self.assertEqual(resultado, -3)
          self.assertEqual(calc.obter_ultimo_resultado(), -3)

        
Teste extra para multiplicacao

-
      def test_multiplicacao_negativos(self):
          calc = Calculadora()
          resultado = calc.multiplicar(-4, -5)
          self.assertEqual(resultado, 20)

Testes rodados: 17
- testes rodados com sucesso: 17
- testes rodados com falha: 0


## Terminal
-
      PS D:\SimulacaoTestes\projeto_calculadora> coverage run -m unittest discover tests
      .................
      ----------------------------------------------------------------------
      Ran 17 tests in 0.003s


-
      PS D:\SimulacaoTestes\projeto_calculadora> coverage report
      Name                        Stmts   Miss  Cover
      -----------------------------------------------
      src\__init__.py                 0      0   100%
      src\calculadora.py             45      1    98%
      tests\teste_integracao.py      20      1    95%
      tests\teste_unidade.py         91      0   100%
      -----------------------------------------------
      TOTAL                         156      2    99%
