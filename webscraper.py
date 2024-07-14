from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import pandas as pd

# Initialize the Selenium WebDriver (Chrome in this example)
driver = webdriver.Chrome()

# Open the Zillow page
driver.get('https://www.zillow.com/alexandria-va/rentals/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22isMapVisible%22%3Atrue%2C%22mapBounds%22%3A%7B%22north%22%3A38.88889516454313%2C%22south%22%3A38.67934578643801%2C%22east%22%3A-76.9912824885254%2C%22west%22%3A-77.22851851147462%7D%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A10071%2C%22regionType%22%3A6%7D%5D%2C%22filterState%22%3A%7B%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22price%22%3A%7B%22min%22%3A0%2C%22max%22%3A440797%7D%2C%22mp%22%3A%7B%22min%22%3A0%2C%22max%22%3A2200%7D%2C%22sf%22%3A%7B%22value%22%3Afalse%7D%2C%22ah%22%3A%7B%22value%22%3Atrue%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A12%2C%22usersSearchTerm%22%3A%22Alexandria%2C%20VA%22%7D')

# Wait for the dynamic content to load (you may need to adjust the selector and wait time)
try:
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, 'list-card-info'))
    )
finally:
    # Get the page source
    page_source = driver.page_source

    # Close the driver
    driver.quit()

# Parse the page source with BeautifulSoup
soup = BeautifulSoup(page_source, 'html.parser')

# Extract data (example for extracting property titles)
titles = [title.get_text() for title in soup.find_all(class_='list-card-info')]

# Convert to DataFrame
df = pd.DataFrame(titles, columns=['Title'])

# Print the DataFrame
print(df)
