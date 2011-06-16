def brainfuck(codigo, input)
  (input[0]+codigo.count('+')-codigo.count('-')).to_s
end
