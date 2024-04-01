import json
from dotenv import dotenv_values
import s3fs
import pandas as pd
import pyarrow as pa
import pyarrow.parquet as pq


class SaveS3:
    def __init__(self, json):
        self.json = json

    def write_to_minio(self):
        config = dotenv_values(".env")

        fs = s3fs.S3FileSystem(
            client_kwargs={"endpoint_url": config["MINIO_ENDPOINT"]},
            key=config["MINIO_ACCESS_KEY"],
            secret=config["MINIO_SECRET_KEY"],
            use_ssl=False,
        )

        with fs.open("testbucket/myfirsts3obj.json", "w") as f:
            json.dump(self.json, f)

        return "Successfully uploaded as object..."

    def write_to_minio_parquet(self):
        config = dotenv_values(".env")
        fs = s3fs.S3FileSystem(
            client_kwargs={"endpoint_url": config["MINIO_ENDPOINT"]},
            key=config["MINIO_ACCESS_KEY"],
            secret=config["MINIO_SECRET_KEY"],
            use_ssl=False,
        )
        dic = json.loads(str(self.json))
        df = pd.DataFrame.from_dict(dic)
        print(df)
        tb = pa.Table.from_pandas(df)
        pq.write_to_dataset(
            tb,
            "testbucket/myfirst3obj.parquet",
            filesystem=fs,
            use_dictionary=True,
            compression="snappy",
            version="2.4",
        )

        return "Successfully uploaded as parquet file"
