from mtools import get_l3_companies_info

with open("test_output.txt", "w", encoding="utf-8") as f:
    for i in get_l3_companies_info("850832.SI"):
        f.write(i + "\n")
