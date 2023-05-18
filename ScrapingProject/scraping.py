# Import scraping modules
from urllib.request import urlopen
import urllib.request
from bs4 import BeautifulSoup

# Import data manipulation modules
import pandas as pd
import numpy as np
import re



hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
       'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
       'Accept-Encoding': 'none',
       'Accept-Language': 'en-US,en;q=0.8',
       'Connection': 'keep-alive'}

data = pd.read_excel("toolspareparts.xlsx")
link_list = list(data.iloc[:, 0])

name_list = []
sku_list = []
imgurl_list = []
imgname_list = []
diagramurl_list = []
diagramname_list = []
details_list = []

for url in link_list:

       request = urllib.request.Request(url, None, hdr)
       response = urllib.request.urlopen(request)
       soup = BeautifulSoup(response)

       headers = [i.getText() for i in soup.find('table', {'class', 'table data grouped'}).findAll('tr')[0].findAll('th')][0:3]
       name = soup.find('span', {'class':'base'}).getText()
       sku = soup.find('div', {'class':'value'}).getText()
       image_url = soup.find('img', {'class': 'gallery-placeholder__image'}).get('src')
       image_name = image_url.split('/')[-1]
       diagram_url = soup.find('div', {'class':'diagram__content'})
       if diagram_url is not None:
              diagram_url = diagram_url.find('img').get('src')
       else:
              diagram_url = 'Not available'
       diagram_name = diagram_url.split('/')[-1]
       details = soup.find('div', {'class':'product attribute description'}).getText().replace('\n', '')
       # diagram = soup.find('table', {'class','table data grouped'}).findAll('tr')[1].find('td').getText()

       name_list.append(name)
       sku_list.append(sku)
       imgname_list.append(image_name)
       imgurl_list.append(image_url)
       diagramurl_list.append(diagram_url)
       diagramname_list.append(diagram_name)
       details_list.append(details)

df = pd.DataFrame(list(zip(name_list, sku_list, imgname_list, imgurl_list, diagramurl_list,
                           diagramname_list, details_list)), columns=headers)
