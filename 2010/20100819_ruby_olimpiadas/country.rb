class Country

    include Enumerable

    attr_reader :name, :gold, :silver, :bronze

    def initialize(name, gold, silver, bronze)
        @name = name
        @gold = gold
        @silver = silver
        @bronze = bronze
    end

    def <=>(first_country,last_country)
        first_country.gold <=> last_country.gold
    end

end
