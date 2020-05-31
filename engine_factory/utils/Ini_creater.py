import configparser
import os

from engine_factory.logger.Log import log


class IniCreater(object):

    def __init__(self, country: str):
        self.section = country
        self.period = 'monthly'
        self.root = os.path.join(os.path.dirname(
            os.path.dirname(__file__)), 'conf', 'Setting.ini')

        return None

    def create_ini_file(self, target_code: list):
        try:
            config = configparser.ConfigParser()
            config.add_section(self.section)
            config.set(self.section, 'period', self.period)
            config.set(self.section, 'code', ','.join(target_code))
            with open(self.root, 'w') as file:
                config.write(file)

        except Exception as e:
            log.w(e)
            log.w('Failed to create ini file .')
            log.w('')
            return None

        return None


if __name__ == '__main__':
    pass
