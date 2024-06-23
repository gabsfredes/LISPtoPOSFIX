import ply.yacc as yacc
from trabalho import tokens

# Definição da gramática (regras de produção)
def p_expressao_mais(p):
    "expressao : expressao MAIS termo"
    p[0] = p[1] + p[3]

def p_expressao_menos(p):
    "expressao : expressao MENOS termo"
    p[0] = p[1] - p[3]

def p_expressao_termo(p):
    "expressao : termo"
    p[0] = p[1]

def p_termo_vezes(p):
    "termo : termo VEZES fator"
    p[0] = p[1] * p[3]
    
def p_termo_dividir(p):
    "termo : termo DIVIDIR fator"
    p[0] = p[1] / p[3]

def p_termo_fator(p):
    "termo : fator"
    p[0] = p[1]
    
def p_fator_numero(p):
    "fator : NUMERO"
    p[0] = p[1]

def p_fator_id(p):
    "fator : ID"
    p[0] = p[1]

def p_fator_parenteses(p):
    "fator : ABRE_PAREN expressao FECHA_PAREN"
    p[0] = p[2]
    
def p_error(p):
    print("Erro de sintaxe!")

# Construir o parser
parser = yacc.yacc()

# Testar o parser 
entrada = "((2 + 3) * 4) / 2" 
resultado = parser.parse(entrada)
print("Resultado: %s" % resultado) 

