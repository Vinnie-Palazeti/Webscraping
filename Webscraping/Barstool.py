import pandas as pd
import numpy as np
from datetime import date
import requests
from bs4 import BeautifulSoup

start_date = date(2015, 1, 1)
end_date = date(2016, 1, 1)
daterange = pd.date_range(start_date, end_date)

dates = pd.DataFrame({"dates":daterange})
dates = dates.iloc[::5, :].reset_index(drop=True)

after = dates.iloc[::2].reset_index(drop=True)  # even
before = dates.iloc[1::2].reset_index(drop=True)  # odd

after_offset = after + pd.DateOffset(1)
before_offset = before + pd.DateOffset(-1)

after = after.dates.dt.strftime('%Y-%m-%d')
before = before.dates.dt.strftime('%Y-%m-%d')
after_offset = after_offset.dates.dt.strftime('%Y-%m-%d')
before_offset = before_offset.dates.dt.strftime('%Y-%m-%d')

urls = []
for j in range(0,36):
  url_1 = "https://union.barstoolsports.com/stories/latest?limit=1500&after="+ after[j] + "&before=" + before[j] +"&type=standard_post"
  urls.append(url_1)
  url_2 = "https://union.barstoolsports.com/stories/latest?limit=1500&after="+ before_offset[j] + "&before=" + after_offset[j+1] +"&type=standard_post"
  urls.append(url_2)


Barstool = pd.DataFrame({
    "dates": [],
    "author": [],
    "title": [],
    "text": []
    
    })


for i in range(len(urls)):
  info = pd.read_json(urls[i])['url']
  print("---", i, "---")
  for k in range(len(info)):
    print("---", k,"---")
    url = info[k]
    page = requests.get(url)
    soup = BeautifulSoup(page.content,"html.parser")
    words = [t.get_text() for t in soup.select(".story__content")]
    author = [w.get_text() for w in soup.select(".authorName")][1]
    date = [d.get_text() for d in soup.select(".timestamp")][1]
    title = [p.get_text() for p in soup.select(".story__title")]

    frame = pd.DataFrame({
        "dates": date,
        "author": author,
        "title": title,
        "text": words
        })
  
    Barstool = Barstool.append(frame)




#Barstool
#usually works for about 8 months, then barstool kicks me off
#Barstool.to_excel("Barstool_2019.xlsx", index=False)
#works
#Barstool.to_excel("Barstool_2019.xlsx", engine='xlsxwriter')
#Barstool.to_excel("Barstool_2018_08_27.xlsx", index=False)

i

Barstool



################################################### For fixing traceback error
len(urls)


done_thus_far = i+1
range(done_thus_far, len(urls))

print(list(range(done_thus_far, len(urls))))


for i in range(done_thus_far, len(urls)):
  info = pd.read_json(urls[i])['url']
  print("---", i, "---")
  for k in range(len(info)):
    print("---", k,"---")
    url = info[k]
    page = requests.get(url)
    soup = BeautifulSoup(page.content,"html.parser")
    words = [t.get_text() for t in soup.select(".story__content")]
    author = [w.get_text() for w in soup.select(".authorName")][1]
    date = [d.get_text() for d in soup.select(".timestamp")][1]
    title = [p.get_text() for p in soup.select(".story__title")]

    frame = pd.DataFrame({
        "dates": date,
        "author": author,
        "title": title,
        "text": words
        })
  
    Barstool = Barstool.append(frame)


Barstool


#Barstool.to_excel("Barstool_2015.xlsx", index=False)