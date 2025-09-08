cisla = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15)

# Procházej hodnoty pro zadaný tuple se jménem cisla,
# .. pokud je hodnota dělitelná třemi, vypiš "Fizz",
# .. pokud je hodnota dělitelná pěti, vypiš "Buzz",
# .. pokud je hodnota dělitelná třemi a současně pěti, vypiš "FizzBuzz",
# .. pokud nebude platit ani jedna z předchozích podmínek, vypiš hodnotu samotnou.
for cislo in cisla:
    if cislo % 3 == 0 and cislo % 5 == 0:
        pass
    elif cislo % 3 == 0:
        print("Fizz")
    elif cislo % 5 == 0:
        print("Buzz")
    else:
        print(cislo)
