import ply.lex as lex
import codecs
import sys
import os

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

# Calcula la columna del token [token]
#   data es la cadena de entrada
#   token es una instancia de token
def find_column(input, token):
    line_start = input.rfind('\n', 0, token.lexpos) + 1
    return (token.lexpos - line_start) + 1

# String con los caracteres que se ignoran (espacios y tabs)
t_ignore = " \t"

# Error handling rule
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

# Retorna un string del token [tk] en formato legible (segun las especificaciones)
#   tk es una instancia de token.
def prettyString(tk):
    if tk.type == "ID" and tk.value not in reserved and tk.type not in type_data:
        if tk.value == "false" or tk.value == "true":
            s = f"Tk{tk.value.capitalize()}" # Es constante booleana
        else:
            s = f"TkId(\"{tk.value}\")"  # Es identificador de variable
    elif tk.type == "STRING" or tk.type == "TkNum":
        s = f"{tk.value}"
    else:
        s = f"{tk.type}"
    return f"{s} {tk.lineno} {find_column(data, tk)}"

# Verifica la entrada, si hay error muestra el mensaje y termina con
# la ejecucion del programa
def input_check():
    if len(sys.argv) < 2:
        print("Error, no especifico el archivo del programa.")
        sys.exit()
    elif os.path.splitext(sys.argv[1])[1] != ".gcl":
        print("Error, la extension del archivo no es .gcl")
        sys.exit()

# Tokenize
def tokenize():
    while True:
        tok = lexer.token()
        if not tok:
            break      # No more input
        print(prettyString(tok))

# Codifica el archivo de entrada a utf-8 y retorna su contenido.
def read_file():
    fp = codecs.open(name_file, "r", "utf-8")
    return fp.read()

# Verificar parametro de entrada
input_check()

# Leer y codificar el archivo de entrada
name_file = sys.argv[1]
data = read_file()

# Construir el lexer
lexer = lex.lex()

# Darle al lexer la entrada
lexer.input(data)

# Tokenize
tokenize()

# Falta documentar
# Verificar si falta algun token/palabra reservada
# Caracter ilegal
