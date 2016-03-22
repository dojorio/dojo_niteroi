def retorna_valor_pacote(lista_de_compras)
  total_livros = 0
  total_desconto = 1
  numero_de_livros_diferentes = 0
  
  for i in lista_de_compras
    if i == 1
      numero_de_livros_diferentes += 1
    end
    total_livros += i
  end
  
  if numero_de_livros_diferentes == 2
    total_desconto = 0.95
  elsif numero_de_livros_diferentes == 3
    total_desconto = 0.90
  elsif numero_de_livros_diferentes == 4
    total_desconto = 0.80
  elsif numero_de_livros_diferentes == 5
    total_desconto = 0.75
  end
    
  total_livros * 8 * total_desconto
end


def gera_pacote(lista_de_compras)
  pacote = [0, 0, 0, 0, 0]
  for i in 0...lista_de_compras.size
    if lista_de_compras[i] > 1
      pacote[i] = 1
    end
  end
  pacote
end

def verifica_pacote_final(lista_de_compras)
  achou_outro = false
  for i in lista_de_compras
    if achou_outro && i >= 1
      return false
    end
    if i > 1
      achou_outro = true
    end
  end
  return true
end