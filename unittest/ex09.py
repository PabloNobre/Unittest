import unittest

def fibonacci(n):
    if n == 0 or n == 1:
        return n
    a, b = 0, 1
    for i in range(2, n + 1):
        a, b = b, a + b
    return a

class TestFibonacci(unittest.TestCase):
    def test_numero_negativo(self):
        self.assertEqual(fibonacci(-1), 0)

    def test_numero_zero(self):
        self.assertEqual(fibonacci(0), 0)

    def test_numero_um(self):
        self.assertEqual(fibonacci(1), 1)

    def test_numero_cinco(self):
        self.assertEqual(fibonacci(5), 5)

    def test_numero_dez(self):
        self.assertEqual(fibonacci(10), 55)

if __name__ == "__main__":
    unittest.main()
