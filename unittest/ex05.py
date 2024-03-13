import unittest

def media(lista):
    return sum(lista) / len(lista)

class TestMedia(unittest.TestCase):
    def test_lista_vazia(self):
        self.assertEqual(media([]), 0)

    def test_lista_com_um_elemento(self):
        self.assertEqual(media([1]), 1)

    def test_lista_com_varios_elementos(self):
        self.assertEqual(media([1, 2, 3]), 2)

if __name__ == "__main__":
    unittest.main()
