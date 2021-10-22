import sys
sys.path.append(r'.\src')

from asclepius.releasetest import ReleaseTesten, Medewerker

from ggz_instellingen_origineel import *

nils = Medewerker('nils.warsen@valuecare.nl', r'C:\Users\nwarsen\Downloads', r'C:\Users\nwarsen\Documents\Testprogramma\excel')

tester = ReleaseTesten(nils)

tester.test_da(fier, eleos)