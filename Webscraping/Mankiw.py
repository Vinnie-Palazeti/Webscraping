Mankiwdata = pd.DataFrame({
    "dates": [],
    "text": [] 
    
    })

url = "http://gregmankiw.blogspot.com/2006/03/" #maybe set up the url as a variable & increase from 03 to 12 to 1 to 12
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