import math
import os

polomery = (1, 2, 3, 4, 5)

plochy = list()

for polomer in polomery:
    plochy.append(round(math.pi * pow(polomer, 2), 2))

print(plochy)
