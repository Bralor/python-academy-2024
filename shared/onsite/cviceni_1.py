from cviceni_2 import preved_text_na_velke_pocatecni_pismeno


jmeno = "Matouš"

def spoj_slova(*args):
    prijmeni = "Holinka"
    
    if not args:  # None, '', {}, []
        return None
    else:
        return '-'.join(args)  # ('a' ,'b', 'c') --> 'a-b-c'
    

# print(spoj_slova(),
#       spoj_slova(''),
#       spoj_slova('a', 'b', 'c'),
#       spoj_slova('a', 'b', 'c', 'd'),
#       sep='\n')

# print(globals())

spojene_slovo = spoj_slova('a', 'b', 'c')
print(preved_text_na_velke_pocatecni_pismeno(spojene_slovo))