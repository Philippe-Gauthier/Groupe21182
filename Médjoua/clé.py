"""
Dictionnaires de substitution pour le chiffrement et déchiffrement.
"""

# Dictionnaire pour déchiffrer (transforme message encrypté en lisible)
cle_dechiffrage = {
    'q': 'a', 'w': 'b', 'e': 'c', 'r': 'd', 't': 'e', 'y': 'f',
    'u': 'g', 'i': 'h', 'o': 'i', 'p': 'j', 'a': 'k', 's': 'l',
    'd': 'm', 'f': 'n', 'g': 'o', 'h': 'p', 'j': 'q', 'k': 'r',
    'l': 's', 'z': 't', 'x': 'u', 'c': 'v', 'v': 'w', 'b': 'x',
    'n': 'y', 'm': 'z'
}

# Dictionnaire pour chiffrer (transforme message lisible en encrypté)
cle_chiffrage = {
    'a': 'q', 'b': 'w', 'c': 'e', 'd': 'r', 'e': 't', 'f': 'y',
    'g': 'u', 'h': 'i', 'i': 'o', 'j': 'p', 'k': 'a', 'l': 's',
    'm': 'd', 'n': 'f', 'o': 'g', 'p': 'h', 'q': 'j', 'r': 'k',
    's': 'l', 't': 'z', 'u': 'x', 'v': 'c', 'w': 'v', 'x': 'b',
    'y': 'n', 'z': 'm'
}
