import unittest

from defs import (
    traduzir_frame,
    traduzir_tres_frames,
    reverso_complementar,
    traduzir_seis_frames,
    codigo_genetico_rna
)


class TestTradutorProteinas(unittest.TestCase):

    def test_traduzir_frame_inicio(self):
        seq = "AUGCCUUAA"

        resultado = traduzir_frame(
            seq,
            codigo_genetico_rna,
            0
        )

        self.assertEqual(resultado, "MP*")


    def test_frame_diferente(self):
        seq = "AAUGCCUUAA"

        resultado = traduzir_frame(
            seq,
            codigo_genetico_rna,
            1
        )

        self.assertEqual(resultado, "MP*")


    def test_tres_frames(self):
        seq = "AUGCCUUAA"

        resultado = traduzir_tres_frames(
            seq,
            codigo_genetico_rna
        )

        self.assertIn("+1", resultado)
        self.assertIn("+2", resultado)
        self.assertIn("+3", resultado)

        self.assertEqual(resultado["+1"], "MP*")


    def test_reverso_complementar_dna(self):
        seq = "ATGC"

        resultado = reverso_complementar(seq)

        self.assertEqual(resultado, "GCAT")


    def test_reverso_complementar_rna(self):
        seq = "AUGC"

        resultado = reverso_complementar(seq)

        self.assertEqual(resultado, "GCAU")


    def test_seis_frames(self):
        seq = "ATGGCCATT"

        resultado = traduzir_seis_frames(
            seq,
            codigo_genetico_rna
        )

        self.assertEqual(len(resultado), 6)

        self.assertIn("+1", resultado)
        self.assertIn("-1", resultado)


    def test_codon_invalido(self):
        seq = "AUGXXX"

        resultado = traduzir_frame(
            seq,
            codigo_genetico_rna,
            0
        )

        self.assertIn("?", resultado)


if __name__ == "__main__":
    unittest.main()