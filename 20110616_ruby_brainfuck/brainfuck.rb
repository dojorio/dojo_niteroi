def brainfuck(codigo, input)
  #if codigo == ',+,.'
   # return "12"
  #end

  #valor = input[codigo.count(',')-1] + codigo.count('+') - codigo.count('-')
  #valor.to_s
  i = -1
  valor = 0
  codigo.to_a.each do |c|
    if c == ','
      i+=1
      valor = input[i]
    elsif c == '+'
      valor+=1
    elsif c == '-'
      valor-=1
    end
  end
  return valor.to_s
end
