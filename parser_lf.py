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
# --- Parser --- #
##################

# Nó da árvore sintática abstrata (AST)
# Cada nó é uma tupla com a seguinte estrutura:
# ('tipo', conteúdo1, conteúdo2, ..., conteúdoN)
class Node:
    def __init__(self, value, children=None):
        self.value = value
        self.children = children if children else []

    def add_child(self, child):
        self.children.append(child)

# Write functions for each grammar rule which is

def p_E_plus(p):
    'E : ABRE_PAREN MAIS E E FECHA_PAREN'
    p[0] = ('+', p[3], p[4])

def p_E_minus(p):
    'E : ABRE_PAREN MENOS E E FECHA_PAREN'
    p[0] = ('-', p[3], p[4])

def p_E_times(p):
    'E : ABRE_PAREN VEZES E E FECHA_PAREN'
    p[0] = ('*', p[3], p[4])

def p_E_divide(p):
    'E : ABRE_PAREN DIVIDIR E E FECHA_PAREN'
    p[0] = ('/', p[3], p[4])

def p_E_id(p):
    'E : ID'
    p[0] = ('id', p[1])

def p_E_number(p):
    'E : NUMERO'
    p[0] = ('numero', p[1])

def p_error(p):
    print(f'Erro de sintaxe: {p.value!r}')

# Build the parser
parser = yacc.yacc()

# Parse an expression
<<<<<<< Updated upstream
ast = parser.parse('( * z ( + x y ) ) ')
=======
ast = parser.parse('(/ (* z(+ x y)) 2)')
>>>>>>> Stashed changes
print(ast)

def postfix_expression(node):
    if isinstance(node, tuple):
        if node[0] == 'op_binaria':
            left_expr = postfix_expression(node[3])
            right_expr = postfix_expression(node[1])
            return f'{left_expr} {right_expr} {node[2]}'
        elif node[0] == 'numero' or node[0] == 'id':
            return str(node[1])
    else:
        # Trata casos não cobertos, como números e identificadores diretamente
        return str(node)

posfixa = postfix_expression(ast)
print("\nExpressao em notacao posfixa: %s" % posfixa)