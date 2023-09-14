# Convert Text to ASCII values stored in a list

def ascii_list(chars):
    coded = []
    codable = list(chars)
    for codes in codable:
        coded.append(ord(codes))
    return coded

# main
# Exmaple usage
ascii_list('Navin Amal Anand') # returns [78, 97, 118, 105, 110, 32, 65, 109, 97, 108, 32, 65, 110, 97, 110, 100]
        
#### MADE BY AMAL ANAND NAVIN FROM ASRJC CLASS 24/12 ####
