#scrap product cat by query terms page
from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
import time

#driver = webdriver.Chrome("/usr/lib/chromium-browser/chromedriver")
driver= webdriver.Chrome()
timestr = time.strftime("%Y%m%d-%H%M%S")
query = 'visual mba'
filename = 'scrap_tokped_'+query+'_'+timestr+'.csv'

products=[] #List to store name of the product
prices=[] #List to store price of the product
ratings=[] #List to store rating of the product
links=[] #list of links
imgs=[] #list of imgs
driver.get("https://www.tokopedia.com/search?q="+query+"&source=universe&st=product")
content = driver.page_source
soup = BeautifulSoup(content)
print('loading')
print(filename)
for a in soup.findAll('div',href=False, attrs={'class':'_2OBup6Zd'}):
    print('processing')
    name=a.find('h3', attrs={'class':'Ka_fasQS'})
    price=a.find('span', attrs={'class':'_3fNeVBgQ'})
    link=a.find('a', href=True)
    img=a.find('img', attrs={'class':'_2NQ7bVEP'})
    #rating=a.find('div', attrs={'class':'hGSR34 _2beYZw'})
    products.append(name.text)
    prices.append(price.text)
    #ratings.append(rating.text) 
    links.append(link.get('href'))
    imgs.append(img.get('src'))
    #print(links)
    df = pd.DataFrame({'Pic':imgs,'Product Name':products,'Price':prices,'URL':links}) 
    print(df)
    df.to_csv(filename, index=False, encoding='utf-8')
