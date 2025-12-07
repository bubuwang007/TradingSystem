from stock_databases import StockDaily, StockBasic

# StockBasic.generate_database_file()
df = StockDaily.fetch_all_daily_data(store=True)
# df = StockDaily.update_all_daily_data()
# print(len(df))

# sd = StockDaily()
# a = sd.get_stock_daily_by_name("贵州茅台")

# from plot import K

# k = K()
# k.plot(name="贵州茅台")