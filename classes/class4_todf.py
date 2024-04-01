import pandas as pd

class ToDataFrame:
    def __init__(self, data_list):
        self.data_list = data_list
    def create_dataframe(self):
        df = pd.DataFrame(self.data_list)
        return df