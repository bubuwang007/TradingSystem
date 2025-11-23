import akshare as ak

class Companys:
    
    def get_all_companys(self):
        """
        获取所有A股上市公司基本信息
        """
        # companys_df = ak.stock_info_a_code_name()
        companys_df = ak.stock_sh_a_spot_em()
        return companys_df

companys = Companys()
all_companys_df = companys.get_all_companys()
# 转化为excel文件保存
all_companys_df.to_excel("a_share_companys.xlsx", index=False)


