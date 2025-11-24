import tushare as ts

ts.set_token('3be1c73e47c58ec998059aa2cfe64c87e03485fba0ab10c5788372f7')
pro = ts.pro_api()

df = pro.index_member_all(l3_code='851931.SI')

for i in df['name']:

    print(f'<LinkCard title="{i}" href="/A股/公司/{i}.md" description="{todo}"/>')