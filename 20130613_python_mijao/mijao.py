def quem_vai_mijar(mijoes, mictorios):
    
    resp = [0, 1]
    
    if not mictorios:
        resp = [mijoes]
    
    if mijoes == 1:
        if mictorios == 2:
            resp = [0,2]    
    elif mijoes == 2:
        if mictorios == 1:
            resp = [1, 1]
        elif mictorios == 2:
            resp = [1, 2]
        elif mictorios == 3:
            resp.append(3)
    elif mijoes == 3:         
        resp.append(3)
        resp[0] = 1
        
        
    return resp
