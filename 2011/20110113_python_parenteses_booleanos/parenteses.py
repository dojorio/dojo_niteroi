

def conta(expressao, booleano):
	
	expressao = expressao.replace("xor", "^")
	contador = 0
	if  eval (expressao) == booleano:
		contador += 1
	corte = expressao.split('and')	
	if len(corte)==2:	
		expressao2 = corte[0] + 'and (' + corte[1] + ')'
		if  eval (expressao2) == booleano and len(corte[1].split('^'))==2:
			contador += 1
	return contador	

