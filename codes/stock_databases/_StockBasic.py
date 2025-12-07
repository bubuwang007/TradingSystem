import os
import pandas as pd
import tushare as ts
from mtools import init_tushare


class StockBasic:

    @staticmethod
    def generate_database_file():
        init_tushare()
        pro = ts.pro_api()
        df2 = pro.stock_basic(
            exchange="",
            list_status="L",
            fields="ts_code,symbol,name,area,industry,fullname,enname,cnspell,market,exchange,curr_type,list_status,list_date,delist_date,is_hs,act_name,act_ent_type",
        )
        df2.to_csv(StockBasic.get_stock_basic_filepath(), index=False, encoding="utf-8")

    @staticmethod
    def get_stock_basic_filepath():
        p = os.path.abspath(
            os.path.join(os.path.dirname(__file__), "./files/a_stock/stock_basic.csv")
        )
        return p

    @staticmethod
    def load_stock_basic_dataframe() -> pd.DataFrame:
        p = StockBasic.get_stock_basic_filepath()
        df = pd.read_csv(p, encoding="utf-8")
        return df
