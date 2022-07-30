#%%
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest
import time


desired_cap = {
 'os_version': '10',
 'resolution': '1920x1080',
 'browser': 'Chrome',
 'browser_version': 'latest',
 'os': 'Windows',
 'browserstack.local': 'true',
 'name': 'Test TP3', # test name
 'build': 'build1 TP3', # CI/CD job or build name
 'browserstack.debug': 'true',  # for enabling visual logs
 'browserstack.console': 'info',  # to enable console logs at the info level. You can also use other log levels here
 'browserstack.networkLogs': 'true'  # to enable network logs to be logged
}
driver = webdriver.Remote(
    command_executor='https://aymanchafni_DylKNq:zXnw65jyxNyaSVJzTH49@hub-cloud.browserstack.com/wd/hub',
    desired_capabilities=desired_cap)

driver.get("http://localhost:4200/profile/Da_king")



def check_form_input(input):
        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH,input["id"])))
        elem = driver.find_element_by_name(input['id'])
        WebDriverWait(driver, 5).until(EC.invisibility_of_element_located((By.XPATH,input["error_name"])))

        elem.clear()
        elem.send_keys(input['text'])
        driver.find_element_by_xpath("/html/body/app-root/app-profile/html/body/div/div[2]/div[2]/form/div[5]/button").click()
        driver.find_element_by_xpath("/html/body/app-root/app-profile/html/body/div/div[2]/div[3]/form/div[4]/button").click()
       
        try:
            if input["visible"] :
                       WebDriverWait(driver, 1).until(EC.visibility_of_element_located((By.XPATH,input["error_name"])))
            
            # Setting the status of test as 'passed' or 'failed' based on the condition; if title of the web page starts with 'BrowserStack'
            driver.execute_script('browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"passed", "reason": "entree invalide!"}}')
            print("passed")
            result = 1
        except TimeoutException:
            driver.execute_script('browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"failed", "reason": "entree invalide mais pas de message!"}}')
            print("failed")
            result = 0
        
        #assert result == expected
        driver.quit() 

check_form_input({ "id" : 'first_name', "error_name" : '/html/body/app-root/app-profile/html/body/div/div[2]/div[2]/form/div[1]/div[1]/p', "text" : "", "visible" : 1  })
