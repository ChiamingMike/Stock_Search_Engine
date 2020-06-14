'''
Created on 2020/03/06

@author: ChiamingMike
'''

import configparser
import os

from urllib import request

from engine_factory.logger.Log import log


class DefaultUrlContainer(object):

    def __init__(self, country: str) -> None:
        """
        """
        try:
            root = os.path.join(os.path.dirname(os.path.dirname(
                os.path.dirname(__file__))), 'conf', 'Setting.ini')
            config = configparser.ConfigParser()
            config.read(root)
            section = country
            self.term = config.get(section, 'period')

        except Exception as e:
            log.w(e)
            log.w('Failed to get the information from setting.ini .')
            log.w('')
            return None

        return None

    def create_initial_url(self) -> None:
        pass

    def register_accumulative_url(self) -> None:
        pass

    def get_url_table(self) -> dict:
        """
        """
        return self.url_table

    def get_term(self) -> str:
        """
        """
        return self.term

    def _is_url_valid(self, url, stock_code) -> bool:
        """
        """
        try:
            result = request.urlopen(url)
            result.close()
            return True
        except Exception as e:
            log.w(e)
            log.w(f'Invalid URL for stock code {stock_code}')
            log.w('')
            return False


if __name__ == '__main__':
    pass
