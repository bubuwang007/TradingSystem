from mtools import Excel2MdTable

e2t = Excel2MdTable(r"E:\股票\持仓记录\12月持仓记录.xlsx", "持仓", sheet_name="12.12")

res = e2t.generate()
print(res)
