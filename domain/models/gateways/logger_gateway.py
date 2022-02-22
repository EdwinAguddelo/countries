from abc import ABCMeta, abstractmethod

class LoggerGateway(metaclass=ABCMeta):

    @abstractmethod
    def set_log(self,response)->str:
        "set log in database with the given response."