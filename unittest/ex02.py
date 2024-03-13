import unittest

def subtracao(a, b):
    return a - b

class TestSubtracao(unittest.TestCase):

    def test_subtracao_simples(self):
    
        self.assertEqual(subtracao(5, 2), 3)
        self.assertEqual(subtracao(-1, 1), -2)

    def test_subtracao_com_zero(self):
    
        self.assertEqual(subtracao(5, 0), 5)
        self.assertEqual(subtracao(0, 5), -5)

    def test_subtracao_com_negativos(self):
        
        self.assertEqual(subtracao(-5, -2), -3)
        self.assertEqual(subtracao(-5, 2), -7)

if __name__ == '__main__':
    unittest.main()
