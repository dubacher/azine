import random, string

# alphabet will become our base-32 character set:
alphabet = string.lowercase + string.digits 
# We must remove 4 characters from alphabet to make it 32 characters long. We want it to be 32
# characters long so that we can use a whole number of random bits to index into it.
for loser in 'l1o0': # Choose to remove ones that might be visually confusing
    i = alphabet.index(loser)
    alphabet = alphabet[:i] + alphabet[i+1:]

def byte_to_base32_chr(byte):
    return alphabet[byte & 31]

def random_id(length):
    # Can easily be converted to use secure random when available
    # see http://www.secureprogramming.com/?action=view&feature=recipes&recipeid=20
    random_bytes = [random.randint(0, 0xFF) for i in range(length)]
    return ''.join(map(byte_to_base32_chr, random_bytes))
