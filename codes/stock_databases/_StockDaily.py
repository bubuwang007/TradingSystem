import os
import time
import functools
from datetime import datetime

import pandas as pd
import tushare as ts
from mtools import init_tushare
from ._StockBasic import StockBasic


class StockDaily:

    @staticmethod
    def get_daily_data_filepath(ts_code: str):
        p = os.path.abspath(
            os.path.join(
                os.path.dirname(__file__),
                f"./files/a_stock/daily/{ts_code}.csv",
            )
        )
        return p

    @staticmethod
    def fetch_daily_data(ts_code: str, start_date: str, end_date: str):
        init_tushare()
        pro = ts.pro_api()
        while True:
            try:
                df = pro.daily(
                    ts_code=ts_code, start_date=start_date, end_date=end_date
                )
            except Exception:
                time.sleep(1)
                continue
            return df

    @staticmethod
    def fetch_all_daily_data(
        start_date: str = "20000101", end_date: str = None, store: bool = False
    ):
        if end_date is None:
            end_date = datetime.now().strftime("%Y%m%d")
        df_basic = StockBasic.load_stock_basic_dataframe()
        for ts_code in df_basic["ts_code"]:
            df_daily = StockDaily.fetch_daily_data(
                ts_code=ts_code, start_date=start_date, end_date=end_date
            )
            if store:
                daily_filepath = StockDaily.get_daily_data_filepath(ts_code=ts_code)
                df_daily.to_csv(daily_filepath, index=False, encoding="utf-8")

    @staticmethod
    def update_all_daily_data(step: int = 500):
        pro = ts.pro_api()
        df_basic = StockBasic.load_stock_basic_dataframe()

        now = 0

        ts_codes = ",".join(df_basic["ts_code"][0:10])

        df = pro.daily(ts_code=ts_codes, start_date="20000104", end_date="20000107")

        return df

    @functools.cached_property
    def stock_basic_df(self):
        return StockBasic.load_stock_basic_dataframe()

    def get_stock_daily_by_name(self, name: str):
        stock = self.stock_basic_df[self.stock_basic_df["name"] == name]
        if stock.empty:
            raise ValueError(f"Stock with name {name} not found.")
        ts_code = stock["ts_code"].values[0]
        daily_filepath = StockDaily.get_daily_data_filepath(ts_code=ts_code)
        if not os.path.exists(daily_filepath):
            raise FileNotFoundError(f"Daily data file for {name} not found.")
        df_daily = pd.read_csv(daily_filepath, encoding="utf-8")
        return df_daily

    def get_stock_daily_by_code(self, ts_code: str):
        daily_filepath = StockDaily.get_daily_data_filepath(ts_code=ts_code)
        if not os.path.exists(daily_filepath):
            raise FileNotFoundError(f"Daily data file for {ts_code} not found.")
        df_daily = pd.read_csv(daily_filepath, encoding="utf-8")
        return df_daily
