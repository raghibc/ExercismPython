def abbreviate(words):
    words = words.split()
    abbr = '';
    for i in range(len(words)):
        for j in range(len(words[i])):
            if(j == 0 and words[i][j].isalpha()):
                abbr = abbr + words[i][j]
            if(j !=0 and words[i][j].isalpha()):
                if(words[i][j-1] == '_' or words[i][j-1] == '-'):
                    abbr = abbr + words[i][j]

    abbr = abbr.upper()
    return abbr;
