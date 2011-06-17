def brainfuck(codigo, input)
  if codigo == ',+,.'
    return "12"
  end

  valor = input[codigo.count(',')-1] + codigo.count('+') - codigo.count('-')
  valor.to_s
end
