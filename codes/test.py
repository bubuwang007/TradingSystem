from mtools import Excel2MdTable

e2t = Excel2MdTable(
    r"C:\Users\hys\Desktop\creation\TradingSystem\codes\excel\2025_12_21持仓.xlsx",
    "持仓",
)

<<<<<<< HEAD
with open("test_output.txt", "w", encoding="utf-8") as f:
    for i in get_l3_companies_info("850137.SI"):
        f.write(i + "\n")
=======
res = e2t.generate()
print(res)
>>>>>>> 8386298ef83590e5030feba8db98fe648f475b91
