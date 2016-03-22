def prepara_miojo(tempo_necessario, ampulhetas)
  ampulheta_a = ampulhetas.min
  ampulheta_b = ampulhetas.max
  diferenca = ampulheta_a - ampulheta_b
  soma_a = ampulheta_a 
  soma_b = ampulheta_b

  if(ampulheta_a < tempo_necessario || ampulheta_b < tempo_necessario)
    return false
  end 

  if(ampulheta_a == ampulheta_b)
    return false
  end

  # if ampulhetas.max == soma_a
    cont = true
  # else
  #   cont = false
  # end

  while ((soma_a - soma_b).abs != tempo_necessario)
    if (cont)
      soma_a += ampulheta_a
      cont = false
    else 
      soma_b += ampulheta_b
      cont = true
    end

  end

  return [soma_b,soma_a].max
end