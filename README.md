# projetos-fatec
Repositório para armazenar meus exercícios da faculdade

# Conversor de Bases Numéricas (2 a 16) 🧮

##  Sobre o Projeto
Este projeto foi desenvolvido como parte dos estudos no curso de Análise e Desenvolvimento de Sistemas (FATEC). Trata-se de um script em Python que realiza a conversão de números inteiros positivos entre qualquer base numérica de 2 a 16 (incluindo binário, octal, decimal e hexadecimal).

O objetivo principal deste exercício foi aplicar conceitos fundamentais de lógica de programação, manipulação de strings, laços de repetição e tratamento de exceções.

##  Funcionalidades
O código não apenas realiza a conversão matemática, mas possui uma forte camada de validação para garantir a robustez do programa:
* **Validação de Base:** Verifica se as bases de entrada e saída informadas pelo usuário estão dentro do intervalo permitido (2 a 16).
* **Validação de Entrada:** Impede o processamento de entradas vazias, números negativos ou caracteres que não pertencem à base de entrada selecionada.
* **Conversão Bidirecional Algorítmica:** A lógica principal transforma qualquer entrada para a base decimal primeiro, e em seguida, converte o valor decimal para a base de saída desejada, manipulando caracteres de 'A' a 'F' quando necessário para bases superiores a 10.

##  Tecnologias Utilizadas
* **Python 3:** Uso de funções (`def`), estruturas de controle (`while`, `if/else`), listas/dicionários e tratamento de erros (`try/except`).

##  Como Executar
1. Certifique-se de ter o Python instalado em sua máquina.
2. Faça o clone deste repositório ou baixe o arquivo `.py`.
3. Execute o script no terminal:
   ```bash
   python nome_do_arquivo.py
