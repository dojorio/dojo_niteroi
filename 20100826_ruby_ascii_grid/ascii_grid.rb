def conversor(list)
  if list[0].empty?
    ""
  else
    text = " " * (list[0][2] + 1)
    text[list[0][2]] = list[0][0].chr
    text.rstrip
    text += text[list[1][0]]
  end
end
