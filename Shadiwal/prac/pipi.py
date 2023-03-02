def to_weird_case(words):
    lol = ''
    words1 = words[0] + words[1::].replace(' ', '').lower()
    print(words1)
    for i in words1:
        if words1[0].isupper() and words1.index(i) % 2 == 0:
            i += i.upper()
        
        elif  words1[0].isupper() == False and words1.index(i) % 2 == 0:
            i += i.upper()
        lol += i
    return lol
    
print(to_weird_case('THIs iS a TEST'))
        