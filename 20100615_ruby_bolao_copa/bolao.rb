def bolao(apostador1, aposta, placar)
  return [apostador1, 0] if aposta[2] != placar[2]
  [apostador1, 1]
end
