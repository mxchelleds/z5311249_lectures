""" yf_example3.py

Example of a function to download stock prices from Yahoo Finance.
"""

import toolkit_config as cfg
from lectures import yf_example2


def qan_prc_to_csv(year):
    """ Downloads qantas stock prices for a given year
    Parameters
    ----------
    year : integer
    """
    tic = "QAN.AX"
    start =  f"{year}-01-01"
    end = f"{year}-12-31"
    datadir = cfg.DATADIR
    pth = f'{datadir}\\qan_prc_{year}.csv'
    yf_example2.yf_prc_to_csv(tic, pth, start, end)

# Example
if __name__ == "__main__":
    qan_prc_to_csv(year=2020)