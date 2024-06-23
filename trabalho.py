# Alfabeto = {id, n, +, −, ∗, /}
# # Gramatica:
# E → id
# E → n
# E → E E +
# E → E E -
# E → E E *
# E → E E /


import ply.lex as lex

# Tokenizer
# Lista com nome dos tokens
tokens = (
    "NUMERO",
    "MAIS",
    "MENOS",
    "VEZES",
    "DIVIDIR",
    "ABRE_PAREN",
    "FECHA_PAREN",
)

# Expressões regulares para os tokens
# t_ é um prefixo especial (palavra reservada) que indica que a função é um token

t_MAIS = r"\+"
t_MENOS = r"-"  # O sinal de menos é um token separado para evitar ambiguidade
t_VEZES = r"\*"
t_DIVIDIR = r"/"  # O sinal de divisão é um token separado para evitar ambiguidade
t_ABRE_PAREN = r"\("
t_FECHA_PAREN = r"\)"


# Função para tratar números
def t_NUMERO(t):
    r"\d+"
    t.value = int(t.value)
    return t


# Ignorar espaços em branco
t_ignore = " \t"


# Numero da linha
def t_newline(t):
    r"\n+"
    t.lexer.lineno += len(
        t.value
    )  # Incrementa o número da linha para cada nova linha encontrada
    # lexer é um objeto global que contém informações sobre o estado do analisador léxico
    # lineno é um atributo de lexer que armazena o número da linha atual


# Tratamento de erro
def t_error(t):
    print("O caractere ilegal '%s' foi pulado" % t.value[0])
    t.lexer.skip(1)  # Pula o caractere ilegal


# Construir o lexer
lexer = lex.lex()

# Recebe input de arquivo txt e coloca no lexer.input
arquivo = open("input.txt", "r")
lexer.input(arquivo.read())
arquivo.close()

# Faz toneking do arquivo
while True:
    tok = lexer.token()  # tok é um objeto que contém informações sobre o token
    if not tok:
        break
    print(tok.type, tok.value, tok.lineno, tok.lexpos)
    # TIPO - VALOR - LINHA NO INPUT - POSIÇÃO NO INPUT (index)