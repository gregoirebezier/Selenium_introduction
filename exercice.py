from selenium import webdriver # Importation du module Selenium
from time import sleep # Importation du module time pour la fonction sleep
from selenium.webdriver.common.by import By # Importation du module By pour les éléments du navigateur
from webdriver_manager.chrome import ChromeDriverManager # Importation du module ChromeDriverManager pour le driver Chrome
from selenium.webdriver.chrome.service import Service # Importation du module Service pour le service Chrome

service1 = Service(ChromeDriverManager().install()) # Installation du driver Chrome

bobby = webdriver.Chrome(service=service1) # Création de l'objet bobby pour le navigateur Chrome

bobby.get("https://phptravels.org/") # Ouverture de la page web

buttonRegister = bobby.find_element(By.XPATH, "//a[@class='small font-weight-bold']") # Recherche de l'élément buttonRegister
buttonRegister.click() # Clic sur l'élément buttonRegister


Firstname = bobby.find_element(By.ID, "inputFirstName") # Recherche de l'élément Firstname
Firstname.send_keys("Bobby") # Envoi de la valeur Bobby dans l'élément Firstname

Lastname = bobby.find_element(By.NAME, "lastname")
Lastname.send_keys("Toto")

Email = bobby.find_elements(By.XPATH, "//input[@class='field form-control']")

for elem in Email:
    if (elem.get_attribute("name") == "email"):
        elem.send_keys("bobby@gmail.com")
        break

sleep(1000) # Pause de 1000 secondes