# Reemplazando las importaciones por las clases adaptadas
from classes.water_quality_sources import WaterQualityStations
from classes.sources_data_fetcher import SourceDataFetcher
from classes.water_quality_scrap  import WaterQualityScrap
from classes.to_dataframe import ToDataFrame
from classes.transform import Transform
from classes.to_json import Tojson
from classes.saves_to_s3 import SaveS3

# ------------------ WaterQualityStations class (adaptado de Stocks)
stations = WaterQualityStations()
urls = stations.urls()

# ------------------ WaterQualityScrap class testing (adaptado de Scrap)
scrap = WaterQualityScrap(urls)
data_list = scrap.catch()

# ------------------ ToDataFrame class testing (adaptado de Todf)
to_df = ToDataFrame(data_list)
df_final = to_df.create_dataframe()
print(df_final)

# --------------- Transform class testing (simplificado para Transform)
transform = Transform(df_final)
df_transformed = transform.transform_value_and_add_audit_column()
print(df_transformed)

# -------------- Tojson class testing (adaptado para convertir DataFrame a JSON)
to_json = Tojson(df_transformed)
json_result = to_json.convert()
print(json_result)

# -------------- Save to S3
up = SaveS3(jsn)
s3_obj = up.write_to_minio_parquet()
print(s3_obj)