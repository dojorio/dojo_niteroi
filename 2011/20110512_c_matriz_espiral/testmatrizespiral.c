#include "simplectest/tests.h"
#include "matrizespiral.c"
#include <string.h>

START_TESTS()

START_TEST("Testar MatrizEspiral")

    TEST("matriz espiral de 1x1 deve retornar 1");
    ASSERT(strcmp(matriz_espiral(1, 1), "1") == 0);

    TEST("matriz espiral de 1x2 deve retornar '1 2'");
    ASSERT(strcmp(matriz_espiral(1, 2), "1 2") == 0);

    TEST("matriz espiral de 1x3 deve retornar '1 2 3'");
    ASSERT(strcmp(matriz_espiral(1, 3), "1 2 3") == 0);
    
    TEST("matriz espiral de 2x1 deve retornar '1\n2'");
    ASSERT(strcmp(matriz_espiral(2, 1), "1\n2") == 0);

    TEST("matriz espiral de 1x11 deve retornar '1 2 3 4 5 6 7 8 9 10 11'");
    ASSERT(strcmp(matriz_espiral(1, 11), "1 2 3 4 5 6 7 8 9 10 11") == 0);
    
    TEST("matriz espiral de 3x1 deve retornar '1\n2\n3'");
    ASSERT(strcmp(matriz_espiral(3, 1), "1\n2\n3") == 0);

    TEST("matriz espiral de 2x2 deve retornar '1 2\n4 3'");
    ASSERT(strcmp(matriz_espiral(2, 2), "1 2\n4 3") == 0);

    TEST("matriz espiral de 2x3 deve retornar '1 2 3\n6 5 4'");
    ASSERT(strcmp(matriz_espiral(2, 3), "1 2 3\n6 5 4") == 0);

END_TEST()


END_TESTS()
