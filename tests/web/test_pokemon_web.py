import pytest
import requests

from loguru import logger
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC 

URL = "https://pokemonbattle-stage.ru/"

def test_browser():
    """
    TRP-1. Open browser
    """
    chrome_options = Options()
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("start-maximized") # открываем на полный экран
    chrome_options.add_argument("--disable-infobars") # отключаем инфо сообщения
    chrome_options.add_argument("--disable-extensions") # отключаем расширения
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--disable-search-engine-choice-screen") # отключаем выбор движка для поиска
    # chrome_options.add_argument("--headless") # спец. режим "без браузера"

    service = Service()
    driver = webdriver.Chrome(service=service, options=chrome_options)

    driver.get(URL)

    email_input = WebDriverWait(driver,timeout=10,poll_frequency=2).until(EC.element_to_be_clickable((By.CSS_SELECTOR,'[class*="f_email"]')))
    email_input.click()
    email_input.send_keys('koteika19922@yandex.ru')

    password_input = driver.find_element(by=By.ID, value= 'password')
    password_input.click()
    password_input.send_keys('35Ezipin')

    button = driver.find_element(by=By.CSS_SELECTOR, value='[class="auth_button k_form_send_auth"]')   
    button.click()

    trainer_id = driver.find_element(by=By.CSS_SELECTOR, value='[class="header__id-text"]')

    text_id = trainer_id.text.replace('\n,' '')

    assert True, ''

 # button = WebDriverWait(driver, timeout=10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '[class=class="auth__button k_form_send_auth"]')))
 # button_input = driver.find_element(by=By.CSS_SELECTOR, value='[class="auth_button k_form_send_auth"]')

