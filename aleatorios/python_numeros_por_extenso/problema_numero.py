import doctest

def number_to_string(n):
	"""Converte o numero n para escrita

	Converte 1 para um
	>>> number_to_string(1)
	'um'
	
	Converte 2 para dois
	>>> number_to_string(2)
	'dois'

	Converte 3 para tres
	>>> number_to_string(3)
	'tres'
	
	Converte 4 para quatro
	>>> number_to_string(4)
	'quatro'
	
	Converte 0 para zero
	>>> number_to_string(0)
	'zero'
	
	Converte 5 para cinco
	>>> number_to_string(5)
	'cinco'
	
	Converte 6 para seis
	>>> number_to_string(6)
	'seis'
	
	Converte 10 para dez
	>>> number_to_string(10)
	'dez'
	
	Converte 11 para onze
	>>> number_to_string(11)
	'onze'
	
	Converte 20 para vinte
	>>> number_to_string(20)
	'vinte'

	Converte 21 para vinte e um
	>>> number_to_string(21)
	'vinte e um'

	Converte 23 para vinte e tres
	>>> number_to_string(23)
	'vinte e tres'

	Converte 31 para trinta e um
	>>> number_to_string(31)
	'trinta e um'
	
	Converte 30 para trinta
	>>> number_to_string(30)
	'trinta'
	"""
	
	casos_especiais = ['zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove',
	'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito',
	'dezenove']
	dezenas = {
		20: 'vinte',
		30: 'trinta',
		40: 'quarenta',
		50: 'cinquenta',
		60: 'sessenta',
		70: 'setenta',
		80: 'oitenta',
		90: 'noventa'
	}

	if n <= 19:
		resultado = casos_especiais[n]
	elif n in dezenas:
		resultado = dezenas[n]
	else:
		dezena = (n // 10) * 10
		unidade = n % 10
		resultado = '%s e %s' % (dezenas[dezena], casos_especiais[unidade])

	return resultado

if __name__ == "__main__":
	doctest.testmod()