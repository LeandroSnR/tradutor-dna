# 🧬 Protein Translator

Um tradutor simples de **sequências de DNA para proteínas** desenvolvido em Python.

O programa identifica o **primeiro códon de início (`ATG`)**, realiza a tradução da sequência utilizando o **código genético padrão** e interrompe a tradução ao encontrar um **códon de parada (`TAA`, `TAG` ou `TGA`)**.

## Funcionalidades

* Tradução de sequências de DNA em proteínas.
* Busca automática pelo primeiro códon de início (`ATG`).
* Utiliza a tabela completa do código genético (64 códons).
* Interrompe a tradução ao encontrar um códon de parada.
* Código simples e comentado, ideal para estudos de Bioinformática e Biologia Molecular.

## Como funciona

1. O usuário fornece uma sequência de DNA.
2. O programa procura o primeiro `ATG`.
3. A sequência é dividida em códons (trincas de nucleotídeos).
4. Cada códon é convertido em seu aminoácido correspondente.
5. A tradução termina quando um códon de parada é encontrado.

### Exemplo

Entrada:

```text
ATGGTTTTCTAA
```

Tradução:

```text
ATG | GTT | TTC | TAA
 M     V     F   Stop
```

Saída:

```text
MVF
```

## Estrutura do projeto

```text
protein-translator/
│
├── main.py
└── README.md
```

## Como executar

Clone o repositório:

```bash
git clone https://github.com/LeandroSnR/tradutor-dna.git
```

Entre na pasta do projeto:

```bash
cd tradutor-dna
```

Execute:

```bash
python main.py
```

## Tecnologias

* Python 3
* Estrutura de dados (`dict`) para armazenar o código genético.

## Próximas melhorias

* [ ] Suporte a RNA (`U` → `T`).
* [ ] Tradução dos três quadros de leitura (Reading Frames).
* [ ] Leitura de arquivos FASTA.
* [ ] Saída em aminoácidos de três letras (Met, Val, Phe...).
* [ ] Interface gráfica.
* [ ] Testes automatizados.

## Objetivo

Este projeto foi desenvolvido como prática de programação em Python aplicada à Bioinformática, demonstrando como o código genético pode ser utilizado para traduzir sequências de DNA em proteínas de maneira simples e didática.

## Licença

Este projeto é disponibilizado para fins educacionais. Sinta-se à vontade para utilizá-lo, modificá-lo e contribuir.
