
# Tradutor de expressões numéricas em LISP para pós-fixada
Esse programa foi desenvolvido à fim de por em prática o conteúdo da disciplina de Linguagens Formais do curso de Engenharia de Computação da Universidade Federal do Pampa - [(UNIPAMPA)](https://unipampa.edu.br/)

O tradutor foi criado com intúito de converter uma entrada em LISP em uma expressão numérica pós-fixada (notação polonesa reversa). A estrutura de dados da entrada é uma lista (LISP), que é representada por uma sequência de elementos entre parênteses, sendo o primeiro elemento da lista o nome da função, seguida pelo seus argumentos. Não foram utilizadas definições de funções nem manipulação de listas em LISP, somente formas de definir um valor a partir de fórmulas aritméticas básicas.



## Instalação

As instruções de instalação e funcionalidades encontram-se no portfólio do seu criador [David M. Beazley](https://www.dabeaz.com/ply/ply.html) ou na páigna do [GitHub](https://github.com/dabeaz/ply) do próprio projeto.
    
## Arquivo de entrada (input.txt)
Nesse arquivo deve ser colocado a expressão numérica em LISP que você deseja converter.

## Características do tradutor
### Alfabeto
O tradutor tem como alfabeto {id, n, +, −, ∗, /}, onde **id** é qualquer letra do alfabeto e **n** é qualquer número, seja positivo ou negativo, decimal ou não.

### Gramática da entrada
A gramática da entrada, baseada nas expressões LISP reduzidas é a seguinte:

E → (id)

E → (n)

E → (+ E E)

E → (− E E)

E → (∗ E E)

E → (/ E E)

### Processo de tradução
O primeiro processo é a tokenização. Os tokens que foram gerados são utilizados juntos das regras de produção, conforme gramática informada acima, para que o parser possa gerar a tabela de regras da gramática e, a partir disso, analisar e garar uma AST (árvore sintática abstrata). Essa árvore então é utilizada como entrada do tradutor para que possamos converter a entrada em uma expressão numérica pós-fixada.

### Utilização
Você deve informar a expressão numérica em LISP no arquivo _input.txt_ e executar o código _parser_lf.py_
Vale ressaltar que o caminho para encontrar o arquivo txt deve ser modificado na seguinte linha:

arquivo = open('LISPtoPOSFIX/input.txt', 'r')

Onde "LISPtoPOSFIX/input.txt" foi o caminho do criador deste proejto, mas deve ser modificado para o caminho do seu computador onde o projeto se encontra.
## Autores

- [Gabriel Fredes](https://github.com/gabsfredes)
- [Gabriel Dalmazo](https://github.com/gabrieldal)
- [Nicolas Ramos](https://github.com/nicolasURamos)
- [Thales Dallasta](https://github.com/TPD01)
- [Gabriel Cardoso](https://github.com/gabrielbcardoso)


## Contribuindo

Se desejar contribuir com este projeto, por favor, faça um fork do repositório e envie um pull request com suas alterações.


## Licença

Este projeto está licenciado sob os termos da licença [MIT](https://choosealicense.com/licenses/mit/)

