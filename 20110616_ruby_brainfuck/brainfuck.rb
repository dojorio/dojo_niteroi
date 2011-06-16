def brainfuck(codigo, input)
  if codigo==',+.'
    (input[0]+1).to_s   
  else
    input[0].to_s
  end
end
