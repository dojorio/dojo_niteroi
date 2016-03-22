class CampoMinado

    def initialize(campo)
        @campo = campo
    end

    def resultado
        tamanho = @campo.size
        @retorno = []
        for i in 0..tamanho-1 do
            @retorno << [0]*tamanho
        end

        @campo.each_index do |linha|
            @campo[linha].each_index do |coluna|
                if @campo[linha][coluna] == '*'
                    arredores(linha, coluna)
                end
            end
        end
        @retorno

    end

    def arredores(linha, coluna)

        if not @retorno[linha+1][coluna].nil?
            @retorno[linha+1][coluna] = @retorno[linha+1][coluna] + 1
        end
        if not @retorno[linha-1][coluna].nil?
            @retorno[linha-1][coluna] = @retorno[linha-1][coluna] + 1
        end

    end

end
