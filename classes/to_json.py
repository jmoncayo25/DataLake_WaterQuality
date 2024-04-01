import json
import pandas as pd


class Tojson:
    def __init__(self, data) -> None:
        self.data = data

    def convert(self):
        if isinstance(self.data, pd.DataFrame):
            # If data is a DataFrame, use the to_json method
            json_str = self.data.to_json()
        elif isinstance(self.data, dict):
            # If data is a dictionary, use json.dumps
            json_str = json.dumps(self.data)
        else:
            raise TypeError("Unsupported type for conversion")
        return json_str
