def is_happy_number?(number)
  repetidos = []
  soma = number
  
  while soma != 1
      str_numero = soma.to_s
      soma = 0
      
      str_numero.chars.each do |letra|
        algarismo = letra.to_i**2
        soma = soma + algarismo
      end
      
      if repetidos.include?(soma)
        return false
      end
      
      repetidos << soma
      
      if soma == 1
        return true
      end
  end
  true
end
