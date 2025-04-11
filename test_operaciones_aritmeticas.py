import unittest
from operaciones_aritmeticass import OperacionesAritmeticas

class TestSuma(unittest.TestCase):
    def test_suma_dosNumeros_retornaSuma(self):
        # Arrange
        operando1 = 10
        operando2 = 15
        resultadoEsperado = 25

        obj = OperacionesAritmeticas(operando1, operando2)

        # Act
        resultadoActual = obj.calcularSuma()

        # Assert
        self.assertEqual(resultadoEsperado, resultadoActual, msg="Falló la suma")

    def test_suma_operadorNoNumerico_lanzaExcepcion(self):
        with self.assertRaises(TypeError):
            obj = OperacionesAritmeticas(3, "a")
            obj.calcularSuma()


class TestDivision(unittest.TestCase):
    def test_division_dosNumeros_retornaDivision(self):
        # Arrange
        dividendo = 10
        divisor = 15
        resultadoEsperado = 10 / 15

        obj = OperacionesAritmeticas(dividendo, divisor)

        # Act
        resultadoActual = obj.calcular_division()

        # Assert
        self.assertAlmostEqual(resultadoEsperado, resultadoActual, places=2, msg="Falló la división")

    def test_division_operadorNoNumerico_lanzaExcepcion(self):
        with self.assertRaises(TypeError):
            obj = OperacionesAritmeticas(3, "a")
            obj.calcular_division()

    def test_division_divisorCero_lanzaExcepcion(self):
        with self.assertRaises(ZeroDivisionError):
            obj = OperacionesAritmeticas(3, "a")
            obj.calcular_division()

if __name__ == '__main__':
    unittest.main()
