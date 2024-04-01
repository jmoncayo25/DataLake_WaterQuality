from classes.class1_stocks import Stocks

# from classes.class2_requests import Requests
from classes.class3_scrap import Scrap
from classes.class4_todf import Todf
from classes.class5_transform import Transform
from classes.class6_tojson import Tojson
from classes.class7_saves3 import SaveS3


# ------------------Stocks class testing
stocks = Stocks(["NUTRESA", "PROMIGAS", "GRUBOLIVAR", "BCOLOMBIA"])
list_st_urls = stocks.url()
# print(list_st_urls)

# ------------------Requests class testing
# objReq = Requests(list_st_urls)
# objReq_r = objReq.req()
# print(objReq_r[0])

# ------------------Scrap class testing
scrap_1 = Scrap(list_st_urls)
dict = scrap_1.catch()
# print(dict)

# ------------------Todf class testing
df = Todf(dict)
df_1_wTrans = df.dframe()
print(df_1_wTrans)

# ---------------Transform (df_wTrans) class testing
transf_0 = Transform(df_1_wTrans)
df_col_with_dates_trans = transf_0.str_to_datetime()
transf_1 = Transform(df_col_with_dates_trans)
df_Trans = transf_1.multi_transf()
print(df_Trans)

# --------------Tojson (df_Trans) class testing
obj = Tojson(df_Trans)
jsn = obj.convert()
print(jsn)

# --------------SaveS3 class testing
""" up = SaveS3(jsn)
s3_obj = up.write_to_minio()
print(s3_obj) """

up = SaveS3(jsn)
s3_obj = up.write_to_minio_parquet()
print(s3_obj)
