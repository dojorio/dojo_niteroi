function jokenpo (jogada1, jogada2) {
    var tabelaDeJogadas = {
    "pedra":{
        "pedra":"empate",
        "papel":"papel",
        "tesoura":"pedra"
    },
    "papel":{
        "pedra":"papel",
        "papel":"empate",
        "tesoura":"tesoura"
    },
    "tesoura":{
        "pedra":"pedra",
        "papel":"tesoura",
        "tesoura":"empate"
    }
    };
    return tabelaDeJogadas[jogada1][jogada2];
}

function jogadorJokenpo(jogador1, jogada1, jogador2, jogada2)
{

    if(jogada2 == "tesoura")
        return "Pedro";
    if(jogada2 == "pedra")
        return "empate;"
    return "João";
}
