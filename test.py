from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Initialize Chrome WebDriver with options to block notifications
chrome_options = Options()

# Disable notifications
chrome_options.add_argument("--disable-notifications")

# Initialize the WebDriver with the options
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

# URL of the OTT platform (Replace this with the actual URL of the platform you are testing)
url = "https://sundirectgo.in/"  # Replace with the actual URL

# Credentials for login (replace with real credentials)
username = "**********" #mobile number
password = "**********" #password

def login():
    # Open the OTT platform's login page
    driver.get(url)

    # Wait for the page to load and the profile image to appear
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "profile_img")))

    # Step 1: Click the "Profile Image" to open the login menu
    profile_img = driver.find_element(By.ID, "profile_img")
    profile_img.click()

    # Wait for the login popup to appear
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "Loginpopup")))

    # Step 2: Click the "Sign In / Register" button
    login_popup = driver.find_element(By.ID, "Loginpopup")
    login_popup.click()

    # Wait for the login fields to be visible
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.NAME, "email")))
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.NAME, "password")))

    # Step 3: Locate the username and password fields by name
    username_field = driver.find_element(By.NAME, "email")  # Mobile Number field
    password_field = driver.find_element(By.NAME, "password")  # Password field

    # Step 4: Enter credentials
    username_field.send_keys(username)
    password_field.send_keys(password)

    # Step 5: Locate and click the login button using a more specific method
    try:
        # Attempt to find the login button by its XPath (modify if needed)
        login_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']"))
        )
        login_button.click()
    except Exception as e:
        print(f"Error clicking login button: {e}")

    # Wait for the next page to load or verify successful login
    try:
        # Wait for the profile icon to appear after login (increase the timeout)
        WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "profile-icon")))  # Check for successful login element
        print("Login successful!")
    except Exception as e:
        print(f"Login failed: {e}")
        driver.quit()

def main():
    # Perform login
    login()

    # Close the browser after the test
    driver.quit()

if __name__ == "__main__":
    main()
