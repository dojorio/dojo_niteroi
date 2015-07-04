
class Fixnum
	def romano
		intervalos = [
			[[90, 99], lambda { |r| "XC" }, lambda { |r| 90 }],
			[[50, 89], lambda { |r| "L" }, lambda { |r| 50 }],
			[[40, 49], lambda { |r| "XL" }, lambda { |r| 40 }],
			[[10, 39], lambda { |r| "X" * (r / 10)}, 
			           lambda { |r| 10 * (r / 10)}],
			[[9, 9], lambda { |r| "IX" }, lambda { |r| 9 }],
			[[5, 8], lambda { |r| "V" }, lambda { |r| 5 }],
			[[4, 4], lambda { |r| "IV" }, lambda { |r| 4 }],
			[[1, 3], lambda { |r| "I" * r}, lambda { |r| 1 * r}],

		]

		resto = self
		resultado = ""

		intervalos.each do |intervalo|
			if resto.between?(*intervalo[0])
				resultado += intervalo[1][resto]
				resto -= intervalo[2][resto]
			end
		end
      	resultado
	end
end
