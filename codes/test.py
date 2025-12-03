from stock_databases import StockBasic

<<<<<<< HEAD
e2t = Excel2MdTable(
    r"E:\股票\持仓记录\12月持仓记录.xlsx",
    "持仓",
    sheet_name="12.02"
)

res = e2t.generate()
print(res)
=======
df = StockBasic.load_stock_basic_dataframe()
print(df.head())
>>>>>>> 61228578e79ca6932f307cedcc6cc17795273bc7
