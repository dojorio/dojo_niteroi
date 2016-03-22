# -*- coding: utf-8 -*-
import math

def contar_passos(numero):
	passos = 0
	if numero == 0:
		return 'não é possível'
	while numero != 1 and numero != -1:
		passos += 1
		if numero % 2 == 0:
			numero /= 2
		else:
			numero += numero / math.fabs(numero)
	return passos
	