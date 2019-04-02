import unittest
import adn as f

class pruebas(unittest.TestCase):

    def test_obtener_complemento(self):
        self.assertEqual(f.obtener_complemento('A'), 'T')
        self.assertEqual(f.obtener_complemento('a'), 't')
        self.assertEqual(f.obtener_complemento('T'), 'A')
        self.assertEqual(f.obtener_complemento('t'), 'a')
        self.assertEqual(f.obtener_complemento('C'), 'G')
        self.assertEqual(f.obtener_complemento('c'), 'g')
        self.assertEqual(f.obtener_complemento('G'), 'C')
        self.assertEqual(f.obtener_complemento('g'), 'c')
        self.assertRaises(ValueError, f.obtener_complemento, 'z')
        self.assertRaises(ValueError, f.obtener_complemento, 'tta')
        self.assertRaises(ValueError, f.obtener_complemento, 'x')
        self.assertRaises(TypeError, f.obtener_complemento, -2.2)
        self.assertRaises(TypeError, f.obtener_complemento, 1)

    def test_generar_cadena_complementaria(self):
        self.assertEqual(f.generar_cadena_complementaria('atgc'), 'tacg')
        self.assertEqual(f.generar_cadena_complementaria('ATCG'), 'TAGC')
        self.assertEqual(f.generar_cadena_complementaria('ATgc'), 'TAcg')
        self.assertRaises(ValueError, f.generar_cadena_complementaria, 'zr')
        self.assertRaises(ValueError, f.generar_cadena_complementaria, 'UR')
        self.assertRaises(TypeError, f.generar_cadena_complementaria, -2)
        self.assertRaises(TypeError, f.generar_cadena_complementaria, 2.2)
        self.assertRaises(TypeError, f.generar_cadena_complementaria, 2)

    def test_calcular_correspondencia(self):
        self.assertEqual(f.calcular_correspondencia('ATGCTAGC', 'TACGATCG'), 100.0)
        self.assertEqual(f.calcular_correspondencia('gctaggta', 'cgataacg'), 62.5)
        self.assertEqual(f.calcular_correspondencia('CGTA', 'GCGC'), 50.0)
        self.assertEqual(f.calcular_correspondencia('atat', 'cgat'), 0.0)
        self.assertRaises(ValueError, f.calcular_correspondencia, 'cgat', 'zru')
        self.assertRaises(ValueError, f.calcular_correspondencia, 'rtu', 'gcta')
        self.assertRaises(TypeError, f.calcular_correspondencia, 'ATCG', 1)
        self.assertRaises(TypeError, f.calcular_correspondencia, 2, 'CGTA')

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

    def test_es_cadena_valida(self):
        self.assertEqual(f.es_cadena_valida('GCTA'), True)
        self.assertEqual(f.es_cadena_valida('tata'), True)
        self.assertEqual(f.es_cadena_valida('ctga'), True)
        self.assertEqual(f.es_cadena_valida('nprt'), False)
        self.assertEqual(f.es_cadena_valida('MPTR'), False)
        self.assertRaises(TypeError, f.es_cadena_valida, 1234, 'no es base')
        self.assertRaises(TypeError, f.es_cadena_valida, 5.2, 'no es base')
        self.assertRaises(TypeError, f.es_cadena_valida, -34567, 'no es base')

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

    def test_es_subcadena(self):
        self.assertEqual(f.es_subcadena('gtacg', 'acg'), True)
        self.assertEqual(f.es_subcadena('aatcg', 'cg'), True)
        self.assertEqual(f.es_subcadena('ttaagg', 'agg'), True)
        self.assertEqual(f.es_subcadena('Tata', 'ACG'), False)
        self.assertEqual(f.es_subcadena('tgctg', 'tta'), False)
        self.assertRaises(TypeError, f.es_subcadena, 'tata', 1234, 'no se pueden enteros')
        self.assertRaises(TypeError, f.es_subcadena, -4567, 'TTGCA', 'no se pueden enteros')
        self.assertRaises(TypeError, f.es_subcadena, 4567, 5678, 'no se pueden enteros')
        self.assertRaises(TypeError, f.es_subcadena, 'ttgc', 56.78, 'no se pueden enteros')

    def test_reparar_dano(self):
        self.assertEqual(f.reparar_dano('aaa', 'ttt'), 'No presenta errores')
        self.assertEqual(f.reparar_dano('GGG', 'CCC'), 'No presenta errores')
        self.assertEqual(f.reparar_dano('AAA', 'ACC'), 'TTT')
        self.assertEqual(f.reparar_dano('tcc', 'ggg'), 'agg')
        self.assertRaises(ValueError, f.reparar_dano, 'AUU', 'AAA')
        self.assertRaises(ValueError, f.reparar_dano, 'AAA', 'UAA')
        self.assertRaises(ValueError, f.reparar_dano, 'auu', 'aaa')
        self.assertRaises(ValueError, f.reparar_dano, 'AAA', 'UAA')
        self.assertRaises(TypeError, f.reparar_dano, 1, 'a')
        self.assertRaises(TypeError, f.reparar_dano, -1, 'a')
        self.assertRaises(TypeError, f.reparar_dano, 1.1, 'a')
        self.assertRaises(TypeError, f.reparar_dano, 'a', 1)
        self.assertRaises(TypeError, f.reparar_dano, 'a', 1.1)
        self.assertRaises(TypeError, f.reparar_dano, 'a', -1)

    def test_obtener_secciones(self):
        self.assertEqual(f.obtener_secciones('GTCATC', 3), ['GT', 'CA', 'TC'])
        self.assertEqual(f.obtener_secciones('GTCATCCTACTG', 10), ['G', 'T', 'C', 'A', 'T', 'C', 'C', 'T', 'A', 'CTG'])
        self.assertEqual(f.obtener_secciones('TTATTGGCA', 2), ['TTAT', 'TGGCA'])
        self.assertRaises(ValueError, f.obtener_secciones, '1234', 2)
        self.assertRaises(ValueError, f.obtener_secciones, 'ttagc', 'Z')
        self.assertRaises(TypeError, f.obtener_secciones, 'ttagc', 2.2)
        self.assertRaises(TypeError, f.obtener_secciones, 'ttagc', -2.2)

    def test_obtener_complementos(self):
        self.assertEqual(f.obtener_complementos(['aaa', 'ccc']), ['ttt', 'ggg'])
        self.assertEqual(f.obtener_complementos(['AAA', 'CCC']), ['TTT', 'GGG'])
        self.assertEqual(f.obtener_complementos(['AAA', 'ccc']), ['TTT', 'ggg'])
        self.assertEqual(f.obtener_complementos(['aaa', 'CCC']), ['ttt', 'GGG'])
        self.assertRaises(ValueError, f.obtener_complementos, ['aua', 'aaa'])
        self.assertRaises(ValueError, f.obtener_complementos, ['aaa', 'aua'])
        self.assertRaises(ValueError, f.obtener_complementos, ['AUA', 'AAA'])
        self.assertRaises(ValueError, f.obtener_complementos, ['AAA', 'AUA'])
        self.assertRaises(TypeError, f.obtener_complementos, [1, 'aaa'])
        self.assertRaises(TypeError, f.obtener_complementos, [2.2, 'aaa'])
        self.assertRaises(TypeError, f.obtener_complementos, [-2, 'aaa'])
        self.assertRaises(TypeError, f.obtener_complementos, ['aaa', 1])
        self.assertRaises(TypeError, f.obtener_complementos, ['aaa', 1.1])
        self.assertRaises(TypeError, f.obtener_complementos, ['aaa', -2])

    def test_unir_cadenas(self):
        self.assertEqual(f.unir_cadena(['ATCGTA', 'TAGCAT']), 'ATCGTATAGCAT')
        self.assertEqual(f.unir_cadena(['atcg', 'tagc']), 'atcgtagc')
        self.assertEqual(f.unir_cadena(['TCGATCGAT', 'AGCTAGCTA']), 'TCGATCGATAGCTAGCTA')
        self.assertRaises(ValueError, f.obtener_complementos, ['aua', 'aaa'])
        self.assertRaises(ValueError, f.obtener_complementos, ['aaa', 'aua'])
        self.assertRaises(ValueError, f.obtener_complementos, ['AUA', 'AAA'])
        self.assertRaises(ValueError, f.obtener_complementos, ['AAA', 'AUA'])
        self.assertRaises(TypeError, f.obtener_complementos, [1, 'aaa'])
        self.assertRaises(TypeError, f.obtener_complementos, [2.2, 'aaa'])
        self.assertRaises(TypeError, f.obtener_complementos, [-2, 'aaa'])
        self.assertRaises(TypeError, f.obtener_complementos, ['aaa', 1])
        self.assertRaises(TypeError, f.obtener_complementos, ['aaa', 1.1])
        self.assertRaises(TypeError, f.obtener_complementos, ['aaa', -2])

    def test_complementar_cadenas(self):
        self.assertEqual(f.complementar_cadenas(['aaa', 'ccc']), 'tttggg')
        self.assertEqual(f.complementar_cadenas(['AAA', 'CCC']), 'TTTGGG')
        self.assertEqual(f.complementar_cadenas(['AGc', 'Gca']), 'TCgCgt')
        self.assertRaises(ValueError, f.obtener_complementos, ['aua', 'aaa'])
        self.assertRaises(ValueError, f.obtener_complementos, ['aaa', 'aua'])
        self.assertRaises(ValueError, f.obtener_complementos, ['AUA', 'AAA'])
        self.assertRaises(ValueError, f.obtener_complementos, ['AAA', 'AUA'])
        self.assertRaises(TypeError, f.obtener_complementos, [1, 'aaa'])
        self.assertRaises(TypeError, f.obtener_complementos, [2.2, 'aaa'])
        self.assertRaises(TypeError, f.obtener_complementos, [-2, 'aaa'])
        self.assertRaises(TypeError, f.obtener_complementos, ['aaa', 1])
        self.assertRaises(TypeError, f.obtener_complementos, ['aaa', 1.1])
        self.assertRaises(TypeError, f.obtener_complementos, ['aaa', -2])





