from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import time


options = Options()
options.add_argument(r"user-data-dir=C:\Users\kamala1\appdata\Local\Google\Chrome\User Data\Selenium")
#options.add_argument("start-maximized")
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)



def CreateLink(inputShortlink, inputUrl, tag="TAG"):
    dupError=False
    
    driver.get('https://go.R.com/app/shortlink/add')
    def setField(webDriver, fieldName, fieldValue):
        field = WebDriverWait(webDriver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, f"input#{fieldName}")))
        #webDriver.execute_script(f"arguments[0].value = '{fieldValue}';", field)
        webDriver.execute_script(f"arguments[0].value = '';", field)
        field.send_keys(f'{fieldValue}\t') #pass the value then press tab to move focus
        field.send_keys(chr(27)) #press escape to stop annoying pop-ups

    setField(driver, 'tag', tag)
    setField(driver, 'inputShortlink', inputShortlink)
    setField(driver, 'inputUrl', inputUrl)
   

    time.sleep(7)
    WebDriverWait(driver,30).until(EC.element_to_be_clickable((By.CSS_SELECTOR,".btn.btn-primary"))).click()
    
    try:
        field = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, f"div.alert.alert-error")))
        if field.text.find('with domain go.roche.com already exists')>0:
            dupError=True
            print(field.text)
            WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, f"button.close"))).click()
    except Exception as e:
        pass
        #print(e)
    
    try:
        field = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, f"div.alert.alert-success")))
        if field.text.find('has been added')>0:
            dupError=False
            print(field.text)
    except Exception as e:
        dupError=True
        #print(e)

        
CreateLink("conceptual", "https://piim.roche.com?m=1&o=xyz")    




