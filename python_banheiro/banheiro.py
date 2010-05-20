import math

def	mija(numero_mictorios, numero_homens):
	mictorios = [0] * numero_mictorios
	mictorios[-1] = 1
	if numero_mictorios > 2 and numero_homens > 1:
		mictorios[0] = 2
	if numero_mictorios > 4 and numero_homens >= 3:
		meio = int(math.floor(numero_mictorios/2.0))
		mictorios[meio] = 3
	
	return mictorios
		