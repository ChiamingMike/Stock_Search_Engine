'''
Created on 2020/05/30

@author: ChiamingMike
'''

from engine_factory.logger.Log import log
from engine_factory.engine.JPEngine import JPEngine
from engine_factory.engine.USEngine import USEngine


class EngineSwitch(object):
    JAPAN = 'JAPAN'
    TAIWAN = 'TAIWAN'
    US = 'US'

    def __init__(self) -> None:
        """
        """

        return None

    def switching_engine_to(self, country: str) -> None:
        """
        """
        if country == self.JAPAN:

            log.i('Switching country to JAPAN...')
            log.i('')

            jp_engine = JPEngine()
            jp_engine.calcualte_data()

        elif country == self.TAIWAN:
            log.i('Switching country to TAIWAN...')
            log.i('')

        elif country == self.US:
            log.i('Switching country to US...')
            log.i('')

            jp_engine = USEngine()

        else:
            log.i('Unexcepted country.')
            log.i('')

        return None


if __name__ == '__main__':
    pass
