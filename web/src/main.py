from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import json
from utils import initialize_driver

driver = initialize_driver()

url = 'https://veri.bet/odds-picks?filter=upcoming' 


driver.get(url)

wait = WebDriverWait(driver, 60)
table = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="odds-picks"]/tbody')))

table_html = table.get_attribute('outerHTML')

soup = BeautifulSoup(table_html, 'html.parser')

rows = soup.find_all('tr')

formatted_data = []

for row in rows[1:]:
    cells = row.find_all(['td', 'th'])

    if len(cells) >= 10:

        cell_data = [cell.get_text(strip=True) for cell in cells]


        event_data = {
            "team1": cell_data[1],
            "team2": cell_data[7],
            "ml1": cell_data[4],
            "ml2": cell_data[5],
            "spread": cell_data[8],
            "total": cell_data[9],
        }

        formatted_data.append(event_data)

print(json.dumps(formatted_data, indent=2))

driver.quit()
