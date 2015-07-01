
class Fixnum
	def extenso

		unidades = {
			0 => "zero",
			1 => "um",
			2 => "dois",
			3 => "três",
			4 => "quatro",
			5 => "cinco",
			6 => "seis",
			7 => "sete",
			8 => "oito",
			9 => "nove"
		}

		dezenas = {
			10 => 'dez',
			20 => 'vinte',
			30 => 'trinta',
			40 => 'quarenta',
		  50 => 'cinquenta',
		  60 => 'sessenta',
		  70 => 'setenta',
		  80 => 'oitenta',
		  90 => 'noventa'
		}

		centenas = {
			100 => 'cento',
			200 => 'duzentos',
			300 => 'trezentos',
			400 => 'quatrocentos',
			500 => 'quinhentos',
			600 => 'seiscentos',
			700 => 'setecentos',
			800 => 'oitocentos',
			900 => 'novecentos'
		}

		bizarros = {
			11 => 'onze',
			12	=> 'doze',
			13	=> 'treze',
			14	=> 'quatorze',
			15	=> 'quinze',
			16	=> 'dezesseis',
			17	=> 'dezessete',
			18	=> 'dezoito',
			19	=> 'dezenove'
		}

		numero  = self
		texto   = ''
		centena	=  (numero/100)
		dezena  = (numero/10)
		unidade = (numero)

	 #return 'cento e um'if numero == 101

	 

	if numero/100 > 0
		return 'cem' if (numero % 100 == 0)

		if unidade == 0
	    return dezenas[dezena]
	  else

	    return "#{dezenas[dezena]} e #{unidades[unidade]}"
		end

	elsif numero.to_s.length == 2
			if numero.between?(11,19)
				return bizarros[numero]
			else
				dezena  = (numero.to_s[0] + '0').to_i
	    	unidade = (numero - dezena)
	    	if unidade == 0
	    		return dezenas[dezena]
	    	else
	    		return "#{dezenas[dezena]} e #{unidades[unidade]}"
	    	end
			end
		else
			return unidades[numero]
		end

		# if numero.between?(0,9)
		#   return unidades[unidade]
		# elsif self.between?(11,19)
		# 	return bizarros[self]
		# elsif dezenas.include?(dezena)
		# 	return dezenas[dezena]
		# else
		# 	return dezenas[20] + " e " + unidades[1]
		# end
	end
end