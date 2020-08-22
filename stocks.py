import yfinance as yf

from datetime import date

aktien = ['MSFT', 'AAPL', 'GOOG']
buyTime = ['01.01.2020', '01.01.2020', '01.01.2020']


def aktien(x):
    hello = aktienKursToday()
    return hello



def aktienKursToday():
    '''
                 Open        High         Low       Close   Adj Close    Volume
Date
2020-05-18  185.75  186.199997  183.960007  184.910004  184.910004  35264500
2020-05-18  185.75  186.199997  183.979996  184.910004  184.910004  35306620
    :return:
    '''
    return yf.download('MSFT', start=date.today(), end=date.today())

