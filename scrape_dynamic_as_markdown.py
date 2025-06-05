from mcp.server.fastmcp import FastMCP
from bs4 import BeautifulSoup
from markdownify import markdownify as md
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import base64
import os
import tempfile
import time
from webdriver_manager.chrome import ChromeDriverManager  


mcp = FastMCP("dynamic_scraper")

def get_driver():
    options = Options()
    options.binary_location = r"C:\Program Files\Google\Chrome\Application\chrome.exe"  # Example for Windows

    options.add_argument("--headless=new")
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    
    
    # ✅ Use webdriver-manager to auto-install and configure ChromeDriver
    service = Service(ChromeDriverManager().install())
    return webdriver.Chrome(service=service, options=options)

@mcp.tool()
async def scrape_dynamic_as_markdown(url: str, wait_time: int = 3) -> str:
    """
    Scrape a dynamically-rendered webpage using Selenium and return Markdown.
    `wait_time`: seconds to wait for JS content to load (default: 3s).
    """
    print("Debugging: Launching dynamic scraper...")

    try:
        driver = get_driver()
        driver.get(url)
        time.sleep(wait_time)  # Wait for JS to render

        html = driver.page_source
        soup = BeautifulSoup(html, "html.parser")

        # Clean JS/CSS
        for tag in soup(["script", "style"]):
            tag.decompose()

        content = soup.body or soup
        markdown = md(str(content))
        print(f"Debugging: scraped content... {markdown[:100]}")
        driver.quit()
        return markdown

    except Exception as e:
        return f"Error: {str(e)}"
    

if __name__ == "__main__":
    mcp.run()
