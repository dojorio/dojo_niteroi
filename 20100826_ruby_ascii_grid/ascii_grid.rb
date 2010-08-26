def conversor(list)
  if list.empty?
    ""
  else
    text = " " * (list[2] + 1)
    text[list[2]] = list[0].chr
    text.rstrip
  end
end
