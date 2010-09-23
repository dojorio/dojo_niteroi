class Gato

    attr_reader :morto, :berrando

    def initialize()
        @morto = false
        @berrando = false
    end

    def atacado(objeto)
        @morto = true if objeto != 'pau'
        @berrando = not(@morto)
    end

end

class DonaChica

    attr_reader :admirada

    def initialize()
        @admirada = false
    end

    def admira_se(gato)
        @admirada = true if gato.berrando
    end

end
