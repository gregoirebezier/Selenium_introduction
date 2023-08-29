from selenium import webdriver
from time import sleep
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service


def Instagram():
    service = Service(ChromeDriverManager().install())
    chrome_options = Options()
    chrome_options.add_argument("--ignore-certificate-errors-spki-list")
    chrome_options.add_argument(
        f"--user-data-dir=C:\\Users\\bezie\\AppData\\Local\\Google\\Chrome\\User Data\\Default1"
    )
    chrome_options.add_argument("log-level=3")
    driver = webdriver.Chrome(service=service, options=chrome_options)
    driver.get("https://www.instagram.com/accounts/login/")
    driver.set_page_load_timeout(30)

    driver.maximize_window()
    sleep(1000)


def main():
    Instagram()


main()
