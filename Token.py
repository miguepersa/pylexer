class Token():
	"""
		Clase definida para los tokens del lenguaje
	"""
	
	def __init__(self, x0: int, y0: int):
		"""
			Constructor de la clase. 
			Input: 
				x0: int - Coordenada horizontal del token en el programa
				y0: int - Coordenada vertical del token en el programa
		"""
		self.x = x0
		self.y = y0

	def __str__(self):
		return f"{self.x} {self.y}"

class TkDeclare(Token):
	"""
		Clase definida para los tokens de declaración de variables.
	"""
	def __init__(self, x0: int, y0: int):
		"""
			Constructor de la clase.
		"""
		super().__init__(x0, y0)

	def __str__(self):
		return "TkDeclare " + super().__str__()

class TkDo(Token):
	"""
		Clase definida para los ciclos do.
	"""
	def __init__(self, x0: int, y0: int):
		"""
			Constructor de la clase.
		"""
		super().__init__(x0, y0)

	def __str__(self):
		return "TkDo " + super().__str__()

class TkOd(Token):
	"""
		Clase definida para el cierre de los ciclos do.
	"""
	def __init__(self, x0: int, y0: int):
		"""
			Constructor de la clase.
		"""
		super().__init__(x0, y0)

	def __str__(self):
		return "TkOd " + super().__str__()

class TkIf(Token):
	"""
		Clase definida para los tokens de condicionales if.
	"""
	def __init__(self, x0: int, y0: int):
		"""
			Constructor de la clase.
		"""
		super().__init__(x0, y0)

	def __str__(self):
		return "TkIf " + super().__str__()

class TkFi(Token):
	"""
		Clase definida para los tokens de cierre de los condicionales if.
	"""
	def __init__(self, x0: int, y0: int):
		"""
			Constructor de la clase.
		"""
		super().__init__(x0, y0)

	def __str__(self):
		return "TkFi " + super().__str__()


class TkFor(Token):
	"""
		Clase definida para los ciclos for.
	"""
	def __init__(self, x0: int, y0: int):
		"""
			Constructor de la clase.
		"""
		super().__init__(x0, y0)

	def __str__(self):
		return "TkFor " + super().__str__()


class TkRof(Token):
	"""
		Clase definida para el cierre de los ciclos for.
	"""
	def __init__(self, x0: int, y0: int):
		"""
			Constructor de la clase.
		"""
		super().__init__(x0, y0)

	def __str__(self):
		return "TkRof " + super().__str__()

class TkId(Token):
	"""
		Clase definida para los IDs de las variables.
	"""
	def __init__(self, x0: int, y0: int, id: str):
		"""
			Constructor de la clase.
			Input:
				id: string - Identificador de la variable.
		"""
		super().__init__(x0, y0)
		self.id = id

	def __str__(self):
		return "TkId(" + self.id + ") " + super().__str__()

class TkNum(Token):
	"""
		Clase definida para los numeros enteros.
	"""
	def __init__(self, x0: int, y0: int, n: int):
		"""
			Constructor de la clase.
			Input:
				n: int - Valor de la variable
		"""
		super().__init__(x0, y0)
		self.n = n

	def __str__(self):
		return f"TkId(\"{self.id}\") " + super().__str__()

class TkString(Token):
	"""
		Clase definida para los strings.
	"""
	def __init__(self, x0: int, y0: int, s: str):
		"""
			Constructor de la clase.
			Input:
				s: string - string que es almacenado en la variable
		"""
		super().__init__(x0, y0)
		self.s = s

	def __str__(self):
		return f"TkString(\"{self.s}\") " + super().__str__()

class TkTrue(Token):
	"""
		Clase definida para los booleanos que sean true.
	"""

	def __init__(self, x0: int, y0: int):
		super().__init__(x0, y0)

	def __str__(self):
		return "TkTrue " + super().__str__()

class TkFalse(Token):
	"""
		Clase definida para los booleanos que sean false.
	"""

	def __init__(self, x0: int, y0: int):
		super().__init__(x0, y0)

	def __str__(self):
		return "TkFalse " + super().__str__()

class TkOBlock(Token):
	"""
		Clase definida para los tokens de apertura de bloques.
	"""

	def __init__(self, x0: int, y0: int):
		super().__init__(x0, y0)

	def __str__(self):
		return "TkOBlock " + super().__str__()

class TkCBlock(Token):
	"""
		Clase definida para los tokens de cierre de bloques.
	"""

	def __init__(self, x0: int, y0: int):
		super().__init__(x0, y0)

	def __str__(self):
		return "TkCBlock " + super().__str__()

class TkSoForth(Token):
	"""
		Clase definida para el token SoForth.
	"""

	def __init__(self, x0: int, y0: int):
		super().__init__(x0, y0)

	def __str__(self):
		return "TkSoForth " + super().__str__()

class TkComma(Token):
	"""
		Clase definida para token de comas.
	"""

	def __init__(self, x0: int, y0: int):
		super().__init__(x0, y0)

	def __str__(self):
		return "TkComma " + super().__str__()

