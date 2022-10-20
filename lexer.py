import ply.lex as lex

reserved = {
    'declare' : 'TkDeclare',
    'if'      : 'TkIf',
    'fi'      : 'TkFi',
    'for'     : 'TkFor',
    'rof'     : 'TkRof',
    'do'      : 'TkDo',
    'od'      : 'TkOd'
}

# List of token names.   This is always required
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
   'NUMBER',
   'ID',
] + list(reserved.values())

# Regular expression rules for simple tokens
t_TkOBlock    = r'\|\['
t_TkCBlock    = r'\|\]'
t_TkSoForth   = r'..'
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
t_TkOBracket  = r'\{'
t_TkCBracket  = r'\}'
t_TkTwoPoints = r':'
t_TkConcat    = r'.'

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value)    # Check for reserved words
    return t

# A regular expression rule with some action code
def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)    
    return t

# Define a rule so we can track line numbers
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# A string containing ignored characters (spaces and tabs)
t_ignore  = ' \t'

# Error handling rule
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

# Build the lexer
lexer = lex.lex()

#data = '''
#if
#(3 + 4 * 10
#  + -20 *2)
#'''
data = '''
\/
'''
# Give the lexer some input
lexer.input(data)

# Tokenize
while True:
    tok = lexer.token()
    if not tok:
        break      # No more input
    print(f'{tok.type} {tok.lexpos} {tok.lineno}')
