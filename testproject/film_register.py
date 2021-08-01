from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import NoSuchElementException
import time

driver = webdriver.Chrome(ChromeDriverManager().install())

# weblap megkeresése
driver.get("https://witty-hill-0acfceb03.azurestaticapps.net/film_register.html")
time.sleep(3)

# TC02 új film felvétele, Register gomb megnyomása
button_register = driver.find_element_by_xpath('/html/body/div[2]/div[1]/button')
button_register.click()
time.sleep(3)

# Teszt adatok felvitele, Save gomb megnyomása
film_title_value = "Black widow"
release_year_value = "2021"
chronological_year_value = "2020"
trailer_url_value = "https://www.youtube.com/watch?v=Fp9pNPdNwjI"
image_url_value = "https://m.media-amazon.com/images/I/914MHuDfMSL._AC_UY327_FMwebp_QL65_.jpg"
film_summary_url_value = "https://www.imdb.com/title/tt3480822/"

driver.find_element_by_id('nomeFilme').send_keys(film_title_value)
driver.find_element_by_id('anoLancamentoFilme').send_keys(release_year_value)
driver.find_element_by_id('anoCronologiaFilme').send_keys(chronological_year_value)
driver.find_element_by_id('linkTrailerFilme').send_keys(trailer_url_value)
driver.find_element_by_id('linkImagemFilme').send_keys(image_url_value)
driver.find_element_by_id('linkImdbFilme').send_keys(film_summary_url_value)
time.sleep(3)

driver.find_element_by_xpath('/html/body/div[2]/div[2]/fieldset/button[1]').click()

# Teszt film képének megkeresése
driver.find_element_by_xpath('//img[@alt="Black widow"]').click()
