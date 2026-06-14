import pytest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture
def driver():
    chrome_driver = webdriver.Chrome()
    chrome_driver.maximize_window()
    yield chrome_driver


def test_fill_the_student_registration_form(driver):
    wait = WebDriverWait(driver, 5)

    driver.get('https://demoqa.com/automation-practice-form')
    driver.execute_script("var el = document.getElementById('fixedban'); if(el) el.style.display = 'none';")
    driver.execute_script("var el = document.querySelector('footer'); if(el) el.style.display = 'none';")

    driver.find_element(By.ID, 'firstName').send_keys('Andrew')
    driver.find_element(By.ID, 'lastName').send_keys('Shabailov')
    driver.find_element(By.ID, 'userEmail').send_keys('test@mail.com')
    driver.find_element(By.CSS_SELECTOR, "label[for='gender-radio-1']").click()
    driver.find_element(By.ID, 'userNumber').send_keys('3442434242')

    date_field = driver.find_element(By.ID, 'dateOfBirthInput')
    date_field.click()
    date_field.send_keys(Keys.CONTROL + 'a')
    date_field.send_keys("18 Nov 1992" + Keys.ENTER)

    driver.find_element(By.CSS_SELECTOR, "label[for='hobbies-checkbox-1']").click()
    driver.find_element(By.CSS_SELECTOR, "label[for='hobbies-checkbox-2']").click()
    driver.find_element(By.CSS_SELECTOR, "label[for='hobbies-checkbox-3']").click()

    subject_input = driver.find_element(By.ID, 'subjectsInput')
    driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", subject_input)
    subject_input.send_keys('Computer Science')

    option = wait.until(EC.element_to_be_clickable(
        (By.XPATH, "//div[contains(@class, 'subjects-auto-complete__option') and text()='Computer Science']"))
    )
    option.click()

    driver.find_element(By.ID, 'currentAddress').send_keys('Nice City')

    state_input = wait.until(EC.presence_of_element_located((By.ID, "react-select-3-input")))
    driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", state_input)
    state_input.send_keys('Rajasthan')
    state_input.send_keys(Keys.ENTER)

    city_input = wait.until(EC.presence_of_element_located((By.ID, "react-select-4-input")))
    city_input.send_keys('Jaipur')
    city_input.send_keys(Keys.ENTER)

    submit_btn = driver.find_element(By.ID, 'submit')
    driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", submit_btn)
    submit_btn.click()

    wait.until(EC.presence_of_element_located((By.ID, "example-modal-sizes-title-lg")))

    driver.save_screenshot('screenshot_result.png')
