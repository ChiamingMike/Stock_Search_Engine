'''
Created on 2020/03/06

@author: ChiamingMike
'''

import datetime
import os
import pandas
import re

from bs4 import BeautifulSoup
from urllib import request

from engine_factory.constant.Definition import UrlsDefinition
from engine_factory.container.code_container.DefaultCodeContainer import DefaultCodeContainer
from engine_factory.logger.Log import log


class JPCodeContainer(DefaultCodeContainer):

    __instance = None
    __is_intialized = False

    JAPAN = 'JAPAN'

    def __new__(cls):
        """
        """
        if cls.__instance is None:
            cls.__instance = object.__new__(cls)

        return cls.__instance

    def __init__(self) -> None:
        """
        """
        if self.__is_intialized is True:
            return None

        self.__is_intialized = True

        self.stock_codes = list()
        file_name = 'JP_stock_list.xls'
        super().__init__(country=self.JAPAN)

        execution_date = datetime.datetime.now().strftime('%Y%m')
        self.file_name = f'{execution_date}_{file_name}'
        self.file_path = os.path.join(os.path.dirname(os.path.dirname(
            os.path.dirname(__file__))), 'asset', 'JP', self.file_name)

        self.conversion_table = pandas.Series()

        if not os.path.isfile(self.file_path):
            self.download_conversion_table()

        self.register_conversion_table()

        return None

    def register_stock_codes(self, codes_list) -> None:
        """
        """
        pattern = re.compile(r'^(\d{4})$')
        codes = [code for code in self.stock_codes if pattern.match(code)]
        stock_codes = [code for code in codes if code in codes_list]
        if stock_codes == list():
            log.e('Failed to create URL.')
            log.e('Valid Stock code doesn\'t exist.')
            log.e('')
            return None
        else:
            self.stock_codes = stock_codes
            stock_codes = ', '.join(stock_codes)
            log.i(f'Found {len(self.stock_codes)} valid codes.')
            log.i(f'STOCK CODE: {stock_codes}')
            log.i('')

            return None

        return None

    def register_conversion_table(self) -> None:
        """
        """
        if not os.path.isfile(self.file_path)\
                or os.path.getsize(self.file_path) == 0:
            log.w(f'Failed to read {self.file_name}.')
            log.w('')
            return None

        df = pandas.read_excel(self.file_path,
                               usecols=['Local Code', 'Name (English)'],
                               dtype=str)
        df.rename(columns={'Local Code': 'code', 'Name (English)': 'name'},
                  inplace=True)
        df.set_index('code', inplace=True)
        df.loc['0000'] = 'Nikkei 225'
        df.loc['0950'] = 'Dollar to Yen Exchange Rate'
        self.register_stock_codes(list(df.index))
        self.conversion_table = df.loc[self.stock_codes, 'name']

        return None

    def download_conversion_table(self) -> None:
        """
        """
        hp = UrlsDefinition.jpx.get('hp', str())
        url = UrlsDefinition.jpx.get('url', str())
        if str() in [hp, url]:
            log.w('Cannot find a URL to download list of TSE-listed Issues.')
            log.w('')
            return None

        html = request.urlopen(url)
        soup = BeautifulSoup(html, 'html.parser')
        url = hp + \
            soup.find('div', attrs={'class': 'component-file'}).a.get('href')
        request.urlretrieve(url, self.file_path)

        return None


if __name__ == '__main__':
    pass
