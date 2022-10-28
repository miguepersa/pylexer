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
   'TkGuard',
   'Tk0Bracket',
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
t_TkGuard     = r'\[\]'
t_Tk0Bracket  = r'\['
t_TkCBracket  = r'\]'
t_TkTwoPoints = r':'
t_TkConcat    = r'\.'

# String con los caracteres que se ignoran (espacios y tabs)
t_ignore = " \t"

#Regla de expresion regular para palabras reservadas del lenguaje
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

#Regla de expresión regular para enteros
def t_TkNum(t):
    r'\d+'
    t.value = f"{t.type}({int(t.value)})" 
    return t

#Regla para rastrear los números de línea
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

#Regla de expresion regular para decartar tokens
def t_COMMENT(t):
    r'//.*'
    pass

#Regla de expresion regular para identificadores de variables
def t_STRING(t):
    r'\".*?\"'
    t.value = f"TkString({t.value})"
    return t

#Regla para el manejo de errores
def t_error(t):
    global errores

    errores = True
    print(f"Error: Unexpected character \"{t.value[0]}\" in row {t.lineno}, column {find_column(data, t)}")
    t.lexer.skip(1)

def find_column(input, token):
    '''
    Calcula la columna del token [token] 

        Parameters:
            data (str): es la cadena de entrada
            token     : es una instancia de token
    '''

    line_start = input.rfind('\n', 0, token.lexpos) + 1
    return (token.lexpos - line_start) + 1

def prettyString(tk):
    '''
    Retorna un string del token [tk] en formato legible (segun las especificaciones).

        Parameters:
            tk: Es una instancia de token.        
    '''

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

def input_check():
    """Verifica la entrada, si hay error muestra el mensaje y termina con la ejecucion del programa"""

    if len(sys.argv) < 2:
        print("Error, no especifico el archivo del programa.")
        sys.exit()
    elif os.path.splitext(sys.argv[1])[1] != ".gcl":
        print("Error, la extension del archivo no es .gcl")
        sys.exit()

def tokenize():
    """Tokenize"""

    list_tk = []
    while True:
        tk = lexer.token()
        if not tk:
            break      # No more input
        list_tk.append(tk)
    return print_tokens(list_tk)

def print_tokens(tokens):
    '''
    Muestra en pantalla los tokens reconocidos

        Parameters:
                a (list): Lista con los tokens reconocidos.
    '''

    if not errores:
        for tk in tokens:
            print(prettyString(tk))

def read_file():
    """Codifica el archivo de entrada a utf-8 y retorna su contenido."""

    fp = codecs.open(name_file, "r", "utf-8")
    return fp.read()

# Verificar parametro de entrada
input_check()

# Leer y codificar el archivo de entrada
name_file = sys.argv[1]
data = read_file()

# Indica si no se reconoce algun caracter
errores = False

# Construir el lexer
lexer = lex.lex()

# Darle al lexer la entrada
lexer.input(data)

# Tokenize
tokenize()
