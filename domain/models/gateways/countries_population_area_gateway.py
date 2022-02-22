from abc import ABCMeta, abstractmethod
from typing import List, Dict

class CountriesPopulationAreaGateWay(metaclass=ABCMeta):

    @abstractmethod
    def get_countries_by_population_and_area(self) -> List[Dict]:
        "get countries by population and area."
        
   