import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


@pytest.fixture
def driver():
    chrome_driver = webdriver.Chrome()
    chrome_driver.maximize_window()
    yield chrome_driver


def test_selected_option(driver):
    driver.get(' https://the-internet.herokuapp.com/dynamic_loading/2')
    driver.find_element(By.CSS_SELECTOR, "#start button").click()

    wait = WebDriverWait(driver, 10)
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#finish h4")))

    assert driver.find_element(By.CSS_SELECTOR, "#finish h4").text == 'Hello World!'
