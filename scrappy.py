import requests
from bs4 import BeautifulSoup

# Send request to cennect to the internet
respond = requests.get('https://www.yahoo.com/news/weather/').text

#Parse request
soup = BeautifulSoup(respond, 'html.parser')


#Loop through the content and grab what we need
for days in soup.findAll('div', class_="accordion Ov(h) Trsdu(.42s) daily"):

    print('------------------DAYS---------------------------------')


# Days of the week
    names = soup.findAll("div", class_="D(ib) Va(m) W(1/4)")
    for name in names:
        print(name.text)

    print('------------------HIGHS---------------------------------')

# Highest degree in F
    highs = soup.find_all('span', class_='high D(ib) Miw(32px)')
    for high in highs:
        print(high.text + 'F')

    print('------------------LOWS---------------------------------')

# Lowest degree in F
    lows = soup.find_all('span', class_="low Pstart(10px) C(#a5d6ff) D(ib) Miw(32px)")
    for low in lows:
        print(low.text + 'F')

    # print(name)
    # print(high)
    # print(low)