"""
IKEA Stock Checker

This module provides functionality to check the stock availability of IKEA products
on the IKEA Hong Kong website using web scraping techniques with Selenium.

The main function, check_stock, takes a product URL and returns a boolean indicating
whether the product is in stock.

Usage:
    python ikea_stock_checker.py

Dependencies:
    - selenium
    - python-dotenv

Environment Variables:
    IKEA_PRODUCT_URL: The URL of the IKEA product to check
"""

import os
import sys
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException, WebDriverException

def clean_text(text: str) -> str:
    """
    Remove all whitespace from a string.

    Args:
        text (str): The input string to clean.

    Returns:
        str: The input string with all whitespace removed.
    """
    return ' '.join(text.split())

def get_headless_driver() -> webdriver.Chrome:
    """
    Create and return a headless Chrome WebDriver instance.

    Returns:
        webdriver.Chrome: A headless Chrome WebDriver instance.
    """
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-gpu")  # Required for some systems
    chrome_options.add_argument("--no-sandbox")  # Required for running Chrome as root
    chrome_options.add_argument("--disable-dev-shm-usage")  # Overcome limited resource problems
    return webdriver.Chrome(options=chrome_options)

def check_stock(item_url: str, timeout=10) -> bool:
    """
    Check if an IKEA product is in stock using a headless Chrome browser.

    This function uses Selenium with a headless Chrome browser to scrape the IKEA 
    product page and check if the product is currently in stock.

    Args:
        item_url (str): The URL of the IKEA product page to check.
        timeout (int, optional): Maximum time in seconds to wait for page elements. 
                                 Defaults to 10.

    Returns:
        bool: True if the product is in stock, False otherwise or if an error occurs.

    Raises:
        TimeoutException: If the page takes too long to load.
        NoSuchElementException: If the required elements are not found on the page.
        WebDriverException: For Selenium WebDriver related errors.
    """
    driver = get_headless_driver()
    try:
        driver.get(item_url)

        sidebar = WebDriverWait(driver, timeout).until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, ".container.template_detail")
        ))

        status_labels = sidebar.find_elements(By.CLASS_NAME, "status__label")

        for label in status_labels:
            text = clean_text(label.text)
            if "存貨" in text:
                return True

        return False

    except TimeoutException:
        print(f"Timeout: The element was not found within {timeout} seconds")
    except NoSuchElementException:
        print("Error: Required element not found on the page")
    except WebDriverException as e:
        print(f"WebDriver error occurred: {str(e)}")
    finally:
        driver.quit()

    return False


if __name__ == "__main__":
    load_dotenv()

    URL = os.getenv('IKEA_PRODUCT_URL')

    if not URL:
        print("Error: IKEA_PRODUCT_URL environment variable is not set.")
        sys.exit(1)

    print(f"Checking stock for {URL}")
    HAS_STOCK = check_stock(URL)
    print(f"Stock available: {HAS_STOCK}")
