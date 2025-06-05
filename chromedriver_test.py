from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

def test_chrome_driver():
    options = Options()
    options.add_argument("--headless=new")  # headless mode
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)

    try:
        driver.get("https://www.google.com")
        print("Title:", driver.title)  # Should print "Google"
    finally:
        driver.quit()

if __name__ == "__main__":
    test_chrome_driver()
