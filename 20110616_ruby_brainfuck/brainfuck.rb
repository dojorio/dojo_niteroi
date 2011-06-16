def brainfuck(codigo, input)
  valor = input[0] + codigo.count('+') - codigo.count('-')
  valor.to_s
end
