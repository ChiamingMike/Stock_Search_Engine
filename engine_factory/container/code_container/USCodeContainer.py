'''
Created on 2020/03/06

@author: ChiamingMike
'''

import datetime
import os
import pandas
import re
import requests

from dateutil.relativedelta import relativedelta
from bs4 import BeautifulSoup
from urllib import request

from engine_factory.constant.Definition import UrlsDefinition
from engine_factory.container.code_container.DefaultCodeContainer import DefaultCodeContainer
from engine_factory.logger.Log import log


class USCodeContainer(DefaultCodeContainer):

    __instance = None
    __is_intialized = False

    US = 'US'

    def __new__(cls):
        """
        """
        if cls.__instance is None:
            cls.__instance = object.__new__(cls)

        return cls.__instance

    def __init__(self) -> None:
        """
        Try to download historical data before finding out if the symbol is substantial.
        If data is not found then the symbol is invalid.
        """
        if self.__is_intialized is True:
            return None

        self.__is_intialized is True

        self.symbols_list = list()
        super().__init__(country=self.US)
        # self.stock_codes = ['BRK-B', 'AAPL', 'test123']

        self.register_stock_codes(self.stock_codes)
        self.stock_codes.clear()

        return None

    def register_stock_codes(self, symbols_list) -> None:
        """
        """
        self.symbols_list = [
            symbol for symbol in symbols_list if self.__is_valid(symbol)]

        if self.symbols_list == list():
            log.e('Valid symbol doesn\'t exist.')
            log.e('')
            return None
        else:
            log.i(f'Found {len(self.symbols_list)} valid codes.')
            log.i('SYMBOLS: {sym}'.format(sym=', '.join(self.symbols_list)))
            log.i('')

        return None

    def register_conversion_table(self) -> None:
        """
        """

        return None

    def download_conversion_table(self) -> None:
        """
        """

        return None

    def __is_valid(self, symbol: str) -> bool:
        """
        """
        is_valid = bool()

        url_format = UrlsDefinition.yahoo_us_finance.get('url', str())
        if url_format == str():
            log.w('Cannot find a format to create initial url.')
            log.w('')
            return None

        now_time_unix = str(datetime.datetime.now().timestamp()).split('.')[0]
        try:
            url = url_format.format(symbol=symbol,
                                    now_time_unix=now_time_unix,
                                    period='wk')
            is_valid = True if requests.get(url).status_code == 200 else False

        except Exception as e:
            log.e(f'Failed to start new HTTPS connection: {symbol}')
            log.e(url)
            log.e(e)

        return is_valid

    # def dl_data(self, symbol: str) -> bool:
    #     """
    #     """
    #     is_valid = bool()

    #     to_time = datetime.datetime.now()
    #     from_time = to_time + relativedelta(years=-5)
    #     to_time_unix = str(to_time.timestamp()).split('.')[0]
    #     from_time_unix = str(from_time.timestamp()).split('.')[0]

    #     path = os.path.join(os.path.dirname(__file__), 'tst.csv')
    #     url = f'https://query1.finance.yahoo.com/v7/finance/download/{symbol}?period1={from_time_unix}&period2={to_time_unix}&interval=1d&events=history'
    #     try:
    #         request.urlretrieve(url, path)
    #         is_valid = True
    #         print('valid:', symbol)

    #     except Exception as e:
    #         print('Invalid symbol:', symbol)
    #         print(e)

    #     return is_valid


if __name__ == '__main__':
    obj = USCodeContainer()
