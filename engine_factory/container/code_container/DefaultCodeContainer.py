'''
Created on 2020/03/19

@author: ChiamingMike
'''

import configparser
import datetime
import os
import re
import pandas

from engine_factory.logger.Log import log


class DefaultCodeContainer(object):

    def __init__(self, country: str) -> None:
        """
        """
        try:
            root = os.path.join(os.path.dirname(os.path.dirname(
                os.path.dirname(__file__))), 'conf', 'Setting.ini')
            config = configparser.ConfigParser()
            config.read(root)
            section = country
            stock_codes = re.sub(
                r'\s+', '', config.get(section, 'code')).split(',')
            self.stock_codes = sorted(list(set(stock_codes)))
        except Exception as e:
            log.w(e)
            log.w('Failed to get the information from setting.ini .')
            log.w('')

        return None

    def register_stock_codes(self, stock_codes) -> None:
        pass

    def register_conversion_table(self) -> None:
        pass

    def download_conversion_table(self) -> None:
        pass

    def get_stock_codes(self) -> list:
        """
        """
        if self.stock_codes == list():
            log.e('Failed to get a list of sotck codes.')
            log.e('Stock code doesn\'t exist.')
            log.e('')
            return list()

        return self.stock_codes

    def get_conversion_table(self) -> pandas.Series:
        """
        """
        if self.conversion_table.empty:
            log.e('Failed to get conversion table.')
            log.e('')
            return pandas.Series()

        return self.conversion_table

    def convert_into_name(self, stock_code: str) -> str:
        """
        """
        try:
            stock_name = self.conversion_table[stock_code]
        except Exception as e:
            log.e(e)
            log.e('Failed to convert code into name.')
            log.e('')
            return str()

        return stock_name


if __name__ == '__main__':
    pass
