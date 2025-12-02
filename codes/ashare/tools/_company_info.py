import tushare as ts


def get_l3_companies_info(l3_code: str):
    pro = ts.pro_api()
    df1 = pro.index_member_all(l3_code=l3_code)
    for i in df1["name"]:
        print(i)
    df2 = pro.stock_basic(exchange="", list_status="L", fields="ts_code,name")

    for i in df1["name"]:
        stock = df2[df2["name"] == i]
        if stock.empty:
            yield f"## {i}\n\n公司状态异常。\n"
            continue

        try:
            cmp = pro.stock_company(
                ts_code=stock["ts_code"].values[0],
                fields="introduction,website,main_business,business_scope",
            )
        except Exception:
            import time
            time.sleep(65)
            cmp = pro.stock_company(
                ts_code=stock["ts_code"].values[0],
                fields="introduction,website,main_business,business_scope",
            )

        intro = "\n\n".join(
            [
                f"**公司名称：** {i}",
                f"**TS代码：** {stock['ts_code'].values[0]}",
                f"**公司简介：** {cmp['introduction'].values[0]}",
                f"**公司官网：** {cmp['website'].values[0]}",
                f"**主营业务：** {cmp['main_business'].values[0]}",
                f"**经营范围：** {cmp['business_scope'].values[0]}",
            ]
        )

        yield f"## [{i}](/A股/公司/{i}.md)\n\n" + intro + "\n"
        # yield f'<LinkCard title="{i}" href="/A股/公司/{i}.md">\n\n{intro}</LinkCard>'
