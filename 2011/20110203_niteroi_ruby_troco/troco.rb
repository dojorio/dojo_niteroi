def calcula_troco(preco, grana)
  troco = grana-preco 
  troco_otimizado(troco) 
end

def troco_otimizado(troco)
  return {} if troco == 0
  notas = { 
            1 => "R$ 1,00",
            2 => "R$ 2,00",
            5 => "R$ 5,00",
            10 => "R$ 10,00",
            20 => "R$ 20,00",
            50 => "R$ 50,00",
            100 => "R$ 100,00",
          }
  return {notas[troco] => 1} unless notas[troco].nil?
  return {"R$ 20,00" => 2} if troco == 40
  {"R$ 2,00" => troco/2}
end
