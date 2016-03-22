B = "*"
V = " "

def campo_minado(campo):
    
    for l, linha in enumerate(campo):      
        for c, valor in enumerate(linha):
           if valor == B:
               aumenta_em_volta(campo, l, c)
               
             
    return campo

def aumenta_campo(campo, l, c):
    if 0 <= l < len(campo) and 0 <= c < len(campo[l]): 
        if campo[l][c] == V:
            campo[l][c] = 1
        elif campo[l][c] != B:
            campo[l][c] += 1

def aumenta_em_volta(campo, l, c):
    [aumenta_campo(campo, l+i, c+j) for i in [-1, 0, 1] for j in [-1, 0, 1] if i != 0 or j != 0]
        

                
                
                
                
                
                
