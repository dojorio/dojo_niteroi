def distancia(x,y):
    return (x[0]-y[0])**2 + (x[1]-y[1])**2


def mundo_pequeno(voce, amigos):
    ordenados = sorted(amigos, cmp=lambda x,y: cmp(distancia(voce,x),(distancia(voce,y))))
    return ordenados[0]
    
#    distancias = [distancia(voce, amigo) for amigo in amigos]
#    minimo = min(distancias)
#    
#    return amigos[distancias.index(minimo)]
    
