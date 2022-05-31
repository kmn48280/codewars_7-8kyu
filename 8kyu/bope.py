# The BOPE is the squad of special forces of police that usually handles the operations in the Favelas in Rio de Janeiro.

# In this Kata you have to write a function that determine the number of magazines that every soldier has to have in his bag.

# You will receive the weapon and the number of streets that they have to cross. Considering that every street the officer shoots 3 times. 
# Bellow there is the relation of weapons:

# PT92 - 17 bullets
# M4A1 - 30 bullets
# M16A2 - 30 bullets
# PSG1 - 5 bullets

# Example:

# ["PT92", 6] => 2 (6 streets 3 bullets each)
# ["M4A1", 6] => 1

# The return Will always be an integer so as the params.
####################################################################################################
import math
from typing import Tuple

def mag_number(info: Tuple[str, int]) -> int:
    if info[0] == 'PT92':
        if info[1] * 3 < 17:
            return 1
        else:
            return math.ceil((info[1] * 3) / 17)
    elif info[0] == 'M4A1':
        if info[1] * 3 < 30:
            return 1
        else:
            return math.ceil((info[1] * 3)/ 30)
    elif info[0] == 'M16A2':
        if info[1] * 3 < 30:
            return 1
        else:
            return math.ceil((info[1] * 3)/ 30)
    elif info[0] == 'PSG1':
        if info[1] * 3 < 5:
            return 1
        else:
            return math.ceil((info[1] * 3)/ 5)
print(mag_number(('PT92', 6)))
#########################################################################
from typing import Tuple
from math import ceil

weapons = {
    "PT92": 17,
    "M4A1": 30,
    "M16A2": 30,
    "PSG1": 5
}

def mag_number(info: Tuple[str, int]) -> int:
    return ceil(info[1] * 3 / weapons[info[0]])