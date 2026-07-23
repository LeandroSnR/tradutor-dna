from defs import (
    traduzir_frame,
    traduzir_tres_frames,
    traduzir_seis_frames,
    codigo_genetico_rna
)


def mostrar_menu():

    print("""
=============================
   TRADUTOR DNA/RNA -> PROTEÍNA
=============================

1 - Traduzir um reading frame
2 - Traduzir os 3 frames
3 - Traduzir os 6 frames
4 - Sair
""")


def main():

    while True:

        mostrar_menu()

        opcao = input("Escolha uma opção: ")

        if opcao == "1":

            seq = input("Digite a sequência: ")

            frame = int(
                input("Frame (1, 2 ou 3): ")
            )

            resultado = traduzir_frame(
                seq,
                codigo_genetico_rna,
                frame - 1
            )

            print("\nProteína:")
            print(resultado)


        elif opcao == "2":

            seq = input("Digite a sequência: ")

            resultado = traduzir_tres_frames(
                seq,
                codigo_genetico_rna
            )

            print("\nResultados:")

            for frame, proteina in resultado.items():
                print(frame, ":", proteina)


        elif opcao == "3":

            seq = input("Digite a sequência: ")

            resultado = traduzir_seis_frames(
                seq,
                codigo_genetico_rna
            )

            print("\nSeis reading frames:")

            for frame, proteina in resultado.items():
                print(frame, ":", proteina)


        elif opcao == "4":

            print("Encerrando...")
            break


        else:

            print("Opção inválida!")


if __name__ == "__main__":
    main()