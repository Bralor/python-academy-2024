import os
import csv


def main():
    nactene_csv = nacti_csv_data('shared/onsite/Aktivace_SVR_01az21042025_ceny.csv')
    vyfiltrovane = filtruj_sloupce(nactene_csv)
    zapis_upravene_hodnoty(cesta_k_souboru='shared/onsite/lesson10_exercise_1.csv',
                           data=vyfiltrovane)


def nacti_csv_data(cesta_k_souboru):
    if not os.path.exists(cesta_k_souboru):  # Guard clause
        return None
    
    with open(cesta_k_souboru,
              mode='r',
              newline='',
              encoding='UTF-8-sig') as csv_soubor:
        cteni = csv.reader(csv_soubor, delimiter=';')
        return tuple(cteni)
    

def filtruj_sloupce(data,
                    pocet_platnych_sloupcu=2,
                    prvni_radek=3):
    if not data:
        return None

    upravene_hodnoty = list()

    for cislo_radku, radek in enumerate(data):
        if cislo_radku < prvni_radek:
            continue

        upravene_hodnoty.append(radek[:pocet_platnych_sloupcu])

    return upravene_hodnoty


def zapis_upravene_hodnoty(cesta_k_souboru, data):
    with open(cesta_k_souboru,
              mode='w',
              newline='',
              encoding='UTF-8') as csv_soubor:
        zapis = csv.writer(csv_soubor, delimiter=';')
        zapis.writerows(data)
        

if __name__ == '__main__':
    main()
