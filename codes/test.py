from mtools import Excel2MdTable

e2t = Excel2MdTable(
    r"C:\Users\hys\Desktop\creation\TradingSystem\codes\excel\2025_12_21持仓.xlsx",
    "持仓",
)

res = e2t.generate()
print(res)
