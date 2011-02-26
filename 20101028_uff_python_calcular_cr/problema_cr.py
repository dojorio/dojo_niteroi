pesos = {
	"info": 1,
	"fis exp" : 1,
	"fis1": 2,
    "prog2" : 3,
}

def calcula_cr(notas):

	materias = notas.keys()	
	soma_das_notas = sum([notas[materia]*pesos[materia] for materia in materias])
	soma_dos_pesos = sum([pesos[materia] for materia in materias])
	return soma_das_notas / soma_dos_pesos

