import unittest

def maior_valor(lista):
    maior = lista[0]
    for valor in lista:
        if valor > maior:
            maior = valor
    return maior

class TestMaiorValor(unittest.TestCase):
    def test_lista_vazia(self):

        self.assertRaises(ValueError, maior_valor, [])

    def test_lista_com_um_elemento(self):
        self.assertEqual(maior_valor([1]), 1)

    def test_lista_com_varios_elementos(self):
        self.assertEqual(maior_valor([10, 2, 5, 7, 1]), 10)

if __name__ == "__main__":
    unittest.main()
