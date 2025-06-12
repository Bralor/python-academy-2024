def vnejsi_funkce(ramec):
    def vnitrni_funkce():
        print(ramec)
    vnitrni_funkce()

vnejsi_funkce("lokalni")