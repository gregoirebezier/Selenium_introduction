#!/usr/bin/python3
from selenium import webdriver # Importation du module Selenium
from time import sleep # Importation du module time pour la fonction sleep
from selenium.webdriver.common.by import By # Importation du module By pour les éléments du navigateur
from webdriver_manager.chrome import ChromeDriverManager # Importation du module ChromeDriverManager pour le driver Chrome
from selenium.webdriver.chrome.service import Service # Importation du module Service pour le service Chrome

#Setup selenium on pc
service = Service(ChromeDriverManager().install()) # Setup du service Chrome
driver = webdriver.Chrome(service=service) # Création d'un objet driver pour le navigateur Chrome

###---------NAVIGATE TO phptravel---------###
driver.get("https://phptravels.org/") # Ouvre le navigateur et va sur le site

button = driver.find_element(By.XPATH, "//a[@class='small font-weight-bold']") # Trouve le bouton "Login" sur la page
button.click() # Clique sur le bouton "Login"
sleep(2)
name = driver.find_element(By.NAME, "firstname") # Trouve le champ "name" sur la page
name.send_keys("John") # Envoie le texte "John" dans le champ "name"

lastname = driver.find_element(By.ID, "inputLastName") # Trouve l'élément par son ID
lastname.send_keys("Doe") # Envoie le texte "Doe" dans le champ "lastname"

email = driver.find_elements(By.XPATH, "//input[@class='field form-control']") # Trouve l'élément par son XPATH
for i in email: # Boucle sur la liste des éléments trouvés
    #print(i.get_attribute("name")) #get_attribute("name") to get the name of the input (aussi possible avec id, type, etc)
    if i.get_attribute("name") == "email": # Trouve l'élément par son nom
        i.send_keys("toto@gmail.com") # Envoie le texte "toto@gmaiL.com" dans le champ "email"
        break # Sort de la boucle for

sleep(1000) # Pause de 1000 secondes