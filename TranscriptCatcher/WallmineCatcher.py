from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common import exceptions
import time
import os,shutil

directory_path = os.getcwd()
name='amzn'
quarter='q4'
str1 = 'Earning'
str2 = 'Call'
str3 = 'transcript'
years = ['2017','2018','2019','2020']
driver = webdriver.Chrome(executable_path=r'C:/Users/Qiaoyi/AppData/Local/WebDriver/chromedriver.exe')

def textCatcher(outfile):
    time.sleep(1)
    try:
        WebDriverWait(driver,20).until(EC.visibility_of_all_elements_located((By.XPATH,"//section[@class='usmf-new article-body']")))
        elem = driver.find_element_by_xpath("//section[@class='usmf-new article-body']")
        article = elem.find_element(By.XPATH,"//span[@class='article-content']")
        outpath = os.path.join(directory_path,'ECTs')
        outpath = os.path.join(outpath,outfile)
        out = open(outpath,'w')
        try:
            print(article.text)
            out.writelines(article.text)
        except:
            print("error")
    except exceptions.TimeoutException as e:
        outpath = os.path.join(directory_path,"ECTnotfounds.txt")
        notfound = open(outpath,'a')
        notfound.write(outfile.replace(".txt","").replace("-"," "))
        print(e)
    
    time.sleep(3)
    elem = driver.back()
    return

def searchCatcher(keyStr):
    outpath = os.path.join(directory_path,"ECTnotfounds.txt")
    notfound = open(outpath,'a')

    # search for company in keyStr
    WebDriverWait(driver,20).until(EC.visibility_of_all_elements_located((By.XPATH,"//input[@name='q']")))
    search_bar = driver.find_element_by_xpath("//input[@name='q']")
    search_bar.click()
    search_bar.clear()
    search_bar.send_keys(str(keyStr))
    time.sleep(3)
    search_bar.send_keys(Keys.RETURN)

    #limit time login popup box handler
    try:
        WebDriverWait(driver,10).until(EC.visibility_of_all_elements_located((By.XPATH,"//div[@id='limit-sign-up-modal']")))
        limitsignup = driver.find_element(By.XPATH,"//div[@id='limit-sign-up-modal']")
        body = driver.find_element(By.TAG_NAME,"body")
        emptydiv=driver.find_element(By.XPATH,"//div[@class='modal-backdrop fade show']")
        time.sleep(3)
        driver.execute_script("arguments[0].setAttribute('class','sign-up-modal modal fade');",limitsignup)
        driver.execute_script("arguments[0].setAttribute('aria-hidden','true');",limitsignup)
        driver.execute_script("arguments[0].setAttribute('style','display: none;');",limitsignup)
        driver.execute_script("arguments[0].setAttribute('class','kit1 platform--ios');",body)
        driver.execute_script("arguments[0].setAttribute('class','');",emptydiv)       
    except (exceptions.NoSuchElementException,exceptions.TimeoutException) as e:
        print("No limit time login popup boxes.\n")

    #404 page handler
    try:
        WebDriverWait(driver,10).until(EC.visibility_of_all_elements_located((By.XPATH,"//div[@class='content']")))
        notfoundmsg = driver.find_element(By.TAG_NAME,"b")
        if "couldn't find" in notfoundmsg.text:
            driver.back()
            time.sleep(3)
            return
    except (exceptions.NoSuchElementException,exceptions.TimeoutException) as e:
        print("Not 404 page.\n")

    #transcript divisionn finder
    try:
        WebDriverWait(driver,20).until(EC.visibility_of_all_elements_located((By.XPATH,"//div[@class='company-transcripts']")))
    except exceptions.TimeoutException as e:
        notfound.write("q4 "+"2017"+" "+keyStr+" EarningCallTranscript\n")
        notfound.write("q4 "+"2018"+" "+keyStr+" EarningCallTranscript\n")
        notfound.write("q4 "+"2019"+" "+keyStr+" EarningCallTranscript\n")
        notfound.write("q4 "+"2020"+" "+keyStr+" EarningCallTranscript\n")
        return

    # try to find company transcript section in page
    try:
        time.sleep(3)
        division = driver.find_element(By.XPATH,"//div[@class='company-transcripts']")
        driver.execute_script("arguments[0].scrollIntoView({block:'center',inline:'nearest'});",division)
        link = division.find_element(By.PARTIAL_LINK_TEXT,"Recent")
        link.click()
    except exceptions.NoSuchElementException as e:
        print(e)
        print(keyStr+": Company Transcript Not Found")
        notfound.write(keyStr+"\n")
        return

    # get 2017-2020 q4 earning call transcript href links
    time.sleep(3)
    try:
        WebDriverWait(driver,20).until(EC.visibility_of_all_elements_located((By.XPATH,"//table[@class='table table-sm table--no-margin table-striped']")))
        table = driver.find_element(By.XPATH,"//table[@class='table table-sm table--no-margin table-striped']")
        rows = table.find_elements(By.XPATH,'//tr[@class="js-clickable-row clickable-row"]')
        urls=[]
        for row in rows:
            url = row.get_attribute("data-href")
            for year in years:     
                if "q4" in url and year in url and "earning" in url and "transcript" in url:
                    urls.append(url)
                    break
    except (exceptions.NoSuchElementException,exceptions.TimeoutException,exceptions.ElementNotInteractableException) as e:
        print("Clickable transcript finding problem\n")
        return
    
    # get each link data
    try:  
        if len(urls)!=0:
            for u in urls:
                if "2017" in u:
                    year="2017"
                elif "2018" in u:
                    year="2018"
                elif "2019" in u:
                    year="2019"
                elif "2020" in u:
                    year="2020"
                else:
                    year="0000"
                outfilename = keyStr+"-"+"q4-"+year+"-EarningCallTranscript.txt"

                if "fool" not in u:
                    outpath = os.path.join(directory_path,"ECTnotfounds.txt")
                    notfound = open(outpath,'a')
                    notfound.write(outfilename.replace(".txt","").replace("-"," ")+"\n")
                    continue
                driver.get(u)
                WebDriverWait(driver,20).until(EC.visibility_of_all_elements_located((By.XPATH,"//section[@class='usmf-new article-body']")))
                time.sleep(3)
                textCatcher(outfilename)
    except (exceptions.TimeoutException,UnboundLocalError) as e:
        print("Text Catcher calling problem\n")

    driver.get("https://wallmine.com/")
    time.sleep(3)
    return

#==============================Main===============================================#
if not os.path.exists('ECTs'):
    os.mkdir(os.path.join(directory_path,'ECTs'))
else:
    shutil.rmtree(os.path.join(directory_path,'ECTs'))
    os.mkdir(os.path.join(directory_path,'ECTs'))

infile = os.path.join(directory_path,"SNP500.txt")
outpath = os.path.join(directory_path,"ECTnotfounds.txt")
os.remove(outpath)
driver.get("https://wallmine.com/")
time.sleep(2)

with open(infile,'r') as content:
    data = content.readlines()
for line in data:
    name = line.replace("\n","").lower()
    print (name)
    searchCatcher(name)
driver.close()
