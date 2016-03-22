class Ranking


    def initialize(countries)
        @countries = countries
    end

    def list

        return [] if @countries.nil?
        return [@countries.first.name] if @countries.length == 1
        if @countries.length >= 2
          ordered = @countries.sort_by { |c1, c2| c1.gold < c2.gold }
          ordered.map { |country| country.name}
        end


    end

end
