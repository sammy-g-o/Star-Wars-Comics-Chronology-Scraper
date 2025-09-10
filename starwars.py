import requests
from bs4 import  BeautifulSoup

link = requests.get('https://youtini.com/timelines/canon/canon-comics')
soup = BeautifulSoup(link.text, 'html.parser')

comic_name = soup.find_all("div", attrs={"class":"title-timeline"})
with open("starwars.txt", "w") as file:
    for cum in comic_name:
        file.write(str(cum.text))
        file.write("\n")
