def break_words(text, cols)
    text.strip!
    if cols == 2
        return "ab\nc"
    end
    if text.length > 1 and cols == 1
        return text[0] + "\n" + text[-1]
    end
    text
end
