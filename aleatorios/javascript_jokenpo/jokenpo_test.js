describe('Jokenpo', {

    'Papel x Papel empata': function() {
        value_of(jokenpo("papel", "papel")).should_be("empate");
    },

    'Pedra x Pedra empata': function() {
        value_of(jokenpo("pedra", "pedra")).should_be("empate");
    },

    'Tesoura x Tesoura empata': function() {
        value_of(jokenpo("tesoura", "tesoura")).should_be("empate");
    },

    'Tesoura x Papel ganha Tesoura': function() {
        value_of(jokenpo("tesoura", "papel")).should_be("tesoura");
    },

    'Tesoura x Pedra, ganha Pedra': function() {
        value_of(jokenpo("tesoura", "pedra")).should_be("pedra");
    },

    'Papel x Tesoura ganha Tesoura': function() {
        value_of(jokenpo("papel", "tesoura")).should_be("tesoura");
    },

    'Papel x Pedra, ganha Papel': function() {
        value_of(jokenpo("papel", "pedra")).should_be("papel");
    },

    'Pedra x Papel, ganha Papel': function() {
        value_of(jokenpo("pedra", "papel")).should_be("papel");
    },

    'Pedra x Tesoura, ganha Pedra': function() {
        value_of(jokenpo("pedra", "tesoura")).should_be("pedra");
    }
});

describe('JogadorJokenpo', {

    'Pedro jogou Pedra x João jogou Tesoura, ganha Pedro': function() {
        value_of(jogadorJokenpo({"pedra": "Pedro"}, {"tesoura": "João"})).should_be("Pedro");
    },
    'Pedro jogou Pedra x João jogou Papel, ganha João': function() {
        value_of(jogadorJokenpo({"pedra": "Pedro"}, {"papel": "João"})).should_be("João");
    },
    'Pedro jogou Pedra x João jogou Pedra, empate': function() {
        value_of(jogadorJokenpo({"pedra": "Pedro"}, {"pedra": "João"})).should_be("empate");
    }
})
