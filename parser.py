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

# Write functions for each grammar rule which is
# specified in the docstring.
precedence = (
    ("left", "MAIS", "MENOS"),
    ("left", "VEZES", "DIVIDIR"),
)


def p_expression(p):
    '''
    expression : MAIS term term
               | MENOS term term
    '''
    # p is a sequence that represents rule contents.
    #
    # expression : term PLUS term
    #   p[0]     : p[1] p[2] p[3]
    # 
    p[0] = ('op_binaria', p[3], p[1], p[2])

def p_expression_term(p):
    '''
    expression : term
    '''
    p[0] = p[1]

def p_term(p):
    '''
    term : VEZES factor factor
         | DIVIDIR factor factor
    '''
    p[0] = ('op_binaria', p[1], p[3], p[2])

def p_term_factor(p):
    '''
    term : factor
    '''
    p[0] = p[1]

def p_factor_number(p):
    '''
    factor : NUMERO
    '''
    p[0] = ('numero', p[1])

def p_factor_id(p):
    '''
    factor : ID
    '''
    p[0] = ('id', p[1])

def p_factor_unary(p):
    '''
    factor : MAIS factor
           | MENOS factor
    '''
    p[0] = ('unario', p[1], p[2])

def p_factor_grouped(p):
    '''
    factor : ABRE_PAREN expression FECHA_PAREN
    '''
    # p[0] = ('grupo', p[2])
    p[0] = p[2]

def p_error(p):
    print(f'Erro de sintaxe: {p.value!r}')

# Build the parser
parser = yacc.yacc()

# Parse an expression
ast = parser.parse('(/ (* z(+ x y)) 2)')
print(ast)

def postfix_expression(node):
    if isinstance(node, tuple):
        if node[0] == 'op_binaria':
            left_expr = postfix_expression(node[2])
            right_expr = postfix_expression(node[3])
            return f'{left_expr} {right_expr} {node[1]}'
        elif node[0] == 'numero':
            return str(node[1])
        elif node[0] == 'id':
            return node[1]
    else:
        # Trata casos não cobertos, como números e identificadores diretamente
        return str(node)

posfixa = postfix_expression(ast)
print("\nExpressão em notação posfixa: %s" % posfixa)