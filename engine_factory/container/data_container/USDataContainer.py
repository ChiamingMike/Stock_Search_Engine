'''
Created on 2020/06/20

@author: ChiamingMike
'''


import os
import pandas

from urllib import request

from engine_factory.constant.Definition import ColumnsDefinition
from engine_factory.container.data_container.DefaultDataContainer import DefaultDataContainer
from engine_factory.logger.ExecutionLogger import AccumulativeDataLogger
from engine_factory.logger.ExecutionLogger import AverageDataLogger
from engine_factory.logger.Log import log


class USDataContainer(DefaultDataContainer):

    __instance = None
    __is_initialized = False

    def __new__(cls):
        """
        """
        if cls.__instance is None:
            cls.__instance = object.__new__(cls)

        return cls.__instance

    def __init__(self) -> None:
        """
        """
        if self.__is_initialized is True:
            return None

        self.__is_initialized = True

        self.stock_code = str()
        self.average_data_table = dict()
        self.data_table = dict()
        self.average_data = pandas.DataFrame()

        return None

    def register_accumulative_data(self, url_table) -> None:
        """
        """
        if url_table == dict():
            log.e('Failed to accumulate data (URL doesn\'t exist).')
            log.e('')
            return None

        root = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
        for stock_code, url in url_table.items():
            file_name = f'{stock_code}.csv'
            file_path = os.path.join(root, 'asset', 'US', file_name)
            can_download = self.__can_download_data(stock_code, url, file_path)

            if can_download:
                df = pandas.read_csv(file_path)
                self.data_table[stock_code] = df.sort_values(
                    ColumnsDefinition.columns_us.get('DATE'), ascending=False)

        return None

    def register_average_data(self, stock_code, average_data) -> None:
        """
        """
        self.average_data_table[stock_code] = average_data

        return None

    def get_accumulative_data(self, stock_code: str) -> pandas.DataFrame:
        """
        """
        return self.data_table.get(stock_code, pandas.DataFrame())

    def get_average_data(self) -> pandas.DataFrame:
        """
        """
        return self.average_data_table

    def dump_accumulative_data(self, stock_name: str, stock_code: str) -> None:
        """
        """
        accumulative_data_logger = AccumulativeDataLogger(stock_name,
                                                          stock_code)
        accumulative_data_logger.dump_execution_log(
            self.data_table[stock_code])

        return None

    def dump_average_data(self) -> None:
        """
        """
        df_list = list()
        average_data_logger = AverageDataLogger()
        existence_log = average_data_logger.get_existence_log()
        if not existence_log.empty:
            df_list.append(existence_log)

        for stock_code, average_data in self.average_data_table.items():
            df_list.append(average_data)
            log.i(f'Exporting average data...({stock_code})')
            log.i('')
        else:
            self.average_data = pandas.concat(df_list, axis=0)
            self.average_data.sort_values(['TERM', 'CODE'], inplace=True)
            average_data_logger.dump_execution_log(self.average_data)

        return None

    def __can_download_data(self, code: str, url: str, path: str) -> bool:
        """
        """
        can_download = bool()
        try:
            request.urlretrieve(url, path)
            log.i(f'Downloaded data of {code}')
            can_download = True

        except Exception as e:
            log.e(f'Failed to download data of {code}')
            log.e(e)

        return can_download


if __name__ == '__main__':
    pass
