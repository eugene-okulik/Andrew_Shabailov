import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.fixture
def driver():
    chrome_driver = webdriver.Chrome()
    chrome_driver.maximize_window()
    yield chrome_driver


def test_selected_option(driver):
    driver.get('https://www.qa-practice.com/elements/select/single_select')
    driver.find_element(By.NAME, 'choose_language').click()
    driver.find_element(By.CSS_SELECTOR, '#id_choose_language option[value="5"]').click()
    driver.find_element(By.CSS_SELECTOR, 'input[value="Submit"]').click()

    assert driver.find_element(By.ID, 'result-text').text == 'C#'
