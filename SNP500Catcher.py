from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common import exceptions
import time
import os,shutil

directory_path = os.getcwd()
names=[]
driver = webdriver.Chrome(executable_path=r'C:/Users/Qiaoyi/AppData/Local/WebDriver/chromedriver.exe')
driver.get("https://www.theglobeandmail.com/investing/markets/indices/SPX/components/")

def SNP500SymbolCatcher():
    filepath = os.path.join(directory_path,"SNP500.txt")
    out = open(filepath,'w')
    bar = driver.find_element(By.XPATH,"//div[@class='barchart-paginator']")
    driver.execute_script("arguments[0].scrollIntoView({block:'center',inline:'nearest'});",bar)
    try:
        for i in range(2,6):
            WebDriverWait(driver,20).until(EC.visibility_of_all_elements_located((By.XPATH,"//td[@data-barchart-field='symbol']")))
            symbols = driver.find_elements(By.XPATH,"//td[@data-barchart-field='symbol']")
            for td in symbols:
                sname = td.find_element(By.TAG_NAME,"a")
                symbol = sname.text.split("-")
                out.write(symbol[0]+"\n")
                names.append(symbol[0])    
            next_page = driver.find_element(By.XPATH,f"//button[@page='{i}']")
            next_page.click()
            driver.implicitly_wait(10)
    except (exceptions.NoSuchElementException,exceptions.StaleElementReferenceException) as e:
        print(e)
    return

def SNP500NameCatcher():
    filepath = os.path.join(directory_path,"SNP500.txt")
    out = open(filepath,'w')
    bar = driver.find_element(By.XPATH,"//div[@class='barchart-paginator']")
    driver.execute_script("arguments[0].scrollIntoView({block:'center',inline:'nearest'});",bar)
    try:
        for i in range(2,6):
            WebDriverWait(driver,20).until(EC.visibility_of_all_elements_located((By.XPATH,"//barchart-field[@name='symbolName']")))
            symbolnames = driver.find_elements(By.XPATH,"//barchart-field[@name='symbolName']")
            for sname in symbolnames:
                outstr = sname.text.lower()
                if(" cl a" in outstr or " cl b" in outstr or " cl c" in outstr):
                    elem = driver.find_element(By.XPATH,f"//barchart-link-field[@symbolname='{sname.text}']").find_element(By.TAG_NAME,"a")
                    outstr = elem.text.split("-")[0]
                outstr = outstr.replace("company","co.").replace("corp a","corp")
                out.write(outstr+"\n")
                print(outstr+"\n")
                names.append(outstr)    
            next_page = driver.find_element(By.XPATH,f"//button[@page='{i}']")
            next_page.click()
    except (exceptions.NoSuchElementException,exceptions.StaleElementReferenceException) as e:
        print(e)
    return

WebDriverWait(driver,10).until(EC.visibility_of_all_elements_located((By.XPATH,"//div[@class='barchart-paginator']")))
SNP500NameCatcher()
driver.close()