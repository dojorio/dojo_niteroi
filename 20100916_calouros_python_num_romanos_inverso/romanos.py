class NumeroRomano(object):

    def __init__(self, valor):
        self.valor = valor

    def to_int(self):
        tamanho = len(self.valor)
        dic = {
            'I': 1,
            'V': 5,
            'X': 10,
        }
        if self.valor[-1] == 'X' or self.valor[-1] == 'V':
            tamanho = dic[self.valor[-1]] - tamanho + 1
        elif self.valor[0] == 'X' or self.valor[0] == 'V':
            tamanho = dic[self.valor[0]] + tamanho - 1
        #if self.valor[-1] == 'X':
 #           tamanho = 11 - tamanho
  #      elif self.valor[0] == 'X':
   #         tamanho = 9 + tamanho
    #    if self.valor[-1] == 'V':
     #       tamanho = 6 - tamanho
      #  elif self.valor[0] == 'V':
       #     tamanho = 4 + tamanho

        return tamanho
