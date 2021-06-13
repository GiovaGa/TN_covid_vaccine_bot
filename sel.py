from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

cod_fisc = ""
num_tes = ""

url = "https://cup.apss.tn.it/webportal/vaccinocovid/welcome"

driver = webdriver.Firefox()
driver.implicitly_wait(5)
driver.get(url)

### go to booking page ###
driver.find_element_by_css_selector("div.widget:nth-child(1)").click()

########## insert info ##########
try:
    ## Not working ##
    # wait = WebDriverWait(driver,10)
    # el_cf = wait.until(EC.element_to_be_clickable((By.ID, 'cf')))
    el_cf = driver.find_element_by_id('cf')
    el_cf.click()
    el_cf.send_keys(cod_fisc)
    
    el_num = driver.find_element_by_id("ts")
    el_num.click()
    el_num.send_keys(num_tes)
except:
    ### Let's go the hard way
    from pynput.keyboard import Key, Controller
    print("Going the hard way")
    sleep(0.3)
    keyboard = Controller()

    keyboard.press(Key.tab)
    keyboard.release(Key.tab)
    keyboard.type(cod_fisc)
    keyboard.press(Key.tab)
    keyboard.release(Key.tab)
    keyboard.type(num_tes)
    
    pass
# check the checkboxes

i = 1
while True:
    cssel = "form.ng-dirty > div:nth-child(2) > div:nth-child(4) > div:nth-child(" + str(i) + ") > label:nth-child(1) > i:nth-child(1)"
    try: 
        driver.find_element_by_css_selector(cssel).click()
        print(cssel)
    except: break
    i += 1

sleep(0.1)
css_continue = ".wizard-body > team-card-login:nth-child(1) > div:nth-child(1) > ng-include:nth-child(2) > form:nth-child(1) > div:nth-child(3) > button:nth-child(2)"
driver.find_element_by_css_selector(css_continue).click()

## Mistero....
