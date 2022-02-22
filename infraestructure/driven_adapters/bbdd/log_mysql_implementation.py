import pymysql
from domain.models.gateways.logger_gateway import LoggerGateway
from domain.use_cases.utils.parameters import Parameters

class LogMysqlImplementation(LoggerGateway):
    
    def __init__(self):
        self.connection = pymysql.connect(
            host = Parameters.host,
            user = Parameters.user,
            password = Parameters.password,
            db = Parameters.db
        )
        self.cursor = self.connection.cursor()
    
    def set_log(self, response):                
        self.cursor.execute(f'INSERT INTO Line.Log (consultationDate,response) VALUE (now(),"{response}")')
        self.connection.commit()
        return 'Logged in the database'
        
            
        
        
    