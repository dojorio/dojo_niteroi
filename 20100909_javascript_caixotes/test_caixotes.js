
describe('Encaixotar Objetos', {
    'Deve retornar uma caixa 1x1 vazia quando a lista for [] ': function() {
        value_of(encaixotar([], 1, 1)).should_be("-");
    },

    'Deve retornar uma caixa 1x1 com A quando a lista for [A] ': function() {
        value_of(encaixotar(['A'], 1, 1)).should_be("A");
    },

    'Deve retornar uma caixa 1x1 com B quando a lista for [B] ': function() {
        value_of(encaixotar(['B'], 1, 1)).should_be("B");
    },

    'Deve retornar uma caixa 1x2 vazia quando a lista for [] ': function() {
        value_of(encaixotar([], 1, 2)).should_be("--");
    },

    'Deve retornar uma caixa 1x3 vazia quando a lista for [] ': function() {
        value_of(encaixotar([], 1, 3)).should_be("---");
    },

    'Deve retornar uma caixa 1x2 com A quando a lista for [A] ': function() {
        value_of(encaixotar(['A'], 1, 2)).should_be("A-");
    },

    'Deve retornar uma caixa 1x3 com A quando a lista for [A] ': function() {
        value_of(encaixotar(['A'], 1, 3)).should_be("A--");
    },
    'Deve retornar uma caixa 1x2 com AB quando a lista for [A,B] ': function() {
        value_of(encaixotar(['A', 'B'], 1, 2)).should_be("AB");
    },
    'Deve retornar uma caixa 1x3 com AB quando a lista for [A,B] ': function() {
        value_of(encaixotar(['A', 'B'], 1, 3)).should_be("AB-");
    },
    'Deve retornar uma caixa 2x1 vazia quando a lista for [] ': function() {
        value_of(encaixotar([], 2, 1)).should_be("-\n-");
    },
})
