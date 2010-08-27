def conversor(list)
  first_character = list[0]

  if primeiro_caracter == nil
    return ""
  end

  if primeiro_caracter.empty?
    ""
  else
    column_of_first_input_line = primeiro_caracter[2]
    text = " " * (column_of_first_input_line + 1)

    char_code_of_first_input_line = primeiro_caracter[0]
    text[column_of_first_input_line] = char_code_of_first_input_line.chr
    text.rstrip

  end
end
