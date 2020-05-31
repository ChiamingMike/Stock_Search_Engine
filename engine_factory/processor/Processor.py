'''
Created on 2020/03/06

@author: ChiamingMike
'''

import pandas
import datetime

from engine_factory.constant.Definition import ColumnsDefinition
from engine_factory.container.data_container.JPDataContainer import JPDataContainer
from engine_factory.logger.Log import log


class DataProcessor(object):

    def __init__(self, term, stock_name, stock_code) -> None:
        """
        """
        execution_date = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        self.data_container = JPDataContainer()

        self.term = term
        self.date = execution_date
        self.stock_code = stock_code
        self.stock_name = stock_name

        return None

    def set_target_data(self) -> None:
        """
        """
        return None

    def calculate_data(self) -> None:
        """
        """
        return None


class AverageDataProcessor(DataProcessor):

    def __init__(self, term, stock_name, stock_code) -> None:
        """
        """
        self.length = int()
        self.start = str()
        # self.end = str()
        self.open = str()
        self.high = str()
        self.low = str()
        self.close = str()
        super().__init__(term, stock_name, stock_code)

        self.set_target_data()

        return None

    def set_target_data(self) -> None:
        """
        """
        accumulative_data = self.data_container.get_accumulative_data(
            self.stock_code)
        if accumulative_data.empty:
            log.e(f'No accumulative data relevant to {self.stock_code}')
            log.e('')
            return None

        try:
            self.length = len(accumulative_data)
            self.start = accumulative_data.iloc[-1][ColumnsDefinition.DATE]
            self.end = accumulative_data.iloc[0][ColumnsDefinition.DATE]
            self.open = sum(
                accumulative_data.loc[:, ColumnsDefinition.OPENING_PRICE])
            self.high = sum(
                accumulative_data.loc[:, ColumnsDefinition.HIGH_PRICE])
            self.low = sum(
                accumulative_data.loc[:, ColumnsDefinition.LOW_PRICE])
            self.close = sum(
                accumulative_data.loc[:, ColumnsDefinition.CLOSING_PRICE])
        except Exception as e:
            log.e(e)
            log.e('Failed to prepare calculation with accumulative data.')
            log.e('')
            return None

        return None

    def calculate_data(self) -> None:
        """
        """
        if str() in [self.open, self.high, self.low, self.close]:
            log.e('Failed to do calculation with accumulative data.')
            log.e('')
            return None

        average_data = pandas.DataFrame([{
            'EXE_DATE': str(self.date),
            'TERM': str(self.term),
            'START': str(self.start),
            'END': str(self.end),
            'NAME': str(self.stock_name),
            'CODE': str(self.stock_code),
            'OPENING PRICE (AVE)': float(self.open / self.length),
            'HIGH PRICE (AVE)': float(self.high / self.length),
            'LOW PRICE (AVE)': float(self.low / self.length),
            'CLOSING PRICE (AVE)': float(self.close / self.length)
        }])

        self.data_container.register_average_data(self.stock_code,
                                                  average_data)

        return None


if __name__ == '__main__':
    pass
