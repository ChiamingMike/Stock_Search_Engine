'''
Created on 2020/03/06

@author: ChiamingMike
'''

from engine_factory.container.data_container.JPDataContainer import JPDataContainer
from engine_factory.container.url_container.JPUrlContainer import JPUrlContainer
from engine_factory.container.code_container.JPCodeContainer import JPCodeContainer
from engine_factory.engine.DefaultEngine import DefaultEngine
from engine_factory.logger.Log import log
from engine_factory.processor.Processor import AverageDataProcessor


class JPEngine(DefaultEngine):

    def __init__(self) -> None:
        """
        """
        self.code_container = JPCodeContainer()
        self.url_container = JPUrlContainer()
        self.data_container = JPDataContainer()

        self.stock_codes = self.code_container.get_stock_codes()
        self.term = self.url_container.get_term()
        self.accumulate_urls()
        self.accumulate_data()

        return None

    def accumulate_urls(self) -> None:
        """
        """
        self.url_container.register_accumulative_url()
        self.url_table = self.url_container.get_url_table()
        del self.url_container

        return None

    def accumulate_data(self) -> None:
        """
        """
        self.data_container.register_accumulative_data(self.url_table)

        return None

    def calcualte_data(self) -> None:
        """
        """
        for stock_code in self.stock_codes:
            stock_name = self.code_container.convert_into_name(stock_code)
            average_data_processor = AverageDataProcessor(self.term,
                                                          stock_name,
                                                          stock_code)
            average_data_processor.calculate_data()
            self.data_container.dump_accumulative_data(stock_name, stock_code)
        else:
            self.export_data()

        return None

    def export_data(self) -> None:
        """
        """
        self.data_container.dump_average_data()

        return None


if __name__ == '__main__':
    pass
