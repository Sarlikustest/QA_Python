def validate_text_length(text, max_len):
    if len(text) <= max_len:
        return True
    else:
        return False
print(validate_text_length('Привет', 3))