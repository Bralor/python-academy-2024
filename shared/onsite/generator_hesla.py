import string
import random

delka_hesla = int(input('Požadovaná délka hesla:'))  # 10 = 4 + 4 + 2
pocet_pismen = i1nt(delka_hesla * 0.4)
pocet_cislic = int(delka_hesla * 0.4)
pocet_znaku = int(delka_hesla * 0.2)

dovolene_pismena = string.ascii_letters
dovolene_cislice = string.digits
dovolene_znaky = string.punctuation

# ['a', 'b'] ==> 'ab'
vsechny_vybrane_znaky = \
    random.choices(dovolene_pismena, k=pocet_pismen) \
    + random.choices(dovolene_cislice, k=pocet_cislic) \
    + random.choices(dovolene_znaky, k=pocet_znaku)

print(''.join(vsechny_vybrane_znaky))
