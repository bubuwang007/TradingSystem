from stock_databases import StockBasic

df = StockBasic.load_stock_basic_dataframe()
print(df.head())