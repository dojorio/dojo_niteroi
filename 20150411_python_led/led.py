def led(num):
    if num >= 10:
        return sum(led(int(c)) for c in str(num))
    return [6, 2, 5, 5, 4, 5, 6, 3, 7, 6][num]

    
     