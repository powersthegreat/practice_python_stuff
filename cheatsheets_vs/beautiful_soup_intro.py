import requests as requests
from bs4 import BeautifulSoup 

url = "https://www.whitehouse.gov/briefing-room/"
results = requests.get(url)
src = results.content
soup = BeautifulSoup(src, "lxml")

article_links = []

for h2_tags in soup.find_all("h2"):
    for a_tag in h2_tags.find_all("a"):
        article_links.append(a_tag["href"])

