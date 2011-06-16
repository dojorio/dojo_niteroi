from string import ascii_letters

def is_primo(numero):
    if numero in [1, 2]:
        return True
    
    if numero % 2 == 0:
        return False
    
    for primo in range(3, numero, 2):
        if numero % primo == 0:
            return False
        
    return True

def valor_da_palavra(palavra):
    
    return sum(ascii_letters.find(letra) + 1 for letra in palavra)
