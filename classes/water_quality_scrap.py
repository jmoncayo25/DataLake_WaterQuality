import time
from bs4 import BeautifulSoup as bs
from lxml import etree
from functions.webdriver import wdriver

class WaterQualityScrap:
    def __init__(self, urls):
        self.urls = urls
    def catch(self):
        data_all = []
        wd = wdriver()
        for url in self.urls:
            codigo_fuente = url.split('/')[-1]  # Asume que el código fuente es el último segmento de la URL
            wd.get(url)
            time.sleep(7)  # Espera para asegurar que la página haya cargado completamente
            soup = bs(wd.page_source, "lxml")
            p_s = etree.HTML(str(soup))
            # Extracción de valores y unidades
            parametros = {
                "Caudal": {
                    "xpath_valor": "/html/body/div[1]/div/div/div/div[4]/main/div/div/div/div[2]/div/div/div[1]/div[2]/div/div/div[1]/div[2]/div/@title",
                    "xpath_unidad": "/html/body/div[1]/div/div/div/div[4]/main/div/div/div/div[2]/div/div/div[1]/div[2]/div/div/div[1]/div[3]/div/@title"
                },
                "pH": {
                    "xpath_valor": "/html/body/div[1]/div/div/div/div[4]/main/div/div/div/div[2]/div/div/div[1]/div[2]/div/div/div[5]/div[2]/div/@title",
                    "xpath_unidad": "/html/body/div[1]/div/div/div/div[4]/main/div/div/div/div[2]/div/div/div[1]/div[2]/div/div/div[5]/div[3]/div/@title"
                },
                "Turbidez": {
                    "xpath_valor": "/html/body/div[1]/div/div/div/div[4]/main/div/div/div/div[2]/div/div/div[1]/div[2]/div/div/div[15]/div[2]/div/@title",
                    "xpath_unidad": "/html/body/div[1]/div/div/div/div[4]/main/div/div/div/div[2]/div/div/div[1]/div[2]/div/div/div[15]/div[3]/div/@title"
                }
            }
            for parametro, paths in parametros.items():
                valor = p_s.xpath(paths["xpath_valor"])[0]
                unidad = p_s.xpath(paths["xpath_unidad"])[0]
                data_all.append({
                    "codigo_fuente": codigo_fuente,
                    "parametro": parametro,
                    "valor": valor,
                    "unidad": unidad,
                })
        return data_all