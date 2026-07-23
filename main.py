<<<<<<< HEAD
codigo_genetico_dna = {
    "TTT":"F","TTC":"F","TTA":"L","TTG":"L",
    "CTT":"L","CTC":"L","CTA":"L","CTG":"L",
    "ATT":"I","ATC":"I","ATA":"I","ATG":"M",
    "GTT":"V","GTC":"V","GTA":"V","GTG":"V",
    "TCT":"S","TCC":"S","TCA":"S","TCG":"S",
    "CCT":"P","CCC":"P","CCA":"P","CCG":"P",
    "ACT":"T","ACC":"T","ACA":"T","ACG":"T",
    "GCT":"A","GCC":"A","GCA":"A","GCG":"A",
    "TAT":"Y","TAC":"Y","TAA":"*","TAG":"*",
    "CAT":"H","CAC":"H","CAA":"Q","CAG":"Q",
    "AAT":"N","AAC":"N","AAA":"K","AAG":"K",
    "GAT":"D","GAC":"D","GAA":"E","GAG":"E",
    "TGT":"C","TGC":"C","TGA":"*","TGG":"W",
    "CGT":"R","CGC":"R","CGA":"R","CGG":"R",
    "AGT":"S","AGC":"S","AGA":"R","AGG":"R",
    "GGT":"G","GGC":"G","GGA":"G","GGG":"G"
}

codigo_genetico_rna = {
    "TTT":"F","TTC":"F","TTA":"L","TTG":"L",
    "CTT":"L","CTC":"L","CTA":"L","CTG":"L",
    "ATT":"I","ATC":"I","ATA":"I","ATG":"M",
    "GTT":"V","GTC":"V","GTA":"V","GTG":"V",
    "TCT":"S","TCC":"S","TCA":"S","TCG":"S",
    "CCT":"P","CCC":"P","CCA":"P","CCG":"P",
    "ACT":"T","ACC":"T","ACA":"T","ACG":"T",
    "GCT":"A","GCC":"A","GCA":"A","GCG":"A",
    "TAT":"Y","TAC":"Y","TAA":"*","TAG":"*",
    "CAT":"H","CAC":"H","CAA":"Q","CAG":"Q",
    "AAT":"N","AAC":"N","AAA":"K","AAG":"K",
    "GAT":"D","GAC":"D","GAA":"E","GAG":"E",
    "TGT":"C","TGC":"C","TGA":"*","TGG":"W",
    "CGT":"R","CGC":"R","CGA":"R","CGG":"R",
    "AGT":"S","AGC":"S","AGA":"R","AGG":"R",
    "GGT":"G","GGC":"G","GGA":"G","GGG":"G"
=======
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
>>>>>>> suprna
}

def traduzir(sequencia, tabela):
    sequencia = sequencia.upper()
    sequencia = sequencia.replace("T", "U")
    proteina = ""

    inicio = sequencia.find("AUG")
    if inicio == -1:
        return "Não existe códon de início."
    else:
        sequencia = sequencia[inicio:]

    for i in range(0, len(sequencia)-2, 3):
        codon = sequencia[i:i+3]

        aminoacido = tabela.get(codon)

        if aminoacido is None:
            proteina += "?"
            continue

        if aminoacido == "*":
            break

        proteina += aminoacido

    return proteina

testes = ["AUGCCUUAA", "ATGGCCUAG", "AUGGCCTAA", "AUGGCCTAGG", "AUGGCCUAGC", "AUGGCCUAGU", "AUGGCCUAGGCU", "AUGGCCUAGGCUA", "AUGGCCUAGGCUAA", "AUGGCCUAGGCUAAA"]
for teste in testes:
    print(traduzir(teste, codigo_genetico_rna))