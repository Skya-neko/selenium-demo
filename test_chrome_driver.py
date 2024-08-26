import time

from selenium import webdriver


driver = webdriver.Chrome()  # Optional argument, if not specified will search path.

driver.get("http://www.google.com/")

time.sleep(5)  # Let the user actually see something!

search_box = driver.find_element("name", "q")

search_box.send_keys("ChromeDriver")

search_box.submit()

time.sleep(5)  # Let the user actually see something!

driver.quit()

# %%
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.get("http://www.python.org")
assert "Python" in driver.title
elem = driver.find_element(By.NAME, "q")
elem.clear()
elem.send_keys("pycon")
elem.send_keys(Keys.RETURN)
assert "No results found." not in driver.page_source
driver.close()

# %%
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("")
assert "Python" in driver.title
elem = driver.find_element(By.NAME, "download")
for i in elem.get_attribute("href"):
    print(i)
elem.clear()
elem.send_keys("pycon")
elem.send_keys(Keys.RETURN)
assert "No results found." not in driver.page_source
driver.close()

# %%
