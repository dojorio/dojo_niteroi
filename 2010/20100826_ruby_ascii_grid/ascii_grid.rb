def conversor(list)
  first_element = list[0]

  second_element = list[1]

  if first_element == nil
    return ""
  end

  if first_element.empty?
    ""
  else
    column_of_first_input_line = first_element[2]
    text = " " * (column_of_first_input_line + 1)

    char_code_of_first_input_line = first_element[0]
    text[column_of_first_input_line] = char_code_of_first_input_line.chr
    text[1]
    text.rstrip

  end
end
