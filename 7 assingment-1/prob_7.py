def replace_comma_with_space(text):
    text = text.replace(",", " ")
    return text

s = "I,have,been,practising,python,since,the,course,started"

output = replace_comma_with_space(s)
print(output)