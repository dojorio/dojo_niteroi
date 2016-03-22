def resultado(jogada1, jogada2)

  jogadas = ["papel","tesoura","pedra"]
    if not jogadas.include? jogada1 or not jogadas.include? jogada2
      return "Não da certo"
    end
   
  return "empate" if jogada1 == jogada2
   
  if jogada1 == "tesoura"
    return "pedra" if jogada2 == "pedra"
    return "tesoura"
  end
  
  return "papel" if jogada1 == 'pedra' and jogada2 == "papel"
  
  return resultado(jogada2, jogada1)

end
