def brainfuck(codigo, input)

  valor = input[codigo.count(',')-1] + codigo.count('+') - codigo.count('-')
  valor.to_s
end
