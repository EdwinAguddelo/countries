import sys
sys.path.append('././')
from flask import Flask,jsonify
from domain.use_cases.population_density.higher_densities_top import HigherDensitiesTop
from infraestructure.driven_adapters.apis.countries_data_api_integration import CountriesDataApiIntegration
from infraestructure.driven_adapters.bbdd.log_mysql_implementation import LogMysqlImplementation

app=Flask(__name__)

@app.route('/top_population_density')
def top_population_density():
    higher_densities_top = HigherDensitiesTop(CountriesDataApiIntegration(),LogMysqlImplementation())
    return higher_densities_top.get_top_population_density()    

if __name__=='__main__':
    app.run()
