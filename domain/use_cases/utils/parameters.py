import os
class Parameters:
    url_get_rest_countries = os.getenv('url_get_rest_countries')
    top_number = os.getenv('top_number')
    host = os.getenv('host')
    user = os.getenv('user')
    password = os.getenv('password')
    db = os.getenv('db')