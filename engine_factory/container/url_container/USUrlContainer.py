'''
Created on 2020/03/06

@author: ChiamingMike
'''

import datetime

from dateutil.relativedelta import relativedelta

from engine_factory.constant.Definition import UrlsDefinition
from engine_factory.constant.Definition import PeriodDefinition
from engine_factory.container.code_container.USCodeContainer import USCodeContainer
from engine_factory.container.url_container.DefaultUrlContainer import DefaultUrlContainer
from engine_factory.logger.Log import log


class USUrlContainer(DefaultUrlContainer):

    US = 'US'

    def __init__(self) -> None:
        """
        """
        self.url_table = dict()
        self.term = str()
        self.period = str()
        super().__init__(country=self.US)
        self.period = PeriodDefinition.period_us.get(self.term, None)

        self.code_container = USCodeContainer()
        self.create_initial_url()

        return None

    def create_initial_url(self) -> None:
        """
        """
        url_format = UrlsDefinition.yahoo_us_finance.get('url', str())
        if url_format == str():
            log.w('Cannot find a format to create initial url.')
            log.w('')
            return None

        stock_codes = self.code_container.get_stock_codes()
        to_time = datetime.datetime.now()
        from_time = to_time + relativedelta(years=-5)
        to_time_unix = str(to_time.timestamp()).split('.')[0]
        from_time_unix = str(from_time.timestamp()).split('.')[0]
        for symbol in stock_codes:
            url = url_format.format(symbol=symbol,
                                    from_time_unix=from_time_unix,
                                    to_time_unix=to_time_unix,
                                    period=self.period)
            self.url_table[symbol] = url

        return None

    def register_accumulative_url(self) -> None:
        """
        """

        return None


if __name__ == '__main__':
    pass
