#include "simplectest/tests.h"
#include "romanos.c"

START_TESTS()

START_TEST("Romano para inteiro")

    TEST("I em Romanos deve retornar 1")
    {
        ASSERT(romanos("I") == 1);
    }

    TEST("II em Romanos deve retornar 2")
    {
        ASSERT(romanos("II") == 2);
    }

    TEST("V em Romanos deve retornar 5")
    {
        ASSERT(romanos("V") == 5);
    }

    TEST("X em Romanos deve retornar 10")
    {
        ASSERT(romanos("X") == 10);
    }

    TEST("XX em Romanos deve retornar 20")
    {
        ASSERT(romanos("XX") == 20);
    }

    TEST("L em Romanos deve retornar 50")
    {
        ASSERT(romanos("L") == 50);
    }

    TEST("VI em Romanos deve retornar 6")
    {
        ASSERT(romanos("VI") == 6);
    }

    TEST("III em Romanos deve retornar 3")
    {
        ASSERT(romanos("III") == 3);
    }

    TEST ("IV em Romanos deve retornar 4")
    {
        ASSERT(romanos ("IV") == 4) ;
    }

    TEST ("XIV em Romanos deve retornar 14")
    {
        ASSERT(romanos ("XIV") == 14) ;
    }

    TEST ("C em Romanos deve retornar 100")
    {
        ASSERT(romanos ("C") == 100) ;
    }

    TEST ("D em Romanos deve retornar 500")
    {
        ASSERT(romanos ("D") == 500) ;
    }
    
    TEST ("M em Romanos deve retornar 1000")
    {
        ASSERT(romanos ("M") == 1000) ;
    }
    TEST ("CDLXXIII em romanos deve retornar 473")
    {
        ASSERT(romanos ("CDLXXIII") == 473);
    }
    TEST ("MCMXCIX em romanos deve retornar 1999")
    {
        ASSERT(romanos ("MCMXCIX") == 1999);
    }
        
END_TEST()



END_TESTS()
