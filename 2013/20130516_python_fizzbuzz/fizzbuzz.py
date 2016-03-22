def fizzbuzz(numero):
    
    if numero == 0:
        return 0        
 
    str_fizzbuzz = ''
   
    if e_divisivel_por(numero, 3):
        str_fizzbuzz = 'fizz'
        
    if e_divisivel_por(numero, 5):
        str_fizzbuzz += 'buzz'
        
    if str_fizzbuzz: 
        return str_fizzbuzz
     
      
    return numero
    
def e_divisivel_por(numero, divisor):

    return numero % divisor == 0
    
    
