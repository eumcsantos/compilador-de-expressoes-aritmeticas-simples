# 🧮 Compilador de Expressões Aritméticas Simples

> Projeto final desenvolvido para a disciplina de **Compiladores** do curso de Bacharelado em Ciências da Computação.

Este projeto consiste na implementação completa de um compilador para expressões matemáticas (soma, subtração, multiplicação e divisão), incluindo todas as etapas clássicas de compilação: análise léxica, análise sintática, geração de código intermediário e execução através de uma Máquina Virtual baseada em pilha (Stack Machine).

## 🚀 Funcionalidades

- **Precedência de Operadores:** Respeita a ordem matemática correta (multiplicação/divisão antes de soma/subtração) e o uso de parênteses.
- **Arquitetura Modular:** Separação clara entre *Front-end* (Lexer/Parser) e *Back-end* (CodeGen/VM).
- **Geração de Código:** Traduz expressões de alto nível para uma linguagem de montagem (Assembly) hipotética.
- **Máquina Virtual Integrada:** Executa o código Assembly gerado, exibindo o estado da pilha passo a passo.

## 🛠️ Arquitetura do Compilador

O sistema foi desenhado seguindo o pipeline clássico de compiladores:

1.  **Lexer (Analisador Léxico):** Lê a string de entrada e a converte em uma sequência de *tokens*.
2.  **Parser (Analisador Sintático):** Utiliza a técnica *Recursive Descent* para validar a gramática e construir a Árvore Sintática Abstrata (AST).
3.  **Code Generator:** Percorre a AST (padrão *Visitor*) e emite instruções para uma máquina de pilha.
4.  **Virtual Machine:** Interpreta as instruções sequenciais e calcula o resultado final.

### Gramática (BNF)

A análise sintática segue a seguinte *Backus-Naur Form* para garantir a precedência:

```text
expr   : term ((PLUS | MINUS) term)*
term   : factor ((MUL | DIV) factor)*
factor : INTEGER | LPAREN expr RPAREN

### Conjunto de Instruções (ISA)

Instrução,Descrição
PUSH n,Empilha o valor inteiro n no topo da pilha.
ADD,"Desempilha dois valores, soma e empilha o resultado."
SUB,"Desempilha dois valores, subtrai e empilha o resultado."
MUL,"Desempilha dois valores, multiplica e empilha o resultado."
DIV,"Desempilha dois valores, divide (inteiro) e empilha o resultado."
```

## 📂 Estrutura do Projeto

```text
/
├── lexer.py           # Definição de Tokens e Análise Léxica
├── parser.py          # Definição da AST e Análise Sintática
├── codeGenerator.py   # Conversão de AST para Assembly
├── virtualMachine.py  # Execução do código Assembly
├── main.py            # Ponto de entrada (Driver Code)
└── README.md          # Documentação
```

## 💻 Como Executar

Pré-requisitos:
- **Python 3.x instalado.**
- **Nenhuma biblioteca externa é necessária (apenas Standard Library).**

### Passo a Passo
    1. Clone o repositório: git clone https://github.com/eumcsantos/compilador-de-expressoes-aritmeticas-simples.git
    2. Entre na pasta do projeto: cd compilador-de-expressoes-aritmeticas-simples
    3. Abra o terminal na pasta do projeto e execute o arquivo principal: python3 main.py
    4. Exemplo de Saída: Ao executar a expressão (10 + 2) / 4 - 3, o console exibirá:
        1. ENTRADA: (10 + 2) / 4 - 3
        2. PARSER: Árvore Sintática (AST) construída com sucesso.

        3. CÓDIGO INTERMEDIÁRIO (ASSEMBLY):
        ---------------------------------
        PUSH 10
        PUSH 2
        ADD
        PUSH 4
        DIV
        PUSH 3
        SUB
        ---------------------------------

        4. EXECUÇÃO NA VM:
        EXEC: PUSH 10      | Pilha: [10]
        EXEC: PUSH 2       | Pilha: [10, 2]
        EXEC: ADD (10, 2)  | Pilha: [12]
        EXEC: PUSH 4       | Pilha: [12, 4]
        EXEC: DIV (12, 4)  | Pilha: [3]
        EXEC: PUSH 3       | Pilha: [3, 3]
        EXEC: SUB (3, 3)   | Pilha: [0]

        >>> Resultado Final: 0

## 👨‍💻 Autor

- **Desenvolvido por:** Matheus Costa Santos
- **Curso:** Ciências da Computação
- **Disciplina:** Compiladores
- **Semestre:** 5º Semestre
