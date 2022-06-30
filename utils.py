"""
title:                  utils.py
python version:         3.10

code style:             black==22.6
import style:           isort==5.10

Description:
    Responsible for conducting tests on all user inputs and providing the
    dataframe to array conversion method.
"""

from os import PathLike
from typing import Dict, Union

import numpy as np
import numpy.typing as npt
import pandas as pd

NDArrayFloat = npt.NDArray[np.float_]

# default assertion errors
td: str = "variable must be of type dict"
ti: str = "variable must be of type int"
tl: str = "variable must be of type list"
ts: str = "variable must be of type str"


def market_data_tests(
    start: str,
    end: str,
    stooq: Dict[str, list],
    path: Union[str, bytes, PathLike],
    price_type: str,
) -> None:
    """
    Conduct tests prior to scrapping historical financial data from Stooq.

    Parameters:
        star: start data
        end: end date
        stooq: market data to download from Stooq
        path: directory to save data
        price_type: type of market price to utilise
    """
    assert isinstance(start, str), ts
    assert start[4] == start[7] == "-", "data format must be YYYY-MM-DD"
    assert isinstance(end, str), ts
    assert end[4] == end[7] == "-", "data format must be YYYY-MM-DD"

    y_s, m_s, d_s = start[:4], start[5:7], start[-2:]
    y_e, m_e, d_e = end[:4], end[5:7], end[-2:]

    assert isinstance(int(y_s), int), ti
    assert isinstance(int(m_s), int), ti
    assert isinstance(int(d_s), int), ti
    assert isinstance(int(y_e), int), ti
    assert isinstance(int(m_e), int), ti
    assert isinstance(int(d_e), int), ti

    assert 1900 < int(y_s), "start year should be post 1900"
    assert 0 < int(m_s) <= 12, "only 12 months in year"
    assert 0 < int(d_s) <= 31, "maximum 31 days per month"
    assert 1900 < int(y_s), "end year should be post 1900"
    assert 0 < int(m_e) <= 12, "only 12 months in year"
    assert 0 < int(d_e) <= 31, "maximum 31 days per month"

    assert int(y_e + m_e + d_e) > int(
        y_s + m_s + d_s
    ), "end date must exceed start date"

    assert isinstance(stooq, dict), td

    for x in stooq:
        mkt = stooq[str(x)]
        assert isinstance(mkt, list), tl
        assert len(mkt) == 2, "mkt must have at least one number symbol"
        assert isinstance(mkt[0], str), ts
        assert isinstance(mkt[1], list), tl
        assert len(mkt[1]) == len(set(mkt[1])), "mkt must contain only unique elements"
        assert all(isinstance(a, str) for a in mkt[1]), ts

    assert isinstance(path, Union[str, bytes, PathLike])
    assert (
        path[0:2] == "./" and path[-1] == "/"
    ), "file path must be in a sub-directory relative to main.py"

    assert isinstance(price_type, str)
    assert (
        price_type.capitalize() == "Open" or "High" or "Low" or "Close"
    ), "price_type must be one of Open, High, Low, or Close"

    print("Market Import Tests: Passed")


def dataframe_to_array(market_data: pd.DataFrame, price_type: str) -> NDArrayFloat:
    """
    Converts pandas dataframe to cleaned numpy array by extracting relevant prices.

    Parameters:
        market_data: raw dataframe generated by pandas_datareader from remote source
        price_type: 'Open', 'High', 'Low', or 'Close' prices for the time step
        volume: whether to include volume

    Returns:
        prices: cleaned array of asset prices of a given type
    """
    market = market_data[str(price_type).capitalize()]

    # remove all rows with missing values
    market = market.dropna()

    # format time ordering if needed (earliest data point is at index 0)
    if market.index[0] > market.index[-1]:
        market = market[::-1]

    n_assets, n_days = market.columns.shape[0], market.index.shape[0]

    prices = np.empty((n_days, n_assets), dtype=np.float64)

    a = 0
    for asset in market.columns:
        prices[:, a] = market[str(asset)]
        a += 1

    return prices
