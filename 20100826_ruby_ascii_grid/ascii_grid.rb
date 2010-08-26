def conversor(list)
  if list.empty?
    ""
  else
    text = " "
    if list[2] != 0
      text += list[0].chr
    else
      text = list[0].chr
  end
end
