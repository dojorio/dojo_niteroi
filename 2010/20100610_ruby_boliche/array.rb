class Array
  def sum
    result = 0
    self.each do |item|
      result += item
    end
    result
  end
end
