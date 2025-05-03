import argparse


def func1(a, b):
    return int(a) + int(b)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-x', dest='cislo1')
    parser.add_argument('-y', dest='cislo2')
    args = parser.parse_args()

    print(func1(a=args.cislo1,
                b=args.cislo2))