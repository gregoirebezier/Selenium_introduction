from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from time import sleep
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
    # ignore certificate errors
    add_args("--ignore-certificate-errors-spki-list")
    # ignore logs
    add_args("log-level=3")
    # choose french language
    add_args("--lang=fr")
    # set window size
    add_args("--window-size=1920,1080")
    # enable javascript
    add_args("--enable-javascript")
    # Bypass OS security model
    add_args("--no-sandbox")
    # applicable to windows os only
    add_args("--disable-gpu")
    # overcome limited resource problems
    add_args("--disable-dev-shm-usage")
    return chrome_options


def catch_cookies(driver):
    """Catch the cookies from the instagram"""
    # go to the instagram
    driver.get("https://www.instagram.com/accounts/login/")
    # save the cookies in a pickle file
    input("Press enter to save the cookies...")
    driver.refresh()
    sleep(5)
    pickle.dump(driver.get_cookies(), open("cookies_gregoire.pkl", "wb"))
    driver.quit()  # close the driver


def main():
    service = setup_service()
    chrome_options = the_options()
    driver = webdriver.Chrome(service=service, options=chrome_options)
    catch_cookies(driver)


if __name__ == "__main__":
    main()
