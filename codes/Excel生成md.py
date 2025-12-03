from mtools import Excel2MdTable

e2t = Excel2MdTable(
    r"C:\Users\hys\Desktop\creation\TradingSystem\codes\excel\hys持仓.xlsx",
    "持仓",
    sheet_name="2025_12_2"
)

res = e2t.generate()
print(res)
