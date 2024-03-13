import unittest

def numero_primo(numero):
    if numero <= 1:
        return False
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            return False
    return True

class TestNumeroPrimo(unittest.TestCase):
    def test_numero_negativo(self):
        self.assertFalse(numero_primo(-1))

    def test_numero_um(self):
        self.assertFalse(numero_primo(1))

    def test_numero_dois(self):
        self.assertTrue(numero_primo(2))

    def test_numero_primo_par(self):
        self.assertFalse(numero_primo(10))

    def test_numero_primo_impar(self):
        self.assertTrue(numero_primo(7))

if __name__ == "__main__":
    unittest.main()
