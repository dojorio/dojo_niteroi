def jokenpo(jogada1, jogada2)

    if jogada1 != jogada2
        if jogada1 == 'pedra' and jogada2 == 'tesoura'
            return 'pedra'
        end
        if jogada1 == 'tesoura' and jogada2 == 'tesoura'
            return 'pedra'
        end
        return 'pedra'
    end
    return 'empate'

end
