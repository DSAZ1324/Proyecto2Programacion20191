import unittest
import adn as f

class pruebas(unittest.TestCase):

    def test_generar_cadena_complementaria(self):
        self.assertEqual(f.generar_cadena_complementaria('atgc'), 'tacg')
        self.assertEqual(f.generar_cadena_complementaria('ATCG'), 'TAGC')
        self.assertEqual(f.generar_cadena_complementaria('ATgc'), 'TAcg')
        self.assertRaises(ValueError, f.generar_cadena_complementaria, 'z')
        self.assertRaises(ValueError, f.generar_cadena_complementaria, 'U')
        self.assertRaises(ValueError, f.generar_cadena_complementaria, 'AAAZ')
        self.assertRaises(TypeError, f.generar_cadena_complementaria, -2)
        self.assertRaises(TypeError, f.generar_cadena_complementaria, 2.2)
        self.assertRaises(TypeError, f.generar_cadena_complementaria, 2)

    def test_corresponden(self):
        self.assertEqual(f.corresponden('AAA', 'TTT'), True)
        self.assertEqual(f.corresponden('gca', 'cgt'), True)
