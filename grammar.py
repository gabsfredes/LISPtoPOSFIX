# Gramatica:
# E → id
# E → n
# E → E E +
# E → E E -
# E → E E *
# E → E E /

import ply.yacc as yacc
from trabalho import tokens

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

# Teste
arquivo = open("LISPtoPOSFIX/input.txt", "r")
entrada = arquivo.read()
arquivo.close()

print(parser.parse(entrada))
