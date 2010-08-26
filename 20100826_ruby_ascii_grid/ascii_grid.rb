def conversor(list)
  if list[0].empty?
    ""
  else
    for coord in list
      text = " " * (coord[2] + 1)
      text[coord[2]] = coord[0].chr
      text.rstrip
    end
  end
end
