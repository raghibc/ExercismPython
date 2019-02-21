def is_pangram(sentence):
    letters_used = []
    sentence = sentence.upper()
    
    for i in sentence:
        if i not in letters_used and i.isalpha() == True:
            letters_used.append(i)

    if len(letters_used) == 26:
        return True
    else:
        return False
