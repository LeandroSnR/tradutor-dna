codigo_genetico_rna = {
    "UUU":"F","UUC":"F","UUA":"L","UUG":"L",
    "CUU":"L","CUC":"L","CUA":"L","CUG":"L",
    "AUU":"I","AUC":"I","AUA":"I","AUG":"M",
    "GUU":"V","GUC":"V","GUA":"V","GUG":"V",
    "UCU":"S","UCC":"S","UCA":"S","UCG":"S",
    "CCU":"P","CCC":"P","CCA":"P","CCG":"P",
    "ACU":"T","ACC":"T","ACA":"T","ACG":"T",
    "GCU":"A","GCC":"A","GCA":"A","GCG":"A",
    "UAU":"Y","UAC":"Y","UAA":"*","UAG":"*",
    "CAU":"H","CAC":"H","CAA":"Q","CAG":"Q",
    "AAU":"N","AAC":"N","AAA":"K","AAG":"K",
    "GAU":"D","GAC":"D","GAA":"E","GAG":"E",
    "UGU":"C","UGC":"C","UGA":"*","UGG":"W",
    "CGU":"R","CGC":"R","CGA":"R","CGG":"R",
    "AGU":"S","AGC":"S","AGA":"R","AGG":"R",
    "GGU":"G","GGC":"G","GGA":"G","GGG":"G"
}

def traduzir_frame(sequencia, tabela, frame):
    """
    Traduz um único reading frame (0, 1 ou 2).
    """

    sequencia = sequencia.upper().replace("T", "U")
    proteina = ""

    for i in range(frame, len(sequencia) - 2, 3):
        codon = sequencia[i:i+3]
        proteina += tabela.get(codon, "?")

    return proteina

def traduzir_tres_frames(sequencia, tabela):
    """
    Retorna as traduções dos frames +1, +2 e +3.
    """

    return {
        "+1": traduzir_frame(sequencia, tabela, 0),
        "+2": traduzir_frame(sequencia, tabela, 1),
        "+3": traduzir_frame(sequencia, tabela, 2)
    }

def reverso_complementar(sequencia):
    """
    Gera a sequência reverso-complementar.
    Aceita DNA ou RNA.
    """

    sequencia = sequencia.upper()

    if "U" in sequencia:
        complemento = {
            "A":"U",
            "U":"A",
            "C":"G",
            "G":"C"
        }
    else:
        complemento = {
            "A":"T",
            "T":"A",
            "C":"G",
            "G":"C"
        }

    return "".join(complemento[base] for base in reversed(sequencia))

def traduzir_seis_frames(sequencia, tabela):
    """
    Traduz os seis reading frames.
    """

    resultado = {}

    # fita direta
    resultado.update(traduzir_tres_frames(sequencia, tabela))

    # fita reverso-complementar
    reversa = reverso_complementar(sequencia)

    resultado["-1"] = traduzir_frame(reversa, tabela, 0)
    resultado["-2"] = traduzir_frame(reversa, tabela, 1)
    resultado["-3"] = traduzir_frame(reversa, tabela, 2)

    return resultado

