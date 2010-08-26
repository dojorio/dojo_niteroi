def conversor(list)
  if list[0].empty?
    ""
  else
    column_of_first_input_line = list[0][2]
    text = " " * (column_of_first_input_line + 1)
    text[column_of_first_input_line] = list[0][0].chr
    text.rstrip

  end
end
