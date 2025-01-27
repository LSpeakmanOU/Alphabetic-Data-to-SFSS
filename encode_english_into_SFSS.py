'''This encodes ASCII alphabetic symbols + spaces and exclamation points into the appropriate SFSS alphabetic translation.
While the encoding of space was not originally included in RFC 4824, we figured that the participants in
this protocol might need a break from signalling large messages. Thus the symbol for space is encoded 
as the transmitting interface holding a soda thus reinforcing common breaks. '''
# Note: any character without an encoding will result in a ! being sent

def split_n(s, n):
    result = []
    while len(s) > n:
        result.append(s[0:n])
        s = s[n:]
    if len(s.rstrip("\n")) != 0:
        result.append(s.rstrip("\n"))
    return result
def index_alphabet_pieces(line_idx, pieces, mapping, alphabet):
    offset = int(line_idx / 3)*4
    for idx, piece in enumerate(pieces):
        map_id = alphabet[offset+idx]
        if map_id in mapping:
            mapping[map_id].append(piece)
        else:
            mapping[map_id] = [piece]
ascii_to_map = "abcdefghijklmnopqrstuvwxyz! "
alpha_in = open("alphabet.txt", "r")
mapping = {}
for line_idx, line in enumerate(alpha_in.readlines()):
    index_alphabet_pieces(line_idx, split_n(line, 5), mapping, ascii_to_map)
val = input("Enter your message(A-Za-z !): ").lower()
output = [[],[],[]]
for char in val:
    if char in ascii_to_map:
        for i in range(3):
            output[i].append(mapping[char][i])
    else:
        for i in range(3):
            output[i].append(mapping['!'][i])
for i in range(3):
    print(''.join(output[i]))

