import unittest

def menor_valor(lista):
    menor = lista[0]
    for valor in lista:
        if valor < menor:
            menor = valor
    return menor

class TestMenorValor(unittest.TestCase):
    def test_lista_vazia(self):

        self.assertRaises(ValueError, menor_valor, [])

    def test_lista_com_um_elemento(self):
        self.assertEqual(menor_valor([1]), 1)

    def test_lista_com_varios_elementos(self):
        self.assertEqual(menor_valor([10, 2, 5, 7, 1]), 1)

if __name__ == "__main__":
    unittest.main()
