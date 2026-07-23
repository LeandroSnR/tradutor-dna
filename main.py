import sys

from defs import (
    codigo_genetico_rna,
    ler_fasta,
    traduzir_tres_frames,
    traduzir_seis_frames
)


def mostrar_resultado(resultado):

    print("\n===== RESULTADOS =====")

    for frame, proteina in resultado.items():
        print(f"{frame}: {proteina}")

    print("======================\n")


def processar_sequencia(sequencia):

    print("\nSequência analisada:")
    print(sequencia)

    print("""
Escolha a análise:

1 - Traduzir 3 frames (+1, +2, +3)
2 - Traduzir 6 frames (+/-)

""")

    opcao = input("Opção: ")

    if opcao == "1":

        resultado = traduzir_tres_frames(
            sequencia,
            codigo_genetico_rna
        )

        mostrar_resultado(resultado)


    elif opcao == "2":

        resultado = traduzir_seis_frames(
            sequencia,
            codigo_genetico_rna
        )

        mostrar_resultado(resultado)


    else:

        print("Opção inválida.")


def carregar_fasta(caminho):

    try:

        sequencia = ler_fasta(caminho)

        processar_sequencia(sequencia)

    except FileNotFoundError:

        print(
            f"Arquivo não encontrado: {caminho}"
        )


def menu():

    print("""
==============================
   🧬 PROTEIN TRANSLATOR
==============================

1 - Digitar sequência
2 - Abrir arquivo FASTA
3 - Sair
""")


    opcao = input("Escolha: ")


    if opcao == "1":

        sequencia = input(
            "\nDigite a sequência: "
        )

        processar_sequencia(
            sequencia.upper()
        )


    elif opcao == "2":

        caminho = input(
            "\nArquivo FASTA: "
        )

        carregar_fasta(caminho)


    elif opcao == "3":

        exit()


    else:

        print("Opção inválida.")


def main():

    # Caso tenha sido passado um arquivo:
    # python main.py exemplo.fasta

    if len(sys.argv) > 1:

        arquivo = sys.argv[1]

        carregar_fasta(arquivo)

    else:

        menu()


if __name__ == "__main__":
    main()
