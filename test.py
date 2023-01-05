import sys
sys.path.append(r'.\src')

from asclepius.releasetest import ReleaseTest, Medewerker
from ggz_instellingen import *

# main function
def main():
    nils = Medewerker('nils.warsen@valuecare.nl',
                  r'C:\Users\nwarsen\Downloads',
                  r'C:\Users\nwarsen\Documents\Testprogramma\excel')

    tester = ReleaseTest(nils, product = 'omzetprognose')
    
    #emc = GGZ('ggzemc')
    #em = GGZ('ggzemergis')

    #tester.test_bi(delf, emc, emergis, fier, imp, ingeest, met, mondriaan, pp, ps, riv, waag, wnb, ihub)
    ingeest.excel_a = 'ggzingeest_omzetprognose_a.xlsx'
    ingeest.excel_p = 'ggzingeest_omzetprognose_p.xlsx'
    tester.testfuncties.excels_vergelijken(ingeest)

    return None

def main2():
    lijst = ['a', 'b', 'c', 'd']
    del_lijst = []

    for i, val in enumerate(lijst):
        if val == 'b' or val == 'c':
            del_lijst.append(i)
        print(i, val)

    lijst = [lijst[i] for i in range(len(lijst)) if i not in del_lijst]
    
    print(lijst)
    return None

main()