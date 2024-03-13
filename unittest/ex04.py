import unittest

def divisao(a, b):

    if b == 0:
        raise ZeroDivisionError("Divisão por zero não é permitida")
    return round(a / b, 2)

class TesteDivisao(unittest.TestCase):

    def test_divisao_positiva(self):
     
        resultado = divisao(10, 2)
        self.assertEqual(resultado, 5.00)

    def test_divisao_negativa(self):
    
        resultado = divisao(-15, 3)
        self.assertEqual(resultado, -5.00)

    def test_divisao_por_um(self):
    
        resultado = divisao(10, 1)
        self.assertEqual(resultado, 10.00)

    def test_erro_divisao_por_zero(self):
    
        self.assertRaises(ZeroDivisionError, divisao, 10, 0)

if __name__ == "__main__":
    unittest.main()
