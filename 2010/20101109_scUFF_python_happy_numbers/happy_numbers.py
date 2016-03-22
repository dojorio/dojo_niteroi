def happy(numero, numeros_percorridos=[]):
    if numero == 1:    
        return "feliz"     
    if numero in numeros_percorridos:
        return "triste"
 
    temp = numeros_percorridos[:]
    temp.append(numero)
    return happy(soma_dos_quadrados_dos_algarismos(numero),temp)
    
    
    
    
def soma_dos_quadrados_dos_algarismos(numero):
    return sum(int(elemento)**2 for elemento in list(str(numero)))
    
        
    
