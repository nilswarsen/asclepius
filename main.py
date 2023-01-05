from math import sqrt
import time
import multiprocessing as mp

import sys
sys.path.append(r'.\src')

from asclepius.releasetest import ReleaseTest, Medewerker
from ggz_instellingen import *

def block_distribution(data: list, p: int) -> list:

    
    
    block_size = len(data) / 2
    return data

def sieve(number:int) -> list:

    numbers = list(range(2, number + 1))
    root_number = sqrt(number)

    for num in numbers:
        if num < root_number:
            multiples = [i * num for i in range(2, number + 1) if i * num <= number]
            print(multiples)
            numbers = [x for x in numbers if x not in multiples]
        else:
            continue

    return numbers


def main():
    inst_1 = [delf, emc]
    inst_2 = [emergis, fier]
    inst_3 = [imp, ingeest]
    inst_4 = [met, mondriaan]

    nils = Medewerker('nils.warsen@valuecare.nl',
            r'C:\Users\nwarsen\Downloads',
            r'C:\Users\nwarsen\Documents\Testprogramma\excel')

    tester = ReleaseTest(nils, product = 'bi')

    p1 = mp.Process(target=tester.test, args=(*inst_1,))
    p2 = mp.Process(target=tester.test, args=(*inst_2,))
    p3 = mp.Process(target=tester.test, args=(*inst_3,))
    p4 = mp.Process(target=tester.test, args=(*inst_4,))

    p1.start()
    p2.start()
    p3.start()
    p4.start()
    return None

if __name__ == '__main__':

    start = time.time()
    main()
    end = time.time()

    print(end - start)