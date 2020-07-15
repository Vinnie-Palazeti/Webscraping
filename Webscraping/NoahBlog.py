import requests
from bs4 import BeautifulSoup
import pandas as pd


Noahdata = pd.DataFrame({
    "dates": [],
    "text": [] 
    
    })

url = "http://noahpinionblog.blogspot.com/"
num = 1

while True:

    print('---', page, '---') idk why the page counter doesnt work
    page = requests.get(url)
    info = BeautifulSoup(page.content, "html.parser")

    #find stuff
    body = info.find(id="Blog1")
    dates = [dtes.get_text() for dtes in body.select(".date-outer .date-header")]
    text = [t.get_text() for t in body.select(".date-outer .date-posts")]
    
    frame = pd.DataFrame({
    "dates": dates,
    "text": text 
    })
    #save into empty df
    Noahdata = Noahdata.append(frame)


    next_page = info.find(id="blog-pager-older-link")
    

    if next_page:
        url = next_page.find('a', class_="blog-pager-older-link")['href']
        num += 1 
    else:
        break

#Noahdata.to_excel("Noahdata.xlsx", index=False)


################################

MattBdata = pd.DataFrame({
    "dates": [],
    "text": [] 
    
    })

url = "http://mattbruenig.com/"
num = 1

while True:

    print( "----", num, "----")
    page = requests.get(url)
    soup = BeautifulSoup(page.content,"html.parser")

    #body = soup.find(id="page")
    #body = soup.select(".post")
    #body = soup.find_all(class_='post')
    dates = [dtes.get_text() for dtes in soup.select(".entry-date")]
    text = [t.get_text() for t in soup.select(".post")]

    frame = pd.DataFrame({ 
    "dates": dates,
    "text": text 
    })

    MattBdata = MattBdata.append(frame)

    next_page = soup
    
    if next_page:
        url = next_page.find('a', class_="next page-numbers")['href']
        num += 1
    else:
        break

#MattBdata.to_excel("MattBdata.xlsx", index=False)

################################

DavidBdata = pd.DataFrame({
    "dates": [],
    "text": [] 
    
    })


url = "https://macromarketmusings.blogspot.com/"
num = 1
#pooped out @ 51
#url = 'https://macromarketmusings.blogspot.com/search?updated-max=2012-09-25T16:55:00-05:00&max-results=7&start=350&by-date=false'
#num = 52

while True:

    print( "----", num, "----")
    page = requests.get(url)
    soup = BeautifulSoup(page.content,"html.parser")

    body = soup.find(id="main")
    dates = [dtes.get_text() for dtes in body.select(".date-outer .date-header")]
    text = [t.get_text() for t in body.select(".date-outer .date-posts")] #\xa0 & \n need to be removed

    frame = pd.DataFrame({ 
    "dates": dates,
    "text": text 
    })


    DavidBdata = DavidBdata.append(frame)

    next_page = soup
    
    if next_page:
        url = next_page.find('a', class_="blog-pager-older-link")['href']
        num += 1
    else:
        break

#DavidBdata.to_excel("DavidBdata.xlsx", index=False)



################################

MarkTdata = pd.DataFrame({
    "dates": [],
    "text": [] 
    
    })

url = "https://economistsview.typepad.com/economistsview/page/2/"
num = 1


while True:

    print( "----", num, "----")
    page = requests.get(url)
    soup = BeautifulSoup(page.content,"html.parser")

    body = soup.find(id="center")

    titles = [t.get_text() for t in soup.select(".entry-header")]

    dates = soup.select(".posted + p")
    
    dates = pd.DataFrame({
        "dates": dates
        })
    
    dates['dates'] = dates['dates'].astype(str)
    dates['dates'] = dates['dates'].str[188:]
    dates['dates'] = dates['dates'].str[:33]
    
    dates['dates'] = dates.dates.str.extract('(.+\d{4})', expand=False)
    #tes[tes['dates'].isin(words)]
    
    text = [t.get_text() for t in body.select(".entry-content .entry-body")]

   
    frame = pd.DataFrame({ 
    #"dates": dates,
    "text": text,
    "titles": titles 
    })

    frame = pd.concat([frame,dates], axis=1)
    frame = frame[~frame['titles'].str.contains("links|Links")]

    MarkTdata = MarkTdata.append(frame)

    next_page = soup.find(name='span', class_='pager-right')

    if next_page:
        url = next_page.a['href']
        num += 1
    else:
        break


 
 len(titles)
 len(dates)
 len(text) #Broke after 7, why does text have 51?
 #pd.reset_option('^display.', silent=True)
    
