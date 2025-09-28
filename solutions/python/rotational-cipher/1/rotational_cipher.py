def rotate(text, key):
    # list all letters of the alphabet
    plain = "abcdefghijklmnopqrstuvwxyz"
    plain = list(plain)
    final=[]

    for char in text:
        if char in plain:
            char_index= plain.index(char)
            if char_index+key>25:
                char_index-=26
            final.append(plain[char_index+key])
        elif char.lower() in plain:
            char_index= plain.index(char.lower())
            if char_index+key>25:
                char_index-=26
            final.append(plain[char_index+key].upper())
        else:
            final.append(char)
    return "".join(final)