import unittest

def multiplicacao(a, b):

    return a * b

class TestMultiplicacao(unittest.TestCase):
  

    def test_multiplicacao_simples(self):
    
        self.assertEqual(multiplicacao(5, 2), 10)
        self.assertEqual(multiplicacao(-1, 1), -1)

    def test_multiplicacao_com_zero(self):
    
        self.assertEqual(multiplicacao(5, 0), 0)
        self.assertEqual(multiplicacao(0, 5), 0)

    def test_multiplicacao_com_negativos(self):
    
        self.assertEqual(multiplicacao(-5, -2), 10)
        self.assertEqual(multiplicacao(-5, 2), -10)

if __name__ == '__main__':
    unittest.main()
