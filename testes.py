import unittest
import tempfile

from defs import (
    traduzir_frame,
    traduzir_tres_frames,
    reverso_complementar,
    traduzir_seis_frames,
    ler_fasta,
    codigo_genetico_rna
)


class TestTradutorProteinas(unittest.TestCase):


    def test_traduzir_frame_inicio(self):

        resultado = traduzir_frame(
            "AUGCCUUAA",
            codigo_genetico_rna,
            0
        )

        self.assertEqual(
            resultado,
            "MP*"
        )


    def test_dna_convertido_para_rna(self):

        resultado = traduzir_frame(
            "ATGCCATTAA",
            codigo_genetico_rna,
            0
        )

        self.assertEqual(
            resultado,
            "MP*"
        )


    def test_frame_diferente(self):

        resultado = traduzir_frame(
            "AAUGCCUUAA",
            codigo_genetico_rna,
            1
        )

        self.assertEqual(
            resultado,
            "MP*"
        )


    def test_tres_frames(self):

        resultado = traduzir_tres_frames(
            "AUGCCUUAA",
            codigo_genetico_rna
        )

        self.assertEqual(
            len(resultado),
            3
        )

        self.assertEqual(
            resultado["+1"],
            "MP*"
        )


    def test_reverso_complementar_dna(self):

        resultado = reverso_complementar(
            "ATGC"
        )

        self.assertEqual(
            resultado,
            "GCAT"
        )


    def test_reverso_complementar_rna(self):

        resultado = reverso_complementar(
            "AUGC"
        )

        self.assertEqual(
            resultado,
            "GCAU"
        )


    def test_seis_frames(self):

        resultado = traduzir_seis_frames(
            "ATGGCCATT",
            codigo_genetico_rna
        )

        self.assertEqual(
            len(resultado),
            6
        )

        self.assertIn(
            "+1",
            resultado
        )

        self.assertIn(
            "-1",
            resultado
        )


    def test_codon_invalido(self):

        resultado = traduzir_frame(
            "AUGXXX",
            codigo_genetico_rna,
            0
        )

        self.assertIn(
            "?",
            resultado
        )


    def test_frame_invalido(self):

        with self.assertRaises(ValueError):

            traduzir_frame(
                "AUGCCU",
                codigo_genetico_rna,
                4
            )


    def test_ler_fasta(self):

        conteudo = """>teste_gene
        ATGGCCATT
        """

        with tempfile.NamedTemporaryFile(
            mode="w",
            delete=False
        ) as arquivo:

            arquivo.write(conteudo)
            caminho = arquivo.name


        resultado = ler_fasta(caminho)


        self.assertEqual(
            resultado,
            "ATGGCCATT"
        )


if __name__ == "__main__":
    unittest.main()