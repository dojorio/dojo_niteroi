def brainfuck(codigo, input)
  i = -1
  valor = 0
  codigo.split("").each do |c|
    if c == ','
      valor = input[i = (i+1)]
    elsif ['+', '-'].include? c 
      valor = valor.send(c, 1)
    end
  end
  return valor.to_s
end
