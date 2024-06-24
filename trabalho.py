# Alfabeto = {id, n, +, −, ∗, /}
import ply.lex as lex
import ply.yacc as yacc

# Tokenizer
# Lista com nome dos tokens
tokens = (
    "ID", 
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

# Função para tratar ID
def t_ID(t):
    r"[a-zA-Z_][a-zA-Z0-9_]*" # Letra seguida de letras, números ou underline
    return t

# Ignorar espaços em branco
t_ignore = " \t"

# Ignorar comentários
def t_COMENTARIO(t):
    r'\#.*'
    pass

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

##################
##### Parser #####
##################

# Precendência para evitar ambiguidade
precedence = (
    ("left", "MAIS", "MENOS"),
    ("left", "VEZES", "DIVIDIR"),
)

# Definição da gramática (aqui é feita a conversão para notação posfixa)
def p_expressao_id(p):
    "expressao : ID"
    p[0] = p[1]

def p_expressao_numero(p):
    "expressao : NUMERO"
    p[0] = p[1]

def p_expressao_mais(p):
    "expressao : ABRE_PAREN MAIS expressao expressao FECHA_PAREN"
    p[0] = f"{p[3]} {p[4]} +"


def p_expressao_menos(p):
    "expressao : ABRE_PAREN MENOS expressao expressao FECHA_PAREN"
    p[0] = f"{p[3]} {p[4]} -"


def p_expressao_vezes(p):
    "expressao : ABRE_PAREN VEZES expressao expressao FECHA_PAREN"
    p[0] = f"{p[3]} {p[4]} *"


def p_expressao_dividir(p):
    "expressao : ABRE_PAREN DIVIDIR expressao expressao FECHA_PAREN"
    p[0] = f"{p[3]} {p[4]} /"
    
# Função de erro
def p_error(p):
    print("Erro de sintaxe! %s" % p)

# Construção do parser
parser = yacc.yacc()

# Função para converter expressão LISP para POSFIX
def lisp_to_postfix(expression):
    return parser.parse(expression, lexer=lexer)

# Teste
arquivo = open("LISPtoPOSFIX/input.txt", "r")
entrada = arquivo.read()
arquivo.close()

print(lisp_to_postfix(entrada))


