from selenium import webdriver
from selenium.webdriver.firefox.options import Options as FirefoxOptions
import os


def wdriver():
    # serv = Service(executable_path=r'C:\Users\Dev\Desktop\scrap')
    options = webdriver.FirefoxOptions()
    path = "/home/usanovich/Documentos/GDrive/Universidad/TAIN/Clase 5/minio-project/geckodriver-v0.34.0-linux64"
    exits = os.path.exists(path)
    print("Path-Exist:", exits)
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    wd = webdriver.Firefox()
    # wd.get('http://www.google.com/')
    # time.sleep(7)
    # wd.quit()
    return wd
