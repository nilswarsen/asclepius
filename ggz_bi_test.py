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
    tester.test(ingeest, net)

    return None

main()