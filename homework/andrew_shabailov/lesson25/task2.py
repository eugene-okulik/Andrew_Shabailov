from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


options = Options()
options.add_experimental_option(name='detach', value=True)

browser = webdriver.Chrome(options=options)
browser.maximize_window()

wait = WebDriverWait(browser, 2)

browser.get('https://demoqa.com/automation-practice-form')

browser.find_element(By.ID, 'firstName').send_keys('Andrew')
browser.find_element(By.ID, 'lastName').send_keys('Shabailov')
browser.find_element(By.ID, 'userEmail').send_keys('test@mail.com')
browser.find_element(By.CSS_SELECTOR, "label[for='gender-radio-1']").click()
browser.find_element(By.ID, 'userNumber').send_keys('3442434242')

date_field = browser.find_element(By.ID, 'dateOfBirthInput')
date_field.click()
date_field.send_keys(Keys.CONTROL + 'a')
date_field.send_keys("18 Nov 1992" + Keys.ENTER)

browser.find_element(By.CSS_SELECTOR, "label[for='hobbies-checkbox-1']").click()
browser.find_element(By.CSS_SELECTOR, "label[for='hobbies-checkbox-2']").click()
browser.find_element(By.CSS_SELECTOR, "label[for='hobbies-checkbox-3']").click()

browser.find_element(By.ID, 'currentAddress').send_keys('Nice City')

state_input = wait.until(EC.presence_of_element_located((By.ID, "react-select-3-input")))
browser.execute_script("arguments[0].scrollIntoView({block: 'center'});", state_input)
state_input.send_keys('Rajasthan' + Keys.ENTER)

city_input = wait.until(EC.presence_of_element_located((By.ID, "react-select-4-input")))
city_input.send_keys('Jaipur' + Keys.ENTER)

subject_input = browser.find_element(By.ID, 'subjectsInput')
browser.execute_script("arguments[0].scrollIntoView({block: 'center'});", subject_input)
subject_input.send_keys('Computer Science' + Keys.ENTER)
