import ply.lex as lex

# Palabras reservadas del lenguaje
reserved = {
    'declare' : 'TkDeclare',
    'if'      : 'TkIf',
    'fi'      : 'TkFi',
    'for'     : 'TkFor',
    'rof'     : 'TkRof',
    'do'      : 'TkDo',
    'od'      : 'TkOd',
    'print'   : 'TkPrint'
}

# Tipos de datos en el lenguaje
type_data = {
    'int'   : 'TkInt',
    'bool'  : 'TkBool',
    'array' : 'TkArray'
}

# Lista con los nombres de los tokens
tokens = [  
   'TkOBlock',
   'TkCBlock',
   'TkSoForth',
   'TkComma',
   'TkOpenPar',
   'TkClosePar',
   'TkAsig',
   'TkSemicolon',
   'TkArrow',
   'TkPlus',
   'TkMinus',
   'TkMult',
   'TkOr',
   'TkAnd',
   'TkNot',
   'TkLess',
   'TkLeq',
   'TkGeq',
   'TkGreater',
   'TkEqual',
   'TkNEqual',
   'TkOBracket',
   'TkCBracket',
   'TkTwoPoints',
   'TkConcat',
   'TkNum',
   'COMMENT',
   'STRING',
   'ID',
] + list(reserved.values()) + list(type_data.values())

# Reglas de expresiones regulares para literales
t_TkOBlock    = r'\|\['
t_TkCBlock    = r'\]\|'
t_TkSoForth   = r'\.\.'
t_TkComma     = r','
t_TkOpenPar   = r'\('
t_TkClosePar  = r'\)'
t_TkAsig      = r':='
t_TkSemicolon = r';'
t_TkArrow     = r'-->'
t_TkPlus      = r'\+'
t_TkMinus     = r'-'
t_TkMult      = r'\*'
t_TkOr        = r'\\/'
t_TkAnd       = r'/\\'
t_TkNot       = r'!'
t_TkLess      = r'<'
t_TkLeq       = r'<='
t_TkGeq       = r'>='
t_TkGreater   = r'>'
t_TkEqual     = r'=='
t_TkNEqual    = r'!='
t_TkOBracket  = r'\['
t_TkCBracket  = r'\]'
t_TkTwoPoints = r':'
t_TkConcat    = r'\.'

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    # Verificar si es palabra reservada o tipo de dato
    if t.value in reserved:
        t.type = reserved.get(t.value)
        t.value = t.type
    elif t.value in type_data:
        t.type = type_data.get(t.value)
        t.value = t.type
    return t 

# A regular expression rule with some action code
def t_TkNum(t):
    r'\d+'
    t.value = f"{t.type}({int(t.value)})" 
    return t

# Define a rule so we can track line numbers
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_COMMENT(t):
    r'//.*'
    pass

def t_STRING(t):
    r'\".*?\"'
    t.value = f"TkString({t.value})"
    return t

# A string containing ignored characters (spaces and tabs)
t_ignore = " \t"

# Error handling rule
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

def prettyString(tk):
    if tk.type == "ID" and tk.value not in reserved and tk.type not in type_data:
        if tk.value == "false" or tk.value == "true":
            return f"Tk{tk.value.capitalize()}" # Es constante booleana
        else:
            return f"TkId(\"{tk.value}\")"  # Es identificador de variable
    elif tk.type == "STRING" or tk.type == "TkNum":
        return f"{tk.value}"
    else:
        return f"{tk.type}"
     
# Construir el lexer
lexer = lex.lex()

data = '''
|[
declare
a, b, c : int;
d, e, f : array[0..2]
a := b + 3;
print e
// Esto es un comentario. Debe ser ignorado.
]|
'''
# Give the lexer some input
lexer.input(data)

# Tokenize
while True:
    tok = lexer.token()
    if not tok:
        break      # No more input
    print(prettyString(tok))
