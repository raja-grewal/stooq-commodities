# Archive of Stooq Commodity Prices

[![License](https://img.shields.io/badge/License-MIT-green)](https://github.com/rajabinks/stooq-commodities/blob/master/LICENSE)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Imports: isort](https://img.shields.io/badge/%20imports-isort-%231674b1?style=flat&labelColor=ef8336)](https://pycqa.github.io/isort/)

Due to the [issue](https://github.com/pydata/pandas-datareader/issues/925) regarding the downloading of commodity prices from [Stooq](https://stooq.com/) using [pandas-datareader](https://pandas-datareader.readthedocs.io/en/latest/index.html), this repository stores a limited archive of previously obtained data.

The generation of historical data is done using `gen_data.py` with customisation options regarding asset selection and dates available within the file. Tests for all user inputs have also been written.

We provide seven sets of databases outlined in the table below. Note the count refers to cleaned data which only includes days where prices are available for all included assets.

These include the equity indices S\&P500 (SPX), Nasdaq 100 (NDX), Dow Jones Industrial Average (DJIA), along components of the DJIA. For commodities, we provide front month futures contract prices for gold, silver, high grade copper, platinum, palladium, WTI crude oil, RBOB gasoline, lumber, live cattle, coffee, and orange juice. The included 25 of total 30 DJIA components in DJI are not exactly the 26 in Full due to additions and removals to the index.

|  | Components | Count | Start Date | End Date |
| ----------- | ----------- | ----------- | ----------- | ----------- |
| **Equity Indices**
| SNP | SPX | 9,167 |1985-10-01 | 2022-02-10 |
| USEI | SPX + NDX, DJIA | 9,167 | 1985-10-01 | 2022-02-10 |
| DJI | USEI + 25 DJIA Components | 8,024 | 1990-03-26 | 2022-02-10 |
| **Broader Markets**
| Minor | USEI + Gold, Silver, WTI | 9,090 | 1985-10-01 | 2021-12-24 |
| Medium | Minor + Cooper, Platinum, Lumber | 9,077 | 1985-10-01 | 2021-12-24 |
| Major | Medium + Palladium, RBOB, Cattle, Coffee, OJ | 8,990 | 1985-10-01 | 2021-12-24 |
| Full | Major + 26 DJIA Components |7,858 | 1990-03-26 | 2021-12-24 |

Overall, these consist of daily time series of prices spanning from the earlier of either the first available date or the 10th October 1985. Equity indices can be updated whereas Broader Markets are not updatable as explained in the [issue](https://github.com/pydata/pandas-datareader/issues/925).

Initialising the code involves the following commands:
```commandline
git clone https://github.com/raja-grewal/stooq-commodities.git

cd stooq-commodities
```
Install all required packages with or without dependencies using:
```commandline
pip3 install -r requirements.txt

pip3 install -r requirements--no-deps.txt
```
Historical financial market data is sourced and aggregated using:
```commandline
python gen_data.py
```
The `.pkl` dataframes and `.csv` files are equivalent, while the `.npy` arrays are cleaned such that only dates where all assets have prices are included. The `.npy` files are also always ordered where earlier dates are indexed first, whereas the ordering in `.pkl` and `.csv` files is dependent on the communication between the Stooq API and relevant packages.

Additionally, due to requests we also provide the same data for each singular asset contained in the "DJI" and "Major" databases. Note that the arrays for each of these may not be synchronised temporally due to the placement of removed of missing values.

##  We Are Using GitHub Under Protest
This project is currently hosted on GitHub.  This is not ideal; GitHub is a proprietary, trade-secret system that is not Free and Open Souce Software (FOSS).  We are deeply concerned about using a proprietary system like GitHub to develop our FOSS project.  We urge you to read about the [Give up GitHub](https://GiveUpGitHub.org) campaign from [the Software Freedom Conservancy](https://sfconservancy.org) to understand some of the reasons why GitHub is not a good place to host FOSS projects.

Any use of this project's code by GitHub Copilot, past or present, is done without our permission.  We do not consent to GitHub's use of this project's code in Copilot.
