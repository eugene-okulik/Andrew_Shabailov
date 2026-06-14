from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains


options = Options()

browser = webdriver.Chrome(options=options)
browser.maximize_window()

wait = WebDriverWait(browser, 2)

browser.get('https://demoqa.com/automation-practice-form')

browser.execute_script("var el = document.getElementById('fixedban'); if(el) el.style.display = 'none';")
browser.execute_script("var el = document.querySelector('footer'); if(el) el.style.display = 'none';")

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

subject_input = browser.find_element(By.ID, 'subjectsInput')
browser.execute_script("arguments[0].scrollIntoView({block: 'center'});", subject_input)
subject_input.send_keys('Computer Science')

option = wait.until(EC.element_to_be_clickable(
    (By.XPATH, "//div[contains(@class, 'subjects-auto-complete__option') and text()='Computer Science']"))
)
actions = ActionChains(browser)
actions.move_to_element(option).click().perform()

browser.find_element(By.ID, 'currentAddress').send_keys('Nice City')

state_input = wait.until(EC.presence_of_element_located((By.ID, "react-select-3-input")))
browser.execute_script("arguments[0].scrollIntoView({block: 'center'});", state_input)
state_input.send_keys('Rajasthan')
state_input.send_keys(Keys.TAB)

city_input = wait.until(EC.presence_of_element_located((By.ID, "react-select-4-input")))
city_input.send_keys('Jaipur')
city_input.send_keys(Keys.TAB)

browser.find_element(By.ID, 'submit').click()

browser.save_screenshot('screenshot_result.png')
