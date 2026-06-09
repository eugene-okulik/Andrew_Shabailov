from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


options = Options()

browser = webdriver.Chrome(options=options)
browser.maximize_window()
browser.get('https://www.qa-practice.com/elements/input/simple')

search = browser.find_element(By.NAME, 'text_string')
search.send_keys('Python' + Keys.ENTER)

user_input = browser.find_element(By.CLASS_NAME, 'result-text').text

assert user_input == 'Python'

print(user_input)
