class Stocks:
    def __init__(self, stname):
        self.stname = stname
    def url(self):
        url_stocks = []
        # url_base = 'https://www.marketwatch.com/investing/stock/'
        for i in self.stname:
            # url_stocks.append(url_base + i)
            url_stocks.append(f"https://www.tradingview.com/symbols/BVC-{i}/")
        stocks_and_urls = [self.stname, url_stocks]
        return stocks_and_urls

class WaterQualitySources:
    def __init__(self, station_code_base="BARQ", start=4, end=8):
        self.station_code_base = station_code_base
        self.start = start
        self.end = end
    def urls(self):
        base_url = "https://piragua.corantioquia.gov.co/geoportal/fisicoquimico/"
        urls = []
        for i in range(self.start, self.end + 1):
            station_code = f"{self.station_code_base}{str(i).zfill(2)}"
            full_url = f"{base_url}{station_code}"
            urls.append(full_url)
        return urls