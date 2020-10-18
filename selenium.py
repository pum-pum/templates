from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep

options = Options()
options.binary_location = 'C:\\Users\\exp\\software\\chromium\\chrome-win\\chrome.exe'
driver_path = 'C:\\Users\\exp\\software\\chromedriver\\chromedriver_win32\\chromedriver.exe'
browser = webdriver.Chrome(options = options, executable_path = driver_path)
browser.get('https://example.com')

sleep(2)

browser.find_element_by_class_name("").send_keys('')
browser.find_element_by_class_name("").send_keys('')

sleep(3)

button=browser.find_element_by_class_name("")


sleep(30)

browser.close()
#browser.exit()


