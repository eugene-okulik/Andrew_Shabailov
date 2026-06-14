import pytest
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By


@pytest.fixture
def driver():
    chrome_driver = webdriver.Chrome()
    chrome_driver.maximize_window()
    yield chrome_driver


def test_user_input(driver):
    driver.get('https://www.qa-practice.com/elements/input/simple')
    search = driver.find_element(By.NAME, 'text_string')
    search.send_keys('Python' + Keys.ENTER)
    user_input = driver.find_element(By.CLASS_NAME, 'result-text').text
    assert user_input == 'Python'
    print(user_input)
