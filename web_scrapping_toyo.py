from bs4 import BeautifulSoup
import requests
import csv
import os



from selenium import webdriver
import codecs
import os
os.chmod('C:/Users/amank/Downloads/chromedriver_win32/chromedriver.exe', 755)
#set chromedriver.exe path
driver = webdriver.Chrome(executable_path='C:/Users/amank/Downloads/chromedriver_win32/chromedriver.exe')
driver.implicitly_wait(0.5)
#maximize browser
driver.maximize_window()
#launch URL
driver.get("https://www.demandstar.com/app/agencies/california/city-of-sunnyvale/procurement-opportunities/e9a860f4-8f17-43af-aae7-e5dc8389f36e/")
#get file path to save page
n=os.path.join("C:\\xampp1\\htdocs\\xampp\\","i.html")
#n=os.path.join("C:\\Users\\amank\\Downloads\\","Page.html")
#open file in write mode with encoding
f = codecs.open(n, "w", "utf−8")
#obtain page source
h = driver.page_source
#write page source content to file
f.write(h)
#close browser
driver.quit()


#download webpage put in xampp folder and then doing web scrapping 


fields=['ID','Due','Broadcast','Planholders']
try:
    
 os.remove('aman16.csv')

except:
    print("k")
    
url = "https://www.demandstar.com/app/agencies/california/city-of-sunnyvale/procurement-opportunities/e9a860f4-8f17-43af-aae7-e5dc8389f36e/"




url ="http://localhost/xampp/i.html"



with open('aman16.csv','a') as csvfile:

  writer =csv.writer(csvfile)
  writer.writerow(fields)
csvfile.close()


req = requests.get(url)

soup = BeautifulSoup(req.text.replace('>','>\n'), "html.parser")
a1=[]
for link in soup.find_all(class_="list-inline"):
 for link1 in link(class_="list-inline-item"):
  a=link1.text.split("\n")
  a1.append(a[3])
 a2=a1
 print(link)
 with open('aman16.csv','a') as csvfile:

  writer =csv.writer(csvfile)
  writer.writerow(a2)  
 a1.clear()
