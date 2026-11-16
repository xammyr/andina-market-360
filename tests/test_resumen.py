import unittest
from src.resumen import calcular_resumen


class TestResumenVentas(unittest.TestCase):
    def setUp(self):
        self.resumen = calcular_resumen()

    def test_total_operaciones(self):
        self.assertEqual(self.resumen["operaciones"], 12)

    def test_total_general(self):
        self.assertAlmostEqual(self.resumen["total_general"], 1845.00, places=2)

    def test_totales_por_sede(self):
        sedes = self.resumen["por_sede"]
        self.assertAlmostEqual(sedes["Lima"], 814.00, places=2)
        self.assertAlmostEqual(sedes["Ica"], 555.00, places=2)
        self.assertAlmostEqual(sedes["Arequipa"], 476.00, places=2)

    def test_metadatos_ficticios(self):
        self.assertEqual(self.resumen["proyecto"], "Andina Market 360")
        self.assertIn("Ficticio", self.resumen["tipo_datos"])


if __name__ == "__main__":
    unittest.main()