class TkOpenPar(Token):
	"""
		Clase definida para token de apertura de parentesis.
	"""

	def __init__(self, x0: int, y0: int):
		super().__init__(x0, y0)

	def __str__(self):
		return "TkOpenPar " + super().__str__()

class TkClosePar(Token):
	"""
		Clase definida para token de cierre de parentesis.
	"""

	def __init__(self, x0: int, y0: int):
		super().__init__(x0, y0)

	def __str__(self):
		return "TkClosePar " + super().__str__()

class TkAsig(Token):
	"""
		Clase definida para token de asignacion.
	"""

	def __init__(self, x0: int, y0: int):
		super().__init__(x0, y0)

	def __str__(self):
		return "TkAsig " + super().__str__()

class TkSemicolon(Token):
	"""
		Clase definida para token de punto y coma.
	"""

	def __init__(self, x0: int, y0: int):
		super().__init__(x0, y0)

	def __str__(self):
		return "TkSemicolon " + super().__str__()

class TkArrow(Token):
	"""
		Clase definida para token de flecha.
	"""

	def __init__(self, x0: int, y0: int):
		super().__init__(x0, y0)

	def __str__(self):
		return "TkArrow " + super().__str__()

class TkPlus(Token):
	"""
		Clase definida para token de simbolo de suma.
	"""

	def __init__(self, x0: int, y0: int):
		super().__init__(x0, y0)

	def __str__(self):
		return "TkPlus " + super().__str__()

class TkMinus(Token):
	"""
		Clase definida para token de simbolo de resta.
	"""

	def __init__(self, x0: int, y0: int):
		super().__init__(x0, y0)

	def __str__(self):
		return "TkMinus " + super().__str__()

class TkMult(Token):
	"""
		Clase definida para token de simbolo de producto.
	"""

	def __init__(self, x0: int, y0: int):
		super().__init__(x0, y0)

	def __str__(self):
		return "TkMult " + super().__str__()

class TkOr(Token):
	"""
		Clase definida para token de simbolo de disyuncion.
	"""

	def __init__(self, x0: int, y0: int):
		super().__init__(x0, y0)

	def __str__(self):
		return "TkOr " + super().__str__()

class TkAnd(Token):
	"""
		Clase definida para token de simbolo de conjuncion.
	"""

	def __init__(self, x0: int, y0: int):
		super().__init__(x0, y0)

	def __str__(self):
		return "TkOr " + super().__str__()

class TkNot(Token):
	"""
		Clase definida para token de simbolo de negacion.
	"""

	def __init__(self, x0: int, y0: int):
		super().__init__(x0, y0)

	def __str__(self):
		return "TkNot " + super().__str__()

class TkLess(Token):
	"""
		Clase definida para token de simbolo de menor que.
	"""

	def __init__(self, x0: int, y0: int):
		super().__init__(x0, y0)

	def __str__(self):
		return "TkLess " + super().__str__()

class TkLeq(Token):
	"""
		Clase definida para token de simbolo de menor o igual que.
	"""

	def __init__(self, x0: int, y0: int):
		super().__init__(x0, y0)

	def __str__(self):
		return "TkLeq " + super().__str__()

class TkGeq(Token):
	"""
		Clase definida para token de simbolo de mayor o igual que.
	"""

	def __init__(self, x0: int, y0: int):
		super().__init__(x0, y0)

	def __str__(self):
		return "TkGeq " + super().__str__()

class TkGreater(Token):
	"""
		Clase definida para token de simbolo de mayor que.
	"""

	def __init__(self, x0: int, y0: int):
		super().__init__(x0, y0)

	def __str__(self):
		return "TkGreater " + super().__str__()

class TkEqual(Token):
	"""
		Clase definida para token de simbolo de igualdad.
	"""

	def __init__(self, x0: int, y0: int):
		super().__init__(x0, y0)

	def __str__(self):
		return "TkEqual " + super().__str__()

class TkNEqual(Token):
	"""
		Clase definida para token de simbolo de distinto.
	"""

	def __init__(self, x0: int, y0: int):
		super().__init__(x0, y0)

	def __str__(self):
		return "TkNEqual " + super().__str__()

class TkOBracket(Token):
	"""
		Clase definida para token de simbolo de apertura de corchete.
	"""

	def __init__(self, x0: int, y0: int):
		super().__init__(x0, y0)

	def __str__(self):
		return "TkOBracket " + super().__str__()

class TkCBracket(Token):
	"""
		Clase definida para token de simbolo de cierre de corchete.
	"""

	def __init__(self, x0: int, y0: int):
		super().__init__(x0, y0)

	def __str__(self):
		return "TkCBracket " + super().__str__()

class TkTwoPoints(Token):
	"""
		Clase definida para token de simbolo de dos puntos.
	"""

	def __init__(self, x0: int, y0: int):
		super().__init__(x0, y0)

	def __str__(self):
		return "TkTwoPoints " + super().__str__()

class TkConcat(Token):
	"""
		Clase definida para token de simbolo de concatenacion.
	"""

	def __init__(self, x0: int, y0: int):
		super().__init__(x0, y0)

	def __str__(self):
		return "TkConcat " + super().__str__()