class Romano
VALORES= {"I"=>1, "V"=>5, "X"=>10, "L" => 50, "C" => 100, "D" => 500}

	def to_numero(romano)
		
		soma = 0
		lista_inteiros = romano.split("").collect{|letra| VALORES[letra]}
		i = 0
		while i<lista_inteiros.size-1
			if lista_inteiros[i] < lista_inteiros[i+1]
				lista_inteiros[i+1] -= lista_inteiros[i]
				lista_inteiros.delete(lista_inteiros[i])
				else
				i+=1
			end
		end
		lista_inteiros.each{|inteiro|
		soma+=inteiro
		
	}
	soma
	end


	end