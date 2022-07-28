import requests
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class PokemonMap():
    def get_store_info(self, index):
        response = requests.get('https://tw.portal-pokemon.com/cardmap/api/poi?uuid=e24f6ca8-d2cc-4f9b-8ec0-34b4765f94c3&bounds=23.966175871265033,120.14648437500001,24.44714958973082,121.37695312499999&zoom=11&_=1658799601894')
        return response.json()[index]

    def go_to_pokemon_map_page(self, driver):
        driver.get("https://tw.portal-pokemon.com/cardmap/map?cl=1")

    def search_store_by_name(self, driver, name):
        driver.find_element(By.XPATH,'//*[@id="map-wrapper"]/div[2]/div/div[1]/div/form/div/input').click()
        driver.find_element(By.XPATH,'//*[@id="map-wrapper"]/div[2]/div/div[1]/div/form/div/input').send_keys(name)
        driver.find_element(By.XPATH,'//*[@id="map-wrapper"]/div[2]/div/div[1]/div/div[1]/ul/li[2]').click()
        driver.find_element(By.XPATH,'//*[@id="map-wrapper"]/div[2]/div/div[1]/div/form/div/div[1]').click()

    def get_store_name_by_index(self, driver, index):
        xpath = f'//*[@id="map-wrapper"]/div[2]/div/div[2]/div[2]/ul/li[{index}]/div/div[1]'

        WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH,xpath)))
        return driver.find_element(By.XPATH, xpath).text