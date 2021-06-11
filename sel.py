from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

cod_fisc = ""   # insert your codice fiscale
num_tes = ""    # insert the number behind your tessera sanitaria

url = "https://cup.apss.tn.it/webportal/vaccinocovid/welcome"
url2 = "https://cup.apss.tn.it/webportal/vaccinocovid/main/booking/supplymode"

driver = webdriver.Firefox()
driver.implicitly_wait(5)
driver.get(url)

### go to booking page ###
sleep(0.3)
driver.get(url2)

sleep(0.3)
# print(driver.title)
# assert "paziente" in driver.title
########## insert info ##########
try:
    ## Not working
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
    keyboard = Controller()

    keyboard.press(Key.tab)
    keyboard.release(Key.tab)
    keyboard.type(cod_fisc)
    keyboard.press(Key.tab)
    keyboard.release(Key.tab)
    keyboard.type(num_tes)

    
    pass
# check the checkboxes

css1 = "form.ng-dirty > div:nth-child(2) > div:nth-child(4) > div:nth-child(1) > label:nth-child(1) > i:nth-child(1)"
css2 = "form.ng-dirty > div:nth-child(2) > div:nth-child(4) > div:nth-child(2) > label:nth-child(1) > i:nth-child(1)"
driver.find_element_by_css_selector(css1).click()
driver.find_element_by_css_selector(css2).click()

sleep(0.5)
css_continue = "form.ng-dirty > div:nth-child(3) > button:nth-child(2)"
xpath_continue = "/html/body/div[2]/ion-nav-view/ion-side-menus/ion-side-menu-content/ion-nav-view/ion-view/ion-nav-view/ion-view/ng-include[2]/ion-content/div[2]/div/div[2]/team-card-login/div/ng-include[2]/form/div[3]/button"
driver.find_element_by_xpath(xpath_continue).send_keys(Keys.RETURN)

## Mistero....
