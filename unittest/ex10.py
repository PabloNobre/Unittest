import unittest

def par_ou_impar(numero):
    if numero % 2 == 0:
        return "Par"
    else:
        return "Ímpar"

class TestParOuImpar(unittest.TestCase):
    def test_numero_negativo_par(self):
        self.assertEqual(par_ou_impar(-2), "Par")

    def test_numero_negativo_impar(self):
        self.assertEqual(par_ou_impar(-1), "Ímpar")

    def test_numero_zero(self):
        self.assertEqual(par_ou_impar(0), "Par")

    def test_numero_impar(self):
        self.assertEqual(par_ou_impar(1), "Ímpar")

    def test_numero_par(self):
        self.assertEqual(par_ou_impar(2), "Par")

if __name__ == "__main__":
    unittest.main()
