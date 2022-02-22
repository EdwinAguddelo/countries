import operator
from domain.models.gateways.countries_population_area_gateway import CountriesPopulationAreaGateWay
from domain.models.gateways.logger_gateway import LoggerGateway
from domain.use_cases.utils.parameters import Parameters

class HigherDensitiesTop:
    
    def __init__(self,countries_data:CountriesPopulationAreaGateWay,logger:LoggerGateway):
        self.countries_data = countries_data
        self.logger = logger
        self.countries_by_population_area = self.countries_data.get_countries_by_population_and_area()

    @staticmethod
    def calculate_population_density(population,area):
        return round(population/area, 2)

    def countries_by_population_density(self):
        return list(map(lambda x:{'name':x['name'],'population_density':self.calculate_population_density(x['population'],x['area'])},self.countries_by_population_area))

    def get_top_population_density(self):
        response = sorted(self.countries_by_population_density(),key=operator.itemgetter('population_density'), reverse=True)[:int(Parameters.top_number)]
        try:
            status_log = self.logger.set_log(response)
            return {'status_log':status_log,'response':response}
        except Exception as e:
            print(e)
            return {'status_log':'Error in query','response':response}
    
    
    