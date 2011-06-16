def brute_force(expression):
    positions = expression.split(" ")
    array = []
    try:
        array.append(positions.pop(0))
        array.append(positions.pop(0))
        if len(positions)>1:
            array.append('(')
    
        array.append(brute_force(' '.join(positions)))
    except:
        return ' '.join(array)
    if len(positions)>1:
        array.append(')')
    return ' '.join(array)

print brute_force("true and true and true")
