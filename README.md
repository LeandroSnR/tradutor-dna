# 🧬 Protein Translator

Um tradutor de **sequências de DNA ou RNA para proteínas** desenvolvido em Python, com suporte a **reading frames**, **sequências FASTA** e análise dos seis possíveis quadros de leitura.

O projeto utiliza o **código genético padrão** para converter sequências de nucleotídeos em aminoácidos, permitindo explorar diferentes possibilidades de tradução de uma sequência genética.

---

# Funcionalidades

* Tradução de sequências de DNA ou RNA em proteínas.
* Conversão automática de DNA (`T`) para RNA (`U`).
* Tradução de um reading frame específico.
* Tradução dos três frames da fita original:

  * `+1`
  * `+2`
  * `+3`
* Geração da sequência reverso-complementar.
* Tradução dos três frames da fita reversa:

  * `-1`
  * `-2`
  * `-3`
* Tradução completa dos seis reading frames.
* Uso da tabela completa do código genético (64 códons).
* Identificação de códons de parada (`UAA`, `UAG` e `UGA`) através do símbolo `*`.
* Tratamento de códons inválidos utilizando `?`.
* Leitura de arquivos no formato FASTA.
* Validação de entradas e frames inválidos.
* Testes automatizados utilizando `unittest`.

---

# Como funciona

Uma sequência de DNA pode ser lida em três diferentes posições, chamadas de **reading frames**.

Exemplo:

```text
ATGGCCATT
```

Possibilidades de leitura:

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

Como o DNA possui duas fitas complementares, o programa também calcula a sequência reverso-complementar e traduz seus três frames, totalizando seis possibilidades.

Fluxo do programa:

```text
Sequência DNA/RNA
        |
        v
Conversão para RNA
        |
        v
Separação em códons
        |
        v
Tradução pelo código genético
        |
        v
Proteínas possíveis nos frames
```

---

# Arquivo FASTA

O programa aceita sequências armazenadas no formato FASTA.

Exemplo:

```fasta
>gene_exemplo_001
ATGGCCATTGTAATGGGCCGCTGAAAGGGTGCCCGATAG
```

O cabeçalho iniciado por `>` é ignorado e as linhas seguintes são utilizadas como sequência.

---

# Exemplo de uso

## Executando com arquivo FASTA

```bash
python main.py exemplo.fasta
```

O programa carrega automaticamente a sequência e permite escolher a análise.

Exemplo:

```text
Sequência analisada:

ATGGCCATTGTAATGGGCCGCTGAAAGGGTGCCCGATAG


+1: MAIVMGR*KGAR*
+2: WPL*WAAERV
+3: GHCNGPLKGC
-1: ...
-2: ...
-3: ...
```

---

## Executando no modo interativo

Também é possível executar sem informar um arquivo:

```bash
python main.py
```

Nesse modo, o usuário pode inserir uma sequência manualmente ou carregar um arquivo FASTA.

---

# Estrutura do projeto

```text
tradutor-dna/
│
├── defs.py
├── testes.py
├── main.py
├── exemplo.fasta
├── .gitignore
└── README.md
```

## `defs.py`

Contém:

* tabela do código genético;
* tradução de frames;
* tradução dos três e seis reading frames;
* cálculo da sequência reverso-complementar;
* leitura de arquivos FASTA;
* validação de entradas.

## `testes.py`

Contém testes automatizados para:

* tradução de frames;
* conversão DNA/RNA;
* tradução dos três frames;
* tradução dos seis frames;
* reverso-complementar de DNA e RNA;
* tratamento de códons inválidos;
* validação de frames;
* leitura de arquivos FASTA.

## `main.py`

Responsável pela execução do programa:

* leitura de arquivos FASTA via linha de comando;
* entrada manual de sequências;
* apresentação dos resultados das traduções.

---

# Como executar

Clone o repositório:

```bash
git clone https://github.com/LeandroSnR/protein-translator.git
```

Entre na pasta:

```bash
cd protein-translator
```

Execute com um arquivo FASTA:

```bash
python main.py exemplo.fasta
```

Ou execute no modo interativo:

```bash
python main.py
```

Execute os testes:

```bash
python testes.py
```

---

# Tecnologias

* Python 3
* Estrutura de dados `dict` para armazenamento do código genético.
* Biblioteca `unittest` para testes automatizados.
* Manipulação de arquivos FASTA.

---

# Próximas melhorias

* [x] Suporte a DNA (`T` → `U`).
* [x] Tradução dos três reading frames.
* [x] Tradução dos seis reading frames.
* [x] Leitura de arquivos FASTA.
* [x] Testes automatizados.
* [x] Validação de entradas.
* [ ] Identificação automática de ORFs (*Open Reading Frames*).
* [ ] Seleção da maior ORF candidata.
* [ ] Saída em aminoácidos de três letras (`Met`, `Val`, `Phe`).
* [ ] Exportação dos resultados.
* [ ] Integração com bancos de dados de proteínas.

---

# Objetivo

Este projeto foi desenvolvido como prática de programação em Python aplicada à Bioinformática.

O objetivo é demonstrar como conceitos de Biologia Molecular, como **código genético**, **códons**, **reading frames** e **tradução proteica**, podem ser aplicados na construção de ferramentas computacionais para análise de sequências biológicas.

---

# Licença

Este projeto é disponibilizado para fins educacionais.

Sinta-se à vontade para utilizá-lo, modificá-lo e contribuir.
