'''
Created on 2020/03/06

@author: ChiamingMike
'''


class ColumnsDefinition:
    columns_jp = {
        'DATE': '日付',
        'OPENING_PRICE': '始値',
        'CLOSING_PRICE': '終値',
        'HIGH_PRICE': '高値',
        'LOW_PRICE': '安値'
    }

    columns_us = {
        'DATE': 'Date',
        'OPENING_PRICE': 'Open',
        'CLOSING_PRICE': 'Close',
        'HIGH_PRICE': 'High',
        'LOW_PRICE': 'Low'
    }


class UrlsDefinition:
    kabutan_jp = {
        'url': 'https://kabutan.jp/stock/kabuka?code={stock_code}&ashi={period}&page={offset}',
        'next_page': 'https://kabutan.jp/stock/kabuka{next_page}'
    }

    jpx = {
        'hp': 'https://www.jpx.co.jp',
        'url': 'https://www.jpx.co.jp/english/markets/statistics-equities/misc/01.html'
    }

    yahoo_us_finance = {
        'url': 'https://query1.finance.yahoo.com/v7/finance/download/{symbol}?period1={from_time_unix}&period2={to_time_unix}&interval=1{period}&events=history'
    }


class PeriodDefinition:
    period_jp = {
        'daily': 'day',
        'weekly': 'wek',
        'monthly': 'mon',
        'yearly': 'yar'
    }

    period_us = {
        'daily': 'd',
        'weekly': 'wk',
        'monthly': 'mo',
    }
