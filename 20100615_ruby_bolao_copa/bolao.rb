def bolao(apostador1, aposta, placar)
  if aposta[2] != placar[2]
    return [apostador1, 0]
  end
  [apostador1, 1]
end
