# import Asclepius dependencies
from asclepius.instelling import GGZ
from asclepius.medewerker import Medewerker
from asclepius.regressietest import RegressieTest

# import other dependencies


class ReleaseTest2:

    def __init__(self, gebruiker: Medewerker, losse_bestanden: bool = False):

        # Initialiseren
        self.gebruiker = gebruiker

        self.losse_bestanden = losse_bestanden

        return None
    
    def test_bi(self, *instellingen: GGZ):
        from asclepius.regressietest import RegressieTest, TestExcel

        te = TestExcel(join_col = 'Titel', header_row = 0, test_cols = ['Norm', 'Realisatie'])

        # import hardcoded information from fileserver
        import sys
        sys.path.append(r'\\valuecare.local\fileserver\Algemeen\Automatisch testen\Python')
        from parameters import HardCodedParameters as HCP
        var_links = HCP.ggz_variabele_links

        rt = RegressieTest(self.gebruiker, product = 'bi', test_excel = te, variabele_links = var_links)

        rt.test(*instellingen)

        return None
    
    def test_var(self, *instellingen: GGZ):
        from asclepius.regressietest import RegressieTest, TestExcel

        te = TestExcel(join_col = 'Financier', header_row = 0, test_cols = ['Omzet', 'Omzet norm'])

        # import hardcoded information from fileserver
        import sys
        sys.path.append(r'\\valuecare.local\fileserver\Algemeen\Automatisch testen\Python')
        from parameters import HardCodedParameters as HCP
        T_LINK = HCP.ggz_dict['omzetprog_per_financier']
        D_LINK = HCP.ggz_dict['omzetprog_per_financier_download']

        rt = RegressieTest(self.gebruiker, product = 'var', test_excel = te, target_link = T_LINK, download_link = D_LINK)

        rt.test(*instellingen)

        return None

class ReleaseTest(RegressieTest):
    def __init__(self, gebruiker: Medewerker, product: str = 'custom') -> None:

        from asclepius.regressietest import TestExcel

         # import hardcoded information from fileserver
        import sys
        sys.path.append(r'\\valuecare.local\fileserver\Algemeen\Automatisch testen\Python')
        from parameters import HardCodedParameters as HCP

        if product == 'bi':
            
            te = TestExcel(join_col = 'Titel', header_row = 0, test_cols = ['Norm', 'Realisatie'])

            T_LINK = None
            D_LINK = None

            var_links = HCP.ggz_variabele_links

        elif product == 'omzetprognose':

            te = TestExcel(join_col = 'Financier', header_row = 2, test_cols = ['Omzet', 'Omzet norm'])

            T_LINK = HCP.ggz_dict['omzetprog_per_financier']
            D_LINK = HCP.ggz_dict['omzetprog_per_financier_download']

            var_links = None

        else:
            raise Exception('Geen geldig product opgegeven!')

        super().__init__(gebruiker, product, test_excel = te, target_link = T_LINK, download_link = D_LINK, variabele_links = var_links)
        return None