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