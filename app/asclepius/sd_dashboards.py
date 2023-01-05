import json
import pandas as pd
from copy import deepcopy
import string

class DashboardBuilder:
    def __init__(self, expansions: pd.DataFrame) -> None:
        self.expansions = expansions
        return None

    def create_code(self, base: str, value_1: str, value_2: str = '', tegel_code: bool = False) -> str:

        # convert loopvalues to lowercase and remove punctuation
        value_1 = value_1.translate(str.maketrans('', '', string.punctuation)).lower().replace(' ', '')
        value_2 = value_2.translate(str.maketrans('', '', string.punctuation)).lower().replace(' ', '')
        
        if tegel_code:
            code = base + value_1 + value_2
        elif value_2 == '':
            code = f'{base}_{value_1}'
        else:
            code = f'{base}_{value_1}_{value_2}'
        return code

    def create_quicknavs(self, row, dashboard_code, primary_loop_value, secondary_loop_value) -> list:
        """
        This function generates the quickNavigations section of the json for each dashboard.
        """
        
        # Get the name and values of the primary loop
        primary_loop_title = row['Primary Loop Title']
        primary_loop_values = [value.strip() for value in row['Primary Loop Values'].split(';')]
        
        # Get the name and values of the secondary loop
        secondary_loop_title = row['Secondary Loop Title']
        if secondary_loop_title == 'None':
            secondary_loop_values = ['']
        else:
            secondary_loop_values = [value.strip() for value in row['Secondary Loop Values'].split(';')]

        quicknavs = []

        # Generate a dictionary containing the required information for the quickNavigations button related to the primary loop
        primary_loop_quicknav = {'field': primary_loop_title, 'options': [{'value': value, 'dashboardCode': self.create_code(dashboard_code, value, secondary_loop_value)} for value in primary_loop_values]}
        quicknavs.append(primary_loop_quicknav)

        if secondary_loop_title != 'None':
            # Generate a dictionary containing the required information for the quickNavigations button related to the secondary loop
            secondary_loop_quicknav = {'field': secondary_loop_title, 'options': [{'value': value, 'dashboardCode': self.create_code(dashboard_code, primary_loop_value, value)} for value in secondary_loop_values]}
            quicknavs.append(secondary_loop_quicknav)

        # Put both dictionaries together in a list and return them
        #quicknavs = [primary_loop_quicknav, secondary_loop_quicknav]
        return quicknavs

    def build(self) -> None:
        expansies = self.expansions
        
        # Iterate over the entries in the "expansies" dataframe (i.e. the dashboards we want to build)
        for index, row in expansies.iterrows():

            # Initialize an empty list which shall contain all of the dashboards created below
            new_dashboards = []
            
            # Open the .json file containing the template associated with the dashboard
            with open(row['Template'], 'r') as f:
                template_dashboards = json.load(f)
        
                # Get the loop values of the primary loop
                primary_loop_values = [value.strip() for value in row['Primary Loop Values'].split(';')]

                secondary_loop_title = row['Secondary Loop Title']

                if secondary_loop_title == 'None':
                    secondary_loop_values = ['']

                else:
                    # Get the loop values of the secondary loop
                    secondary_loop_values = [value.strip() for value in row['Secondary Loop Values'].split(';')]

                # Iterate over all combinations of primary and secondary loop values
                for primary_loop_value in primary_loop_values:
                    for secondary_loop_value in secondary_loop_values:
                        
                        # Start with a deep copy of the list of dashboard templates so that we can later reset to that list
                        dashboards = deepcopy(template_dashboards)


                        for dashboard in dashboards:
                            
                            dashboard["quickNavigations"] = self.create_quicknavs(row, dashboard['code'], primary_loop_value, secondary_loop_value)
                            
                            # Change the code so it refers to the dashboard for a specific set of loop values
                            dashboard['code'] = self.create_code(dashboard['code'] , primary_loop_value, secondary_loop_value)
                            dashboard['subtitle'] = f"{dashboard['title']} voor {secondary_loop_value} in {primary_loop_value}."
                            
                            # Modify tile names so that the correct tiles are shown
                            for section in dashboard['sections']:
                                for item in section['dashboardItems']:
                                    item['code'] = self.create_code(item['code'], primary_loop_value + secondary_loop_value, tegel_code = True)
                            
                            new_dashboards.append(dashboard)

            # Write the list of dashboards to a .json file
            with open(row['Save As'] + '.json', 'w') as f:
                json.dump(new_dashboards, f, indent = 4)

        return None