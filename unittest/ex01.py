import unittest

def soma(a, b):
    return a + b

class TestSoma(unittest.TestCase):

    def test_soma_numeros_positivos(self):
        resultado = soma(1, 2)

        self.assertEqual(resultado, 3)


    def test_soma_numeros_negativos(self):
        resultado = soma(-1, -2)

        self.assertEqual(resultado, -3)


    def test_soma_numeros_positivos_e_negativos(self):
        resultado = soma(1, -2)

        self.assertEqual(resultado, -1)

if __name__ == '__main__':
    unittest.main()