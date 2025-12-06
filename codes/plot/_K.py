import functools
import pandas as pd
import mplfinance as mpf
from stock_databases import StockDaily


class K:

    @functools.cached_property
    def stock_daily(self):
        return StockDaily()

    def plot(self, *, name: str = None, ts_code: str = None):
        if name is not None:
            df = self.stock_daily.get_stock_daily_by_name(name)
        elif ts_code is not None:
            df = self.stock_daily.get_stock_daily_by_code(ts_code)
        else:
            raise ValueError("Either name or ts_code must be provided.")
        
        import matplotlib
        import matplotlib.pyplot as plt

        matplotlib.rcParams['font.sans-serif'] = ['SimHei']  # 黑体
        matplotlib.rcParams['axes.unicode_minus'] = False    # 负号正常显示

        df['trade_date'] = pd.to_datetime(df['trade_date'])
        df = df.sort_values('trade_date')
        df = df.tail(20)
        df.set_index('trade_date', inplace=True)

        df = df.rename(columns={
            'open': 'Open',
            'high': 'High',
            'low': 'Low',
            'close': 'Close',
            'vol': 'Volume'
        })

        mpf.plot(
            df,
            type='candle',
            volume=True,
            style='charles',     # 可换成 'yahoo' 等
            title='000001.SZ K线图',
            mav=(5, 10, 20)       # 移动均线
        )

