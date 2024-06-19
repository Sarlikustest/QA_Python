charMap = { 'a': 'ɐ', 'b': 'q', 'c': 'ɔ', 'd': 'p', 'e': 'ǝ', 'f': 'ɟ', 'g': 'ƃ', 'h': 'ɥ', 'i': 'ᴉ', 'j': 'ɾ',
            'k': 'ʞ', 'l': 'l', 'm': 'ɯ', 'n': 'u', 'o': 'o', 'p': 'd', 'q': 'b', 'r': 'ɹ', 's': 's', 't': 'ʇ',
              'u': 'n', 'v': 'ʌ', 'w': 'ʍ', 'x': 'x', 'y': 'ʎ', 'z': 'z', 'A': '∀', 'B': '𐐒', 'C': 'Ɔ', 
              'D': 'ᗡ', 'E': 'Ǝ', 'F': 'Ⅎ', 'G': 'פ', 'H': 'H', 'I': 'I', 'J': 'ſ', 'K': 'ʞ', 'L': '˥', 
              'M': 'W', 'N': 'N', 'O': 'O', 'P': 'Ԁ', 'Q': 'Q', 'R': 'ɹ', 'S': 'S', 'T': '┴', 'U': '∩', 
              'V': 'Λ', 'W': 'M', 'X': 'X', 'Y': '⅄', 'Z': 'Z', '0': '0', '1': 'Ɩ', '2': 'ᄅ', '3': 'Ɛ', 
              '4': 'ㄣ', '5': 'ϛ', '6': '9', '7': 'ㄥ', '8': '8', '9': '6', ',': '‘', '.': '˙', "'": ',', 
              '"': '„', '?': '¿', '!': '¡', '(': ')', ')': '(', '[': ']', ']': '[', '{': '}', '}': '{', 
              '<': '>', '>': '<', '&': '⅋', '_': '‾', '/': '\\', '\\': '/', ';': '؛', ':': '∴', '@': '@', 
              '+': '±', '-': '⁻', '*': '⁎', '=': '≠', '^': 'v', '°': '°', '#': '#', '$': '$', '%': '%', 
              '£': '£', '€': '€', '¥': '¥', '`': '´', '~': '~' }
some_text = 'Ԁɹᴉʌǝʇ ɾnuᴉoɹ'
true_text = []
for i in range(len(some_text)):
    if some_text[i] == ' ':
            true_text.append(' ')
    for key, value in charMap.items():
        
        if value == some_text[i]:
            true_text.append(key)
print(true_text)

true_text = ''.join(true_text)

print(true_text)