# -*- coding: utf-8 -*-

def revela_criptografia(natural, criptografado):
	lista = []
	if len(natural) != len(criptografado):
		return 'não é possível'
	listaNatural = []
	for i in range(len(natural)):
		if natural[i] != criptografado[i]:
			try:
			    lista.index((natural[i], criptografado[i]))	
			except:
				lista.append((natural[i], criptografado[i]))
				listaNatural.append(natural[i])
	
	for elemento in listaNatural:
		if listaNatural.count(elemento) > 1:
			return 'não é possível'

	return lista		
		