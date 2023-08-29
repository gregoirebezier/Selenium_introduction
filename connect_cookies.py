from time import sleep
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import pickle
from selenium import webdriver


def setup_service():
    """Setup the service for the chrome driver"""
    # install the chrome driver and return the service
    return Service(ChromeDriverManager().install())


def the_options():
    """The options for the chrome driver"""
    chrome_options = Options()
    add_args = chrome_options.add_argument
    # headless mode, without the visual interface
    # add_args("--headless")
    # ignore certificate errors
    add_args("--ignore-certificate-errors-spki-list")
    # ignore logs
    add_args("log-level=3")
    # choose french language
    add_args("--lang=fr")
    # enable javascript
    add_args("--enable-javascript")
    # Bypass OS security model
    add_args("--no-sandbox")
    # applicable to windows os only
    add_args("--disable-gpu")
    # overcome limited resource problems
    add_args("--disable-dev-shm-usage")
    return chrome_options


def setup_chromedriver():
    """Setup the chrome driver"""
    # setup the service
    service = setup_service()
    # get the options
    chrome_options = the_options()
    # create the driver
    driver = webdriver.Chrome(service=service, options=chrome_options)
    return driver


def load_cookies(driver, link):
    """Load the cookies from the pickle file"""
    # go to the link to load the cookies
    driver.get(link)
    # load the cookies from the pickle file
    cookies = pickle.load(open("cookies_gregoire.pkl", "rb"))
    for cookie in cookies:
        # add the cookies to the driver
        driver.add_cookie(cookie)
    # refresh the page
    driver.refresh()
    return driver


def setup_global(link):
    """Setup the global variables"""
    # setup the chrome driver
    driver = setup_chromedriver()
    try:
        # load the cookies
        driver = load_cookies(driver, link)
    except:  # noqa
        exit()
    return driver


def main():
    """Main function"""
    # setup selenium and cookies
    driver = setup_global("https://www.instagram.com/accounts/login/")
    # get the statistics
    sleep(1000)
    return driver


main()
