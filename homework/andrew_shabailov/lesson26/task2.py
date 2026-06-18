import pytest
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture
def driver():
    chrome_driver = webdriver.Chrome()
    chrome_driver.maximize_window()
    yield chrome_driver


def test_user_choice(driver):
    driver.get('http://testshop.qa-practice.com/')
    card = driver.find_element(By.CSS_SELECTOR, 'a[href="/shop/customizable-desk-9"]')
    actions = ActionChains(driver)
    actions.move_to_element(card).perform()

    wait = WebDriverWait(driver, 10)
    cart_btn = wait.until(EC.element_to_be_clickable(
        (By.CSS_SELECTOR, ':has([content="Customizable Desk"]) .a-submit'))
    )
    cart_btn.click()

    product_text = wait.until(EC.presence_of_element_located(
        (By.CSS_SELECTOR, 'td>strong.product_display_name'))
    ).text

    assert "Customizable Desk" in product_text, \
        f"Expected -'Customizable Desk', but got '{product_text}'"
