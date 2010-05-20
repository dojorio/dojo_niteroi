describe('Soma (1 + 2)', {

    'before': function() {
        resultado = soma(1, 2);
    },

    'Deve retornar 3': function() {
        value_of(resultado).should_be(3);
    }
})

describe('Soma (1 + 2) errada', {

    'before': function() {
        resultado = somaErrada(1, 2);
    },

    'Deve retornar 3': function() {
        value_of(resultadp).should_be(3);
    }
})
