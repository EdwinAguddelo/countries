import requests
from domain.use_cases.utils.parameters import Parameters
from domain.models.gateways.countries_population_area_gateway import CountriesPopulationAreaGateWay
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

class CountriesDataApiIntegration(CountriesPopulationAreaGateWay):
    
    def __init__(self):
        self.payload = {}
        self.headers = {}
        self.url = Parameters.url_get_rest_countries
    
    def get_data(self):
        session = requests.Session()
        session.trust_env = False
        response = session.request("GET", self.url, headers = self.headers, data = self.payload)
        return response
    
    def get_countries_by_population_and_area(self):
        data_all_countries = self.get_data().json()
        return list(map(lambda x:{'name':x['name']['common'],'area':x['area'],'population':x['population']},data_all_countries))