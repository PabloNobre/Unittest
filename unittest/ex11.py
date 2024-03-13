import unittest

def nome_na_lista(nome, lista_nomes):
  
    return nome.lower() in [nome.lower() for nome in lista_nomes]

class TestNomeNaLista(unittest.TestCase):
    def test_nome_presente(self):
        self.assertTrue(nome_na_lista("João", ["Ana", "João", "Maria"]))

    def test_nome_ausente(self):
        self.assertFalse(nome_na_lista("Pedro", ["Ana", "João", "Maria"]))

    def test_nome_com_caixa_alta(self):
        self.assertTrue(nome_na_lista("JOÃO", ["Ana", "joão", "Maria"]))

if __name__ == "__main__":
    unittest.main()
