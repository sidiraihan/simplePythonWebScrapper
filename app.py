from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
import time

#driver = webdriver.Chrome("/usr/lib/chromium-browser/chromedriver")
driver= webdriver.Chrome()
timestr = time.strftime("%Y%m%d-%H%M%S")
filename = 'scrap_tokped_'+timestr+'.csv'

products=[] #List to store name of the product
prices=[] #List to store price of the product
ratings=[] #List to store rating of the product
links=[] #list of links
driver.get("https://www.tokopedia.com/search?q=the+visual+mba&source=universe&st=product")
content = driver.page_source
soup = BeautifulSoup(content)
print('loading')
for a in soup.findAll('div',href=False, attrs={'class':'_2OBup6Zd'}):
    print('processing')
    name=a.find('h3', attrs={'class':'Ka_fasQS'})
    price=a.find('span', attrs={'class':'_3fNeVBgQ'})
    link=a.find('a', href=True)
    #rating=a.find('div', attrs={'class':'hGSR34 _2beYZw'})
    products.append(name.text)
    prices.append(price.text)
    #ratings.append(rating.text) 
    links.append(link.get('href'))
    #print(links)
    df = pd.DataFrame({'Product Name':products,'Price':prices,'URL':links}) 
    print(df)
    df.to_csv(filename, index=False, encoding='utf-8')