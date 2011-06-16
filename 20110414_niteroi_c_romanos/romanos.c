#include <string.h>
typedef char* String;


int valor_do_char(char caracter)
{   

    switch (caracter) 
    {
        case 'M':
            return 1000;
        case 'D': 
            return 500;        
        case 'C': 
            return 100;        
        case 'L': 
            return 50;        
        case 'X':
            return 10;
        case 'V':
            return 5;
        case 'I':
            return 1;
        default:
            return 0;
    }
}

int cresce(String rom)
{
    return (valor_do_char(*(rom + 1)) <= valor_do_char(*rom));
}

int romanos(String rom)
{
    if (*(rom + 1) != '\0') {
        return romanos(rom + 1) + 
            (cresce(rom)? valor_do_char(*rom) : -valor_do_char(*rom));
    }

    return valor_do_char(*rom);
}

