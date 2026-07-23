# 🧬 Protein Translator

Um tradutor de **sequências de DNA ou RNA para proteínas** desenvolvido em Python, com suporte a **reading frames** e tradução dos **seis quadros de leitura possíveis**.

O programa utiliza o **código genético padrão** para converter sequências de nucleotídeos em sequências de aminoácidos, permitindo analisar diferentes possibilidades de tradução em uma sequência de DNA.

## Funcionalidades

* Tradução de sequências de DNA ou RNA em proteínas.
* Conversão automática de DNA (`T`) para RNA (`U`).
* Tradução de um reading frame específico.
* Tradução dos três frames da fita direta (+1, +2 e +3).
* Tradução dos seis reading frames (+1, +2, +3, -1, -2 e -3).
* Geração da sequência reverso-complementar.
* Utiliza a tabela completa do código genético (64 códons).
* Identificação de códons de parada (`UAA`, `UAG` e `UGA`).
* Testes automatizados utilizando `unittest`.
* Código modular separado em funções, testes e interface principal.

## Como funciona

O DNA possui três possíveis formas de agrupamento dos nucleotídeos em códons. Cada uma delas representa um **reading frame** diferente.

Exemplo:

```text
ATGGCCATT
```

Pode ser lido como:

```text
Frame +1:
ATG | GCC | ATT
 M     A     I

Frame +2:
TGG | CCA
 W     P

Frame +3:
GGC | CAT
 G     H
```

O programa realiza essas traduções e também analisa a fita complementar reversa, totalizando seis possibilidades.

O processo de tradução:

1. O usuário fornece uma sequência de DNA ou RNA.
2. O programa converte a sequência para RNA.
3. A sequência é dividida em códons de três nucleotídeos.
4. Cada códon é convertido em um aminoácido utilizando a tabela genética.
5. Os códons de parada são identificados.
6. A proteína resultante é retornada para o usuário.

## Exemplo

Entrada:

```text
ATGGTTTTCTAA
```

Frame +1:

```text
AUG | GUU | UUC | UAA
 M     V     F    Stop
```

Saída:

```text
MVF*
```

Os demais frames também podem ser analisados pelo programa.

## Estrutura do projeto

```text
tradutor-dna/
│
├── defs.py
├── testes.py
├── main.py
└── README.md
```

### `defs.py`

Contém:

* tabela do código genético;
* funções de tradução;
* geração da sequência reverso-complementar;
* tradução dos três e seis reading frames.

### `testes.py`

Contém:

* testes automatizados das funções principais;
* validação das traduções;
* testes de complementaridade e múltiplos frames.

### `main.py`

Contém:

* menu interativo;
* entrada de sequências;
* apresentação dos resultados.

## Como executar

Clone o repositório:

```bash
git clone https://github.com/LeandroSnR/tradutor-dna.git
```

Entre na pasta do projeto:

```bash
cd tradutor-dna
```

Execute o programa:

```bash
python main.py
```

Para executar os testes:

```bash
python testes.py
```

## Tecnologias

* Python 3
* Estrutura de dados `dict` para armazenamento do código genético.
* Biblioteca `unittest` para testes automatizados.

## Próximas melhorias

* [x] Suporte a DNA (`T` → `U`).
* [x] Tradução dos três quadros de leitura (Reading Frames).
* [x] Tradução dos seis quadros de leitura (+/-).
* [x] Testes automatizados.
* [ ] Leitura de arquivos FASTA.
* [ ] Identificação automática da maior ORF (Open Reading Frame).
* [ ] Saída em aminoácidos de três letras (Met, Val, Phe...).
* [ ] Interface gráfica.
* [ ] Exportação dos resultados.

## Objetivo

Este projeto foi desenvolvido como prática de programação em Python aplicada à Bioinformática, demonstrando como sequências de DNA podem ser analisadas computacionalmente para identificar possíveis traduções em proteínas.

O projeto busca unir conceitos de programação, Biologia Molecular e análise de sequências genéticas de forma simples e didática.

## Licença

Este projeto é disponibilizado para fins educacionais. Sinta-se à vontade para utilizá-lo, modificá-lo e contribuir.
