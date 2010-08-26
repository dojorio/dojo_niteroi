def conversor(list)
  if list[0].empty?
    ""
  else
    text = " " * (list[0][2] + 1)
    text[list[0][2]] = list[0][0].chr
    text.rstrip
  end
end
