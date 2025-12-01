import tushare as ts
from ashare.tools import get_l3_companies_info

ts.set_token("3be1c73e47c58ec998059aa2cfe64c87e03485fba0ab10c5788372f7")

with open("test_output.txt", "w", encoding="utf-8") as f:
    for i in get_l3_companies_info("850784.SI"):
        f.write(i + "\n")
