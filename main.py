import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome()
driver.set_window_size(1440, 768)
wait = WebDriverWait(driver, 10)

driver.get("https://www.twse.com.tw/zh/index.html")
actions = ActionChains(driver)
actions.move_to_element(driver.find_element(by=By.XPATH, value='//*[@id="mega"]/ul/li[2]/a')).perform()

element = wait.until(ec.element_to_be_clickable((By.XPATH, '//*[@id="mega"]/ul/li[2]/div/div/ul[1]/li[10]/a')))
element.click()

select = Select(driver.find_element(by=By.NAME, value='yy'))
select.select_by_visible_text('民國 112 年')

select = Select(driver.find_element(by=By.NAME, value='mm'))
select.select_by_visible_text('01月')
time.sleep(0.5)

input_element = driver.find_element(By.ID, 'label1')
input_element.send_keys('2')
time.sleep(0.5)
input_element.send_keys('3')
time.sleep(0.5)
input_element.send_keys('3')
time.sleep(0.5)
input_element.send_keys('0')


time.sleep(0.5)
wait.until(ec.element_to_be_clickable((By.XPATH, '//*[@id="form"]/div/div[1]/div[3]/button'))).click()

time.sleep(1)

table_body = wait.until(ec.presence_of_element_located((By.CLASS_NAME, 'is-last-page')))
rows = table_body.find_elements(By.TAG_NAME, 'tr')
for row in rows:
    columns = row.find_elements(By.TAG_NAME, 'td')
    if len(columns) > 1:
        closing_price = columns[1].text
        print(closing_price)

time.sleep(2)

screenshot_path = "full_screenshot.png"
driver.save_screenshot(screenshot_path)
driver.quit()
