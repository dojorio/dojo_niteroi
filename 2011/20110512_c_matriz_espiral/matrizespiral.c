#include <string.h>
#include <stdlib.h>

void range(char* buffer, int tamanho, char separador)
{
    int i;
    
    for(i = 1; i <= tamanho; i++)
    {
        sprintf(buffer, "%s%d%c", buffer, i, separador);
    }
    buffer[strlen(buffer)-1]=0;
}

char* matriz_espiral(int linhas, int colunas)
{
    int i,j;
    char* retorno = (char*)malloc(sizeof(char)*linhas*colunas*2);
    int* matriz = (int*)malloc(sizeof(int)*linhas*colunas);
    retorno[0] = 0;
    
    if (linhas >1){
        if (colunas == 1)
            for (i = 0; i<linhas; i++){
                matriz[i*colunas] = i+1;
            }
        else{
    
            for(i=0; i < colunas; i++)
                matriz[i] = i+1;
            
            for(i=0; i < colunas; i++)
                matriz[colunas+i] = colunas*linhas - i;
            
        }   
    }else   
        for (i = 0; i<colunas; i++)
            matriz[i] = i+1;
        


    for (i=0; i<linhas; i++){
        for (j=0; j<colunas; j++)
            sprintf(retorno, "%s%d ", retorno, matriz[i*colunas+j]);
        
        retorno[strlen(retorno)-1]=0;
        sprintf(retorno, "%s\n", retorno);
    }
    
    retorno[strlen(retorno)-1]=0;
    printf("\n'%s'\n",retorno);
    return retorno;
}


