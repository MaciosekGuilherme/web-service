from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService

def initialize_driver():
    chromedriver_path = './drivers/chromedriver.exe'
    chrome_service = ChromeService(executable_path=chromedriver_path)
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--headless')
    return webdriver.Chrome(service=chrome_service, options=chrome_options)
