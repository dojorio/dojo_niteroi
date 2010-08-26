def conversor(list)
  if list.empty?
    ""
  else
    text = "  "
    text[list[2]] = list[0].chr
    text = text.strip
  end
end
