import unittest
import adn as f

class pruebas(unittest.TestCase):

    def test_generar_cadena_complementaria(self):
        self.assertEqual(f.generar_cadena_complementaria('atgc'), 'tacg')
        self.assertEqual(f.generar_cadena_complementaria('ATCG'), 'TAGC')
        self.assertEqual(f.generar_cadena_complementaria('ATgc'), 'TAcg')
        self.assertRaises(ValueError, f.generar_cadena_complementaria, 'zr')
        self.assertRaises(ValueError, f.generar_cadena_complementaria, 'UR')
        self.assertRaises(TypeError, f.generar_cadena_complementaria, -2)
        self.assertRaises(TypeError, f.generar_cadena_complementaria, 2.2)
        self.assertRaises(TypeError, f.generar_cadena_complementaria, 2)

    def test_corresponden(self):
        self.assertEqual(f.corresponden('AAA', 'TTT'), True)
        self.assertEqual(f.corresponden('gca', 'cgt'), True)
        self.assertEqual(f.corresponden('Gca', 'Cgt'), True)
        self.assertEqual(f.corresponden('AAA', 'GCC'), False)
        self.assertEqual(f.corresponden('cga', 'gcc'), False)
        self.assertRaises(ValueError, f.corresponden, 'III', 'gcg')
        self.assertRaises(ValueError, f.corresponden, 'zdd', 't')
        self.assertRaises(TypeError, f.corresponden, 1, 't')
        self.assertRaises(TypeError, f.corresponden, 2.2, 't')
        self.assertRaises(TypeError, f.corresponden, -2, 't')

    def test_es_base(self):
        self.assertEqual(f.es_base('t'), True)
        self.assertEqual(f.es_base('a'), True)
        self.assertEqual(f.es_base('g'), True)
        self.assertEqual(f.es_base('c'), True)
        self.assertEqual(f.es_base('T'), True)
        self.assertEqual(f.es_base('A'), True)
        self.assertEqual(f.es_base('G'), True)
        self.assertEqual(f.es_base('C'), True)
        self.assertEqual(f.es_base('d'), False)
        self.assertEqual(f.es_base('F'), False)
        self.assertRaises(ValueError, f.es_base, 'aaa')
        self.assertRaises(ValueError, f.es_base, 'AAA')
        self.assertRaises(TypeError, f.es_base, 1)
        self.assertRaises(TypeError, f.es_base, 1.1)
        self.assertRaises(TypeError, f.es_base, -2)

    def test_reparar_dano(self):
        self.assertEqual(f.reparar_dano('aaa', 'ttt'), 'No presenta errores')
        self.assertEqual(f.reparar_dano('GGG', 'CCC'), 'No presenta errores')
        self.assertEqual(f.reparar_dano('AAA', 'ACC'), 'TTT')
        self.assertEqual(f.reparar_dano('tcc', 'ggg'), 'agg')
        self.assertRaises(ValueError, f.reparar_dano, 'AUU', 'AAA')

