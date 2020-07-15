import requests
from bs4 import BeautifulSoup
import pandas as pd


# finding a single day
page = requests.get("http://forecast.weather.gov/MapClick.php?lat=37.7772&lon=-122.4168")
soup = BeautifulSoup(page.content,"html.parser")
soup
seven_day = soup.find(id="seven-day-forecast")

forecast_items = seven_day.find_all(class_="tombstone-container")
tonight = forecast_items[0]

period = tonight.find(class_="period-name").get_text()
short_desc = tonight.find(class_="short-desc").get_text()
temp = tonight.find(class_="temp").get_text()

print(period)
print(short_desc)
print(temp)

img = tonight.find('img')
desc = img['title']
print(desc)


# extracting all information
period_tags = seven_day.select(".tombstone-container .period-name")
periods = [pt.get_text() for pt in period_tags]
periods

short_descs = [sd.get_text() for sd in seven_day.select('.tombstone-container .short-desc')]
temps = [t.get_text() for t in seven_day.select(".tombstone-container .temp")]
descs = [d["title"] for d in seven_day.select(".tombstone-container img")]

print(short_descs)
print(temps)
print(descs)


weather = pd.DataFrame({
    "period": periods,
    "short_desc": short_descs,
    "temp": temps,
    "desc": descs
})
weather


#################

#Loop Example
# link to first page - without `page=`
url = 'http://www.housingcare.org/housing-care/results.aspx?ath=1%2c2%2c3%2c6%2c7&stp=1&sm=3&vm=list&rp=10'

page = 0 

while True:

    print('---', page, '---')

    r = requests.get(url)

    soup = BeautifulSoup(r.content, "html.parser")

    # String substitution for HTML
    for link in soup.find_all("a"):
        print("<a href='>%s'>%s</a>" % (link.get("href"), link.text))

    # Fetch and print general data from title class
    general_data = soup.find_all('div', {'class' : 'title'})

    for item in general_data:
        print(item.contents[0].text)
        print(item.contents[1].text.replace('.',''))
        print(item.contents[2].text)

    # link to next page

    next_page = soup.find('a', {'class': 'next'})

    if next_page:
        url = next_page.get('href')
        page += 1
    else:
        break # exit `while True`





##### Below is orig. Works

page = requests.get("http://noahpinionblog.blogspot.com/")

soup = BeautifulSoup(page.content,"html.parser")

body = soup.find(id="Blog1")

dates = [dtes.get_text() for dtes in body.select(".date-outer .date-header")]
text = [t.get_text() for t in body.select(".date-outer .date-posts")]

#strings to remove from text
# \n
# Noah Smith
# Links to this post
# ThisBlogThis!Share to Twitter
# Share to Facebook
# Share to Pintrest
# \
# Email 


frame = pd.DataFrame({
    "dates": dates,
    "text": text #you could pull out the text after \n\n\n\n\n\n\n\n & before \n\n\n\n\n\n\n\n
})

frame

#need to click older posts button

button = soup.find(id="blog-pager-older-link")
press = button.find('a', class_="blog-pager-older-link")['href']

#####





