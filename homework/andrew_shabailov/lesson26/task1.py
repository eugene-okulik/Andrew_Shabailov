import pytest
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture
def driver():
    chrome_driver = webdriver.Chrome()
    chrome_driver.maximize_window()
    yield chrome_driver


def test_open_first_item_in_new_tab(driver):
    driver.get('http://testshop.qa-practice.com/')
    card = driver.find_element(By.CSS_SELECTOR, 'a[href="/shop/customizable-desk-9"]')
    ActionChains(driver) \
        .key_down(Keys.CONTROL) \
        .click(card) \
        .key_up(Keys.CONTROL) \
        .perform()
    driver.switch_to.window(driver.window_handles[1])
    driver.find_element(By.CSS_SELECTOR, '.a-submit').click()

    wait = WebDriverWait(driver, 10)
    continue_btn = wait.until(EC.element_to_be_clickable(
        (By.CSS_SELECTOR, '.btn.btn-secondary'))
    )
    continue_btn.click()
    driver.close()

    driver.switch_to.window(driver.window_handles[0])
    driver.find_element(By.CSS_SELECTOR, '[href="/shop/cart"]').click()

    product_title_element = wait.until(
        EC.presence_of_element_located((By.CSS_SELECTOR, 'h6.fw-bold'))
    )

    product_text = product_title_element.text

    assert "Customizable Desk" in product_text,\
        f"Expected -'Customizable Desk', but got '{product_text}'"
