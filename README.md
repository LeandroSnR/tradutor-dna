# 🧬 Protein Translator

Um tradutor de **sequências de DNA ou RNA para proteínas** desenvolvido em Python, com suporte a **arquivos FASTA** e análise de **reading frames**.

O programa permite traduzir sequências genéticas utilizando o **código genético padrão**, analisando os diferentes quadros de leitura possíveis de uma sequência de DNA e gerando possíveis sequências proteicas.

Este projeto representa uma etapa inicial de análise de sequências em Bioinformática, semelhante ao funcionamento de ferramentas de tradução de sequências como o **Transeq**.

---

# Funcionalidades

* Tradução de sequências de DNA ou RNA em proteínas.
* Conversão automática de DNA (`T`) para RNA (`U`).
* Leitura de sequências no formato FASTA.
* Tradução dos três reading frames da fita direta:

  * +1
  * +2
  * +3
* Tradução dos três reading frames da fita reverso-complementar:

  * -1
  * -2
  * -3
* Geração da sequência reverso-complementar.
* Uso da tabela completa do código genético (64 códons).
* Identificação de códons de parada:

  * `UAA`
  * `UAG`
  * `UGA`
* Testes automatizados utilizando `unittest`.
* Interface via terminal.

---

# Como funciona

O DNA pode ser lido em três posições diferentes, chamadas de **reading frames**.

Por exemplo:

```text
ATGGCCATT
```

Pode ser interpretado como:

```text
Frame +1

ATG | GCC | ATT
 M     A     I


Frame +2

TGG | CCA
 W     P


Frame +3

GGC | CAT
 G     H
```

Como o DNA possui duas fitas complementares, também são analisados os frames da fita reversa, totalizando seis possibilidades.

O programa:

1. Recebe uma sequência de DNA/RNA ou arquivo FASTA.
2. Converte DNA para RNA.
3. Divide a sequência em códons.
4. Traduz cada códon utilizando o código genético.
5. Retorna as possíveis proteínas em cada reading frame.

---

# Formato FASTA

O programa aceita arquivos no formato FASTA:

Exemplo:

```fasta
>gene_exemplo_001
ATGGCCATTGTAATGGGCCGCTGAAAGGGTGCCCGATAG
```

O cabeçalho (`>gene_exemplo_001`) identifica a sequência e as linhas seguintes contêm os nucleotídeos.

---

# Exemplo de uso

## Executando com arquivo FASTA

```bash
python main.py exemplo.fasta
```

Exemplo de saída:

```text
Sequência analisada:

ATGGCCATTGTAATGGGCCGCTGAAAGGGTGCCCGATAG


Escolha a análise:

1 - Traduzir 3 frames
2 - Traduzir 6 frames
```

Resultado:

```text
+1: MAIVMGR*KGAR*
+2: WPL*WAAERV
+3: GHCNGPLKGC
-1: ...
-2: ...
-3: ...
```

---

## Executando sem arquivo

Também é possível iniciar o programa sem argumentos:

```bash
python main.py
```

Nesse modo, o usuário pode inserir uma sequência manualmente ou informar um arquivo FASTA.

---

# Estrutura do projeto

```text
tradutor-dna/
│
├── defs.py
├── testes.py
├── main.py
├── exemplo.fasta
└── README.md
```

## `defs.py`

Contém:

* tabela do código genético;
* tradução de frames;
* tradução dos seis reading frames;
* cálculo do reverso-complementar;
* leitura de arquivos FASTA.

## `testes.py`

Contém testes automatizados para:

* tradução de códons;
* diferentes reading frames;
* sequência reverso-complementar;
* leitura de FASTA;
* tradução dos seis frames.

## `main.py`

Responsável pela execução do programa:

* recebe arquivos FASTA pela linha de comando;
* permite entrada manual;
* exibe os resultados das traduções.

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

Execute com FASTA:

```bash
python main.py exemplo.fasta
```

Ou execute no modo interativo:

```bash
python main.py
```

Para executar os testes:

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
* [ ] Identificação automática de ORFs (Open Reading Frames).
* [ ] Seleção da maior ORF candidata.
* [ ] Saída em aminoácidos de três letras (Met, Val, Phe...).
* [ ] Exportação dos resultados.
* [ ] Integração com bancos de dados de proteínas.
* [ ] Interface gráfica.

---

# Objetivo

Este projeto foi desenvolvido como prática de programação em Python aplicada à Bioinformática.

O objetivo é demonstrar como conceitos de Biologia Molecular, como **código genético**, **códons**, **reading frames** e **tradução proteica**, podem ser aplicados na construção de ferramentas computacionais para análise de sequências.

---

# Licença

Este projeto é disponibilizado para fins educacionais.

Sinta-se à vontade para utilizá-lo, modificá-lo e contribuir.
