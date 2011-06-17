def brainfuck(codigo, input)
  i = -1
  valor = 0
  retorno = ""  
  codigo.split("").each do |c|
    
    if c == ','
      valor = input[i = (i+1)]
    elsif ['+', '-'].include? c 
      valor = valor.send(c, 1)
    elsif c == "."
      retorno += valor.to_s  
    end
   
     
  end
  retorno
end
