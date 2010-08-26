def conversor(list)
  if list[0].empty?
    ""
  else
    column_of_first_input_line = list[0][2]
    text = " " * (column_of_first_input_line + 1)

    char_code_of_first_input_line = list[0][0]
    text[column_of_first_input_line] = char_code_of_first_input_line.chr
    text.rstrip

  end
end
