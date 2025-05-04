import sys


def pozdrav_uzivatele(jmeno):
    if not jmeno:
        return None

    return f'Ahoj, {jmeno}, jak se vede?'


if __name__ == '__main__':
    # print(sys.argv)  # --> list všech předaných spouštěcích argumentů
                     # 0 .. je vždy jméno spouštěného souboru
                     # 'python lesson10_args.py 'aha' 'no toto!'
                     #         0                1     2    
    
    print(pozdrav_uzivatele(jmeno=sys.argv[1]))