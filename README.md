Processamento de Linguagens (ESI) - laboral
-----

## trabalho prático 

### grupo  22     

| Número | Nome |
| 26424 | Afonso Diogo Lopes dos Santos Magalhães Almeida |
| 25436 | Bernardo Miguel Fernandes Martins |
| 26427 | Henrique Meira Gomes |

### estrutura do projeto

  [/doc](./doc)   documentação de apoio do projeto desenvolvido / relatório do trabalho prático
  
  [/data](./data) ficheiros de dados a serem usados no programa (.csv) 

  [/input](./input) exemplos de código na linguagem CQL - Comma Query Language  (.cql)

### dependências de módulos externos 

Este projeto requer os seguintes módulos externos:

- `ply`: Python Lex-Yacc, usado para criar o analisador léxico e sintático.

### Instalação

Para instalar os módulos necessários, correr:

```bash
pip install -r requirements.txt

```

### exemplos de utilização 

#### ficheiro de entrada

```bash
python main.py ./input/entrada1.cql 


python main.py ./input/entrada2.cql 

```

#### de forma interativa (um comando de cada vez)

```bash
python main.py 
>> IMPORT TABLE estacoes FROM "estacoes.csv";
>> SELECT * FROM estacoes;
...
```







