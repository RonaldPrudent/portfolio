import time  # Used for sleep statements.  Pauses the program, so humans can see what's going on
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

# Installs the latest version of the Chromedriver for Chrome Browser automation
# driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver = webdriver.Chrome()

driver.get("https://parabank.parasoft.com/parabank/index.htm")  # Open Chrome browser to this webpage
WebDriverWait(driver, 5).until(expected_conditions.presence_of_element_located((By.ID, "loginPanel")))  # Wait up to 5 seconds for this element to appear on the page
assert driver.title == "ParaBank | Welcome | Online Banking"  # Make sure you are on the right page

# The text below should be visible on screen
assert driver.find_element(By.XPATH, "//*[@id='leftPanel']/h2").text == "Customer Login"
assert driver.find_element(By.XPATH, "//*[@id='leftPanel']/h2").is_displayed()

# The login panel should be visible on screen
assert driver.find_element(By.ID, "loginPanel").is_displayed()
assert driver.find_element(By.XPATH, "//*[@id='loginPanel']/form").is_displayed()

# Enter log in credentials
driver.find_element(By.NAME, "username").send_keys("john")
driver.find_element(By.NAME, "password").send_keys("demo")
time.sleep(3)

driver.find_element(By.CSS_SELECTOR, "[value='Log In']").click()  # Click the Log In button
time.sleep(3)

WebDriverWait(driver, 5).until(expected_conditions.presence_of_element_located((By.CLASS_NAME, "title")))
assert driver.title == "ParaBank | Accounts Overview"  # Make sure you are on the right page

# Make sure user's name is on the screen
assert driver.find_element(By.CLASS_NAME, "smallText").text == "Welcome John Smith"
assert driver.find_element(By.CLASS_NAME, "title").is_displayed()

# Make sure the correct title is appearing on the page
assert driver.find_element(By.CLASS_NAME, "title").text == "Accounts Overview"
assert driver.find_element(By.ID, "accountTable").is_displayed()

# Click the first account in the account table after making a note of the account number
accountNumber = driver.find_element(By.XPATH, "//*[@id='accountTable']/tbody/tr[1]/td[1]/a").text
driver.find_element(By.XPATH, "//*[@id='accountTable']/tbody/tr[1]/td[1]/a").click()
time.sleep(3)

WebDriverWait(driver, 5).until(expected_conditions.presence_of_element_located((By.CLASS_NAME, "title")))
assert driver.title == "ParaBank | Account Activity"
assert driver.find_element(By.CLASS_NAME, "title").is_displayed()
assert driver.find_element(By.CLASS_NAME, "title").text == "Account Details"

# Confirm that we are looking at the expected account
assert driver.find_element(By.ID, "accountDetails").is_displayed()
assert driver.find_element(By.ID, "accountId").text == accountNumber

# Confirm "About Us" appears on the page, then click it
assert driver.find_element(By.XPATH, "//*[@id='footerPanel']/ul[1]/li[2]/a").text == "About Us"
driver.find_element(By.XPATH, "//*[@id='footerPanel']/ul[1]/li[2]/a").click()
time.sleep(3)

WebDriverWait(driver, 5).until(expected_conditions.presence_of_element_located((By.CLASS_NAME, "title")))
assert driver.title == "ParaBank | About Us"
assert driver.find_element(By.CLASS_NAME, "title").is_displayed()
assert driver.find_element(By.CLASS_NAME, "title").text == "ParaSoft Demo Website"
assert driver.find_element(By.XPATH, "//*[@id='rightPanel']/p[2]").is_displayed()
assert driver.find_element(By.XPATH, "//*[@id='rightPanel']/p[2]").text == "In other words: ParaBank is not a real bank!"
time.sleep(5)

# Confirm "Log Out" appears on the screen, then click it to log out
assert driver.find_element(By.XPATH, "//*[@id='leftPanel']/ul/li[8]/a").is_displayed()
assert driver.find_element(By.XPATH, "//*[@id='leftPanel']/ul/li[8]/a").text == "Log Out"
driver.find_element(By.XPATH, "//*[@id='leftPanel']/ul/li[8]/a").click()
time.sleep(3)

# Confirm that we are back on the starting page
WebDriverWait(driver, 5).until(expected_conditions.presence_of_element_located((By.ID, "loginPanel")))
assert driver.title == "ParaBank | Welcome | Online Banking"
assert driver.find_element(By.XPATH, "//*[@id='leftPanel']/h2").text == "Customer Login"
assert driver.find_element(By.XPATH, "//*[@id='leftPanel']/h2").is_displayed()
assert driver.find_element(By.ID, "loginPanel").is_displayed()

# Make sure user's name is not on the page
assert len(driver.find_elements(By.CLASS_NAME, "smallText")) == 0
time.sleep(3)

driver.quit()  # Closes the Web Browser and shuts down this instance of the driver
