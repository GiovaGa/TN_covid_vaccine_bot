from time import sleep
from datetime import datetime
from datetime import timedelta
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC

cod_fisc = "" # insert your codice fiscale
num_tes = ""    # insert the number behind your tessera sanitaria

url = "https://cup.apss.tn.it/webportal/vaccinocovid/welcome"


def wait(target):
    now = datetime.now()
    delta = target - now
    if delta > timedelta(0):
        print("going to sleep for %s" % delta)
        sleep(delta.total_seconds())
        return

driver = webdriver.Firefox()
driver.implicitly_wait(5)

#### Wait the right time ####

driver.get(url)

while "Prenota Vaccino covid-19" != driver.title:
    sleep(0.2)


######## go to booking page ########
driver.find_element_by_css_selector("div.widget:nth-child(1)").click()

########## insert info ##########
try:
    ## Not working ##
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
    sleep(0.2) # may depend on the connection speed
    keyboard = Controller()

    keyboard.press(Key.tab)
    keyboard.release(Key.tab)
    sleep(0.05)
    keyboard.type(cod_fisc)
    keyboard.press(Key.tab)
    keyboard.release(Key.tab)
    sleep(0.05)
    keyboard.type(num_tes)

#### check the checkboxes ####
i = 1
while True:
    cssel = "form.ng-dirty > div:nth-child(2) > div:nth-child(4) > div:nth-child(" + str(i) + ") > label:nth-child(1) > i:nth-child(1)"
    try:
        driver.find_element_by_css_selector(cssel).click()
        # print(cssel)
    except: break
    i += 1

#### Hit the continue button ####

css_continue = ".wizard-body > team-card-login:nth-child(1) > div:nth-child(1) > ng-include:nth-child(2) > form:nth-child(1) > div:nth-child(3) > button:nth-child(2)"
driver.find_element_by_css_selector(css_continue).click() ## implicitly waits until button is availible
# slow, but apparently cannot do better

print("Done")

## Login done
## Now the user needs to manually choose the place and date of the vaccination

