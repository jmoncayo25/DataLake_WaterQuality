import pandas as pd
import requests
from lxml import etree
from datetime import date
import numpy as np
import re

class Stocks:
    def __init__(self, stname):
        self.stname = stname
    def url(self):
        url_stocks = []
        url_base = "https://www.marketwatch.com/investing/stock/"
        for i in self.stname:
            url_stocks.append(url_base + i.replace(" ", "-").lower())
        return url_stocks

class StockDataRequester:
    def __init__(self, stocks_instance):
        self.stocks_instance = stocks_instance
    def request_data(self):
        url_stocks = self.stocks_instance.url()
        stock_responses = []
        for url in url_stocks:
            r = requests.get(url)
            stock_responses.append(r.content)
        return stock_responses

class StockDataExtractor:
    def __init__(self):
        pass
    def extract_data(self, stock_responses, stock_names):
        stock_data = {}
        for response, stock_name in zip(stock_responses, stock_names):
            tree = etree.HTML(response)
            prices = []
            dates = []
            price_changes = []
            percent_changes = []
            market_cap = []
            yield_value = []
            # Extrayendo el precio
            element_price = tree.xpath(
                "/html/body/div[3]/div[2]/div[3]/div/div[2]/h2/span"
            )
            prices.append(element_price[0].text if element_price else None)
            # Extrayendo la fecha de actualización
            element_date = tree.xpath(
                "/html/body/div[3]/div[2]/div[3]/div/div[1]/span/bg-quote"
            )
            dates.append(element_date[0].text if element_date else None)
            # Extrayendo el valor del cambio de precio
            element_price_change = tree.xpath(
                "/html/body/div[3]/div[2]/div[3]/div/div[2]/bg-quote/span[1]"
            )
            price_changes.append(
                element_price_change[0].text if element_price_change else None
            )
            # Extrayendo el porcentaje del cambio de precio
            element_percent_change = tree.xpath(
                "/html/body/div[3]/div[2]/div[3]/div/div[2]/bg-quote/span[2]"
            )
            percent_changes.append(
                element_percent_change[0].text if element_percent_change else None
            )
            # Extrayendo el market cap
            element_market_cap = tree.xpath(
                "/html/body/div[3]/div[6]/div[1]/div[1]/div/ul/li[4]/span[1]"
            )
            market_cap.append(
                element_market_cap[0].text if element_market_cap else None
            )
            # Extrayendo el yield
            element_yield = tree.xpath(
                "/html/body/div[3]/div[6]/div[1]/div[1]/div/ul/li[11]/span[1]"
            )
            yield_value.append(element_yield[0].text if element_yield else None)
            stock_data[stock_name] = {
                "Price": prices,
                "PriceChangeValue": price_changes,
                "PriceChangePercentage": percent_changes,
                "MarketCap": market_cap,
                "Yield": yield_value,
                "UpdateDate": dates,
                "QueryDate": date.today(),
            }
        return stock_data


class StockDataFrameConverter:
    def __init__(self, stock_data):
        self.stock_data = stock_data
    def to_dataframe(self):
        data = []
        for stock_name, values in self.stock_data.items():
            data.append(
                [
                    stock_name,
                    *values["Price"],
                    *values["PriceChangeValue"],
                    *values["PriceChangePercentage"],
                    *values["MarketCap"],
                    *values["Yield"],
                    *values["UpdateDate"],
                    values["QueryDate"],
                ]
            )
        columns = [
            "StockName",
            "Price",
            "PriceChangeValue",
            "PriceChangePercentage",
            "MarketCap",
            "Yield",
            "UpdateDate",
            "QueryDate",
        ]
        df = pd.DataFrame(data, columns=columns)
        return df


class StockDataCleaner:
    def __init__(self, df):
        self.df = df
    def clean_data(self):
        # Convertir 'Price' a float, manejando valores no convertibles como NaN
        self.df["Price"] = pd.to_numeric(self.df["Price"].astype(str).str.replace(",", ""), errors='coerce')
        # Aplica la misma lógica para 'PriceChangeValue', 'MarketCap', y 'PriceChangePercentage'
        self.df["PriceChangeValue"] = pd.to_numeric(self.df["PriceChangeValue"].str.replace(",", ""), errors='coerce')
        self.df["PriceChangePercentage"] = pd.to_numeric(self.df["PriceChangePercentage"].str.replace("%", ""), errors='coerce')
        # Limpiar y convertir 'Yield' a float, similarmente
        self.df["Yield"] = self.df["Yield"].astype(str).apply(lambda x: re.sub(r'%', '', x))
        self.df["Yield"] = pd.to_numeric(self.df["Yield"], errors='coerce')
        self.df["Yield"] = self.df["Yield"].replace('N/A', np.nan)
        # Intentar convertir 'UpdateDate' a datetime, manejando errores
        try:
            self.df["UpdateDate"] = pd.to_datetime(self.df["UpdateDate"], errors="coerce")
        except ValueError:
            print("Error al convertir UpdateDate. Verifica el formato.")
        return self.df
