from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import pytest
import os
import random
import time

def singup_case():
    
    name_i = input("Escriba un nombre: ")
    last_name_i = input("Escriba un apellido: ")
    email_i = input("Escriba un correo electronico: ")
    password_i = input("Escriba una contrasena: ")

    service = Service(executable_path=("chromedriver.exe"))
    
    chrome_options = Options()
    chrome_options.add_argument("--disable-notifications")
    
    driver = webdriver.Chrome(service = service, options = chrome_options)

    driver.maximize_window()
    driver.get("https://facebook.com/register")
    time.sleep(2)

    #NAME
    WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.NAME, 'firstname'))
    )
    first_n = driver.find_element(By.NAME, 'firstname')
    first_n.send_keys(name_i)
    time.sleep(2)

    #LASTNAME
    last_n = driver.find_element(By.NAME, 'lastname')
    last_n.send_keys(last_name_i)
    time.sleep(2)

    #EMAIL
    email = driver.find_element(By.NAME, 'reg_email__')
    email.send_keys(email_i)
    time.sleep(2)

    WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.NAME, 'reg_email_confirmation__'))
    )
    email_confirmation = driver.find_element(By.NAME, 'reg_email_confirmation__')
    email_confirmation.send_keys(email_i)
    time.sleep(2)

    #PASSWORD
    password = driver.find_element(By.NAME, 'reg_passwd__')
    password.send_keys(password_i)
    time.sleep(2)

    #MONTH
    month = driver.find_element(By.NAME, "birthday_month")
    month.click()

    random_month = str(random.randint(1, 12))
    month_xpath = '//*[@id="month"]/option[' + random_month + ']'
    WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.XPATH, month_xpath))
    )
    month_option = driver.find_element(By.XPATH, month_xpath)
    month_option.click()
    time.sleep(2)

    #DATE
    day = driver.find_element(By.NAME, "birthday_day")
    day.click()

    random_day = str(random.randint(1, 28))
    day_xpath = '//*[@id="day"]/option[' + random_day + ']'
    WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.XPATH, day_xpath))
    )
    day_option = driver.find_element(By.XPATH, day_xpath)
    day_option.click()
    time.sleep(2)    

    #YEAR
    year = driver.find_element(By.NAME, "birthday_year")
    year.click()

    random_year = str(random.randint(14, 45))
    year_xpath = '//*[@id="year"]/option[' + random_year + ']'
    WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.XPATH, year_xpath))
    )
    year_option = driver.find_element(By.XPATH, year_xpath)
    year_option.click()
    time.sleep(2)

    #SEX
    sex = driver.find_element(By.CLASS_NAME, "_58mt")
    sex.click()
    time.sleep(2)

    #SIGNUP BUTTON
    signup = driver.find_element(By.NAME, "websubmit")
    signup.click()
    time.sleep(60)

def login_case():

    #CUENTA A USAR
    email_list = ["lajaibaloca47@gmail.com", "jukachakajukajuka@gmail.com"]
    password_list = ["lajaibaloca47.", "jukachaka."]
    email = random.choice(email_list)
    if test_case == "B" or test_case == "b":
        password = random.choice(password_list)
    else:
        password = password_list[email_list.index(email)]
    print(email)
    email_index = email_list.index(email)
    print(email_index)
    print(password)
    password_index = password_list.index(password)
    print(password_index)
    time.sleep(3)
    
    service = Service(executable_path=("chromedriver.exe"))
    
    chrome_options = Options()
    chrome_options.add_argument("--disable-notifications")
    
    driver = webdriver.Chrome(service = service, options = chrome_options)

    driver.maximize_window()
    driver.get("https://www.facebook.com/")
    time.sleep(2)

    #ESCRIBIR EMAIL
    WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="email"]'))
    )
    email_box = driver.find_element(By.XPATH, '//*[@id="email"]')
    email_box.send_keys(email)
    time.sleep(2)

    #ESCRIBIR CONTRASENA
    WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="pass"]'))
    )
    password_box = driver.find_element(By.XPATH, '//*[@id="pass"]')
    password_box.send_keys(password)
    time.sleep(2)

    #ACCEDER A LA CUENTA
    login_button = driver.find_element(By.NAME, "login")
    login_button.click()
    time.sleep(5)
    
    if email_index == password_index:
        #IR A LA PAGINA PRINCIPAL
        WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'a[aria-label="Facebook"]'))
        )
        menu_button = driver.find_element(By.CSS_SELECTOR, 'a[aria-label="Facebook"]')
        menu_button.click()
        time.sleep(5)

    else:
        WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'input[id="pass"]'))
        )
        correct_pass = driver.find_element(By.CSS_SELECTOR, 'input[id="pass"]')
        correct_pass.send_keys(password_list[email_index])
        time.sleep(2)
        correct_pass.send_keys(Keys.ENTER)
        
        WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'a[aria-label="Facebook"]'))
        )
        menu_button = driver.find_element(By.CSS_SELECTOR, 'a[aria-label="Facebook"]')
        menu_button.click()
        time.sleep(5)

    return driver, email_index

def search_case():
    driver, email_index = login_case()
    print(email_index)

    if email_index == 1:
        WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'input[placeholder="Search Facebook"]'))
        )
        search_bar = driver.find_element(By.CSS_SELECTOR, 'input[placeholder="Search Facebook"]')
        search_bar.click
        search_bar.send_keys("Sasa Pachuchulia") 
        time.sleep(2)

        driver.get("https://www.facebook.com/profile.php?id=61557183483746")
        time.sleep(10)

    elif email_index == 0:
        WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'input[placeholder="Search Facebook"]'))
        )
        search_bar = driver.find_element(By.CSS_SELECTOR, 'input[placeholder="Search Facebook"]')
        search_bar.click
        search_bar.send_keys("Aya Yay") 
        time.sleep(2)

        driver.get("https://www.facebook.com/profile.php?id=61557505564665")
        time.sleep(10)

def message_case():
    driver, email_index = login_case()

    #ESCRIBIR MENSAJE 
    WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, 'div[aria-label="Messenger"]'))
    )
    messenger = driver.find_element(By.CSS_SELECTOR, 'div[aria-label="Messenger"]')
    messenger.click()
    time.sleep(2)

    WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, 'div[role="row"]'))
    )
    friend = driver.find_element(By.CSS_SELECTOR, 'div[role="row"]')
    friend.click()
    time.sleep(2)
    
    WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, 'div[role="textbox"]'))
    )
    message = driver.find_element(By.CSS_SELECTOR, 'div[role="textbox"]')
    print(message)
    message.click()
    message.send_keys("La prueba ha sido exitosa")
    time.sleep(2)
    message.send_keys(Keys.ENTER)
    time.sleep(10)

test_case = ""
answer_list = ["A", "a", "B", "b", "C", "c", "D", "d"]

while test_case not in answer_list:
    os.system("cls")
    test_case = input("Que caso de prueba desea realizar?\n"
                      "A) Creacion de cuenta\n"
                      "B) Inicio de sesion\n"
                      "C) Hacer busqueda\n"
                      "D) Enviar mensaje\n")

if test_case == "A" or test_case == "a":
    singup_case()

elif test_case == "B" or test_case == "b":
    login_case()

elif test_case == "C" or test_case == "c":
    search_case()

elif test_case == "D" or test_case == "d":
    message_case()