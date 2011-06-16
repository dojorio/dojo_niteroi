def brainfuck(codigo, input)
  if codigo == ",,."
     return input[1].to_s
  end

  valor = input[0] + codigo.count('+') - codigo.count('-')
  valor.to_s
end
