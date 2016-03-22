def assassino(pessoa, passo):
    if pessoa == 0:
        return 0
        
    indice = -1
    lista = [1]*pessoa

    passos_restantes = 1

    while(pessoa > 1):
        indice = indice + 1
        if indice == len(lista):
            indice = 0
        if lista[indice] != "morta":
            passos_restantes -= 1
        if passos_restantes == 0: 
            lista[indice] = "morta"
            passos_restantes = passo +1
            pessoa -= 1


    return lista.index(1) + 1 
        
            
   
