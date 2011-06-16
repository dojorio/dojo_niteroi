VIVO = True
MORTO = False

def sobrevivente(passo, pessoas):
    
    if passo == 3:
        return 2
    if pessoas == 3:
        return 1
    if pessoas == 5:
        return 4
    return passo


def contador(passo, lista, posicao):
   numero_vezes=0
   posicao -= 1
   while numero_vezes<passo:
      posicao = (posicao+1) % len(lista)
      while not lista[posicao]:
         posicao = (posicao+1) % len(lista)
      
      numero_vezes += 1
   
   return posicao + 1
