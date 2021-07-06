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
name='amzn'
quarter='q4'
str1 = 'Earning'
str2 = 'Call'
str3 = 'transcript'
years = ['2017','2018','2019','2020']
driver = webdriver.Chrome(executable_path=r'C:/Users/Qiaoyi/AppData/Local/WebDriver/chromedriver.exe')

def SNP500Catcher():
    driver.get("https://www.theglobeandmail.com/investing/markets/indices/SPX/components/")
    driver.implicitly_wait(5)
    filepath = os.path.join(directory_path,"SNP500.txt")
    out = open(filepath,'w')
    bar = driver.find_element(By.XPATH,"//div[@class='barchart-paginator']")
    driver.execute_script("arguments[0].scrollIntoView({block:'center',inline:'nearest'});",bar)
    for i in range(2,6):
        WebDriverWait(driver,20).until(EC.visibility_of_all_elements_located((By.XPATH,"//barchart-field[@name='symbolName']")))
        symbolnames = driver.find_elements(By.XPATH,"//barchart-field[@name='symbolName']")
        for sname in symbolnames:
            out.write(sname.text+"\n")
            names.append(sname.text)    
        next_page = driver.find_element(By.XPATH,f"//button[@page='{i}']")
        next_page.click()
        driver.implicitly_wait(10)


def textCatcher(outfile):
    elem = driver.find_elements_by_xpath("//div[@data-test-id='content-container']")
    outpath = os.path.join(directory_path,'ECTs')
    outpath = os.path.join(outpath,outfile)
    out = open(outpath,'w')
    for e in elem:
        try:
            print(e.text)
            out.writelines(e.text)
        except:
            print("error")
    elem = driver.back()
    return

def searchCatcher(keyStr):
    outpath = os.path.join(directory_path,"ECTnotfounds.txt")
    notfound = open(outpath,'w')
    WebDriverWait(driver,20).until(EC.visibility_of_all_elements_located((By.XPATH,"//input[@data-test-id='search-input']")))
    search_bar = driver.find_element_by_xpath("//input[@data-test-id='search-input']")
    search_bar.click()
    search_bar.clear()
    search_bar.send_keys(str(keyStr))
    search_bar.send_keys(Keys.RETURN)
    if "No results found" in driver.page_source:
        driver.refresh()
        search_bar.click()
        search_bar.clear()
        search_bar.send_keys(str(keyStr))
        search_bar.send_keys(Keys.RETURN)
    if "No results found" in driver.page_source:
        notfound.write(keyStr+"\n")
    driver.implicitly_wait(10)
    for year in years: 
        try:      
            post = driver.find_element_by_partial_link_text(year+' Results')  
            post.click()
            outfilename = name+"-"+quarter+"-"+year+"-EarningCallTranscript.txt"
            textCatcher(outfilename)
        except exceptions.NoSuchElementException as e:
            print(e)
            notfound.write(year + " " + keyStr)

def signin():
    WebDriverWait(driver,20).until(EC.visibility_of_all_elements_located((By.XPATH,"//button[@data-test-id='header-button-sign-in']")))
    elem = driver.find_element(By.XPATH,"//button[@data-test-id='header-button-sign-in']")
    elem.click()
    WebDriverWait(driver,20).until(EC.visibility_of_all_elements_located((By.XPATH,"//input[@name='email']")))
    elem = driver.find_element(By.XPATH,"//input[@name='email']")
    elem.clear()
    elem.send_keys("---")
    elem = driver.find_element(By.XPATH,"//input[@name='password']")
    elem.clear()
    elem.send_keys("---")
    elem.send_keys(Keys.RETURN)

if not os.path.exists('ECTs'):
    os.mkdir(os.path.join(directory_path,'ECTs'))
else:
    shutil.rmtree(os.path.join(directory_path,'ECTs'))
    os.mkdir(os.path.join(directory_path,'ECTs'))
#SNP500Catcher()

infile = os.path.join(directory_path,"SNP500.txt")
driver.get("https://seekingalpha.com/article/4402939-amazon-com-inc-amzn-q4-2020-results-earnings-call-transcript")
time.sleep(10)
#signin()
with open(infile,'r') as content:
    data = content.readlines()
for line in data:
    name = line.replace("\n","")
    search_string = name.lower()+" "+quarter.lower()+" "+str1.lower()+" "+ str2.lower()+" "+str3.lower()
    print (search_string)
    searchCatcher(search_string)
driver.close()
