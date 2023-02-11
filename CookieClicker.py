from selenium import webdriver
from time import sleep
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def click_cookies():
    service = Service(ChromeDriverManager().install())
    chrome_options = Options()
    #chrome_options.add_argument("--incognito")
    chrome_options.add_argument("--window-size=1920,1080")
    #chrome_options.add_argument("--headless")
    bobbo = webdriver.Chrome(service=service, options=chrome_options)
    bobbo.get("https://orteil.dashnet.org/cookieclicker/")
    wait = WebDriverWait(bobbo, 10)
    langue = wait.until(EC.element_to_be_clickable((By.ID, "langSelect-FR")))
    langue.click()
    sleep(5)
    bobbo.execute_script("Game.Earn(100000)")
    sleep(2)
    while (1):
        bobbo.find_element(By.ID, "bigCookie").click()
        product = bobbo.find_elements(By.XPATH, "//*[@class='product unlocked enabled']")
        CraftObject = bobbo.find_elements(By.XPATH, "//*[@class='crate upgrade enabled']")
        try:
            product[-1].click()
        except:
            pass
        try:
            CraftObject[-1].click()
        except:
            pass
    sleep(1000)

def main():
    click_cookies()


if __name__ == '__main__':
    main()