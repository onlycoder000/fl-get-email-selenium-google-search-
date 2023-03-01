from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time
import csv
from datetime import datetime
import random
from selenium.webdriver.common.proxy import Proxy, ProxyType


line_count=0
found=0
not_found=0


prox = Proxy()
prox.proxy_type = ProxyType.MANUAL
prox.http_proxy = "50.231.154.82:4444"


capabilities = webdriver.DesiredCapabilities.CHROME
prox.add_to_capabilities(capabilities)

op = Options()
op.add_argument("user-data-dir=browser_data") 
driver = webdriver.Chrome('chromedriver/chromedriver',options=op,desired_capabilities=capabilities)
driver.get('https://www.google.com/')


with open('import.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for d in csv_reader:
        s=False
        if d[9] == False or d[9] == 'False':
            driver.get('https://www.google.com/search?q='+d[2]+' linkedin.com')
            if driver.find_elements(By.ID,'captcha-form'):
                n=input('Click Enter')

            a=driver.find_elements(By.CSS_SELECTOR,'#search [data-hveid] a:first-child')

            r=[]
            for z in a:
                if z.get_attribute('href').find('linkedin.com/in') > -1:
                    r.append(z.get_attribute('href'))
            
            s=str(r)
        else:
            s=d[9]
        
        if s:
            d[9]=s
            found+=1
        else:
            not_found+=1


        with open('output.csv', mode='a') as open_file:
            open_writer = csv.writer(open_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            open_writer.writerow(d)
        # time.sleep(1000)
    
        print('scan='+str(line_count)+' found='+str(found)+' not-found='+str(not_found)+' time='+datetime.now().strftime("%H:%M:%S")) 
        line_count+=1           
        # time.sleep(random.randint(0,10000))
            

        