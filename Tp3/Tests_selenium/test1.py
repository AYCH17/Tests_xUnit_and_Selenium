#%%
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest


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


inputs = [( { "name" : "first_name", "error_name" : "first_name_error", "text" : "", "visible" : 1  }, 1), 
( { "name" : "last_name", "error_name" : "last_name_error", "text" : "", "visible" : 1  }, 1),
( { "name" : "username", "error_name" : "username_error", "text" : "", "visible" : 1  }, 1),
( { "name" : "email", "error_name" : "email_error", "text" : "", "visible" : 1  }, 1),
( { "name" : "email", "error_name" : "email_error", "text" : "falseemail.com", "visible" : 1  }, 1),
( { "name" : "phone", "error_name" : "phone_error", "text" : "" , "visible" : 1 }, 1),
( { "name" : "phone", "error_name" : "phone_error", "text" : "123456789", "visible" : 1  }, 1),
( { "name" : "phone", "error_name" : "phone_error", "text" : "12345678900", "visible" : 1  }, 1),
( { "name" : "current_password", "error_name" : "current_password_error", "text" : "", "visible" : 1  }, 1),
( { "name" : "current_password", "error_name" : "current_password_error", "text" : "1234567" , "visible" : 1 }, 1),
( { "name" : "current_password", "error_name" : "current_password_error", "text" : "12345678" , "visible" : 1 }, 1),

( { "name" : "new_password", "error_name" : "new_password_error", "text" : "", "visible" : 1  }, 1),
( { "name" : "new_password", "error_name" : "new_password_error", "text" : "1234567", "visible" : 1  }, 1),
( { "name" : "confirm_password", "error_name" : "confirm_password_error", "text" : "", "visible" : 1  }, 1),

( { "name" : "first_name", "error_name" : "first_name_error", "text" : "ismail", "visible" : 0  }, 1), 
( { "name" : "last_name", "error_name" : "last_name_error", "text" : "khriss", "visible" : 0  }, 1),
( { "name" : "username", "error_name" : "username_error", "text" : "prof" , "visible" : 0 }, 1),
( { "name" : "email", "error_name" : "email_error", "text" : "ismail_khriss@uqar.ca", "visible" : 0  }, 1),
( { "name" : "phone", "error_name" : "phone_error", "text" : "2345678900", "visible" : 0  }, 1),
( { "name" : "current_password", "error_name" : "current_password_error", "text" : "aaaaaaaa", "visible" : 0  }, 1),
( { "name" : "new_password", "error_name" : "new_password_error", "text" : "12345678", "visible" : 0  }, 1),
( { "name" : "confirm_password", "error_name" : "confirm_password_error", "text" : "12345678", "visible" : 0  }, 1),

]


def check_form_input(input):
        
       
        driver.get("http://localhost:4200/profile/Da_king")

        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.NAME,input["name"])))
        elem = driver.find_element_by_name(input['name'])
        WebDriverWait(driver, 5).until(EC.invisibility_of_element_located((By.ID,input["error_name"])))
        elem.send_keys(input['text'])
        #click boutton confirmer
        driver.find_element_by_xpath("/html/body/app-root/app-profile/html/body/div/div[2]/div[2]/form/div[5]/button").click()
        #click boutton changer
        driver.find_element_by_xpath("/html/body/app-root/app-profile/html/body/div/div[2]/div[3]/form/div[4]/button").click()
       
        try:
            if input["visible"] :
                       WebDriverWait(driver, 1).until(EC.visibility_of_element_located((By.ID,input["error_name"])))
            
            # Setting the status of test as 'passed' or 'failed' based on the condition; if title of the web page starts with 'BrowserStack'
            driver.execute_script('browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"passed", "reason": "comportement attendu!"}}')
            print("passed")
            result = 1
        except TimeoutException:
            driver.execute_script('browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"failed", "reason": "comportement inattendu!"}}')
            print("failed")
            result = 0
      

for input,expectation in inputs :
    check_form_input(input)


driver.quit() 
        

        
