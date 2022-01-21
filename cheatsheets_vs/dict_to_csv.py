import requests as requests
from bs4 import BeautifulSoup as BeautifulSoup
import pandas
from pandas import DataFrame


def pulling_from_url(url):
    results = requests.get(url)
    src = results.content
    soup = BeautifulSoup(src, "lxml")

    article_titles = []
    article_links = []
    article_titles_cleaned = []
    index_list = list(range(1,11))
    
    for h2_tags in soup.find_all("h2"):
        for a_tag in h2_tags.find_all("a"):
            article_links.append(a_tag["href"])

    for a_tags in soup.find_all("a", {"class": "news-item__title"}):
        a_tags_text = a_tags.getText()
        article_titles.append(a_tags_text)
    
    for titles in article_titles:
        clean_title_1 = titles.replace("\t", "")
        clean_title_2 = clean_title_1.replace("\a", "")
        clean_title_3 = clean_title_2.replace("\n", "")
        clean_title_4 = clean_title_3.replace("x", "")
        article_titles_cleaned.append(clean_title_3)

    values_1 = article_titles_cleaned
    values_2 = article_links
    keys = index_list
    titles_links_dict = dict(zip(index_list, zip(values_1, values_2)))
    data_frame_t_and_l = pandas.DataFrame(titles_links_dict)
    data_frame_t_and_l.to_csv("briefings_title_and_link.csv", sep = ",", header = False, index=False)
    
url = "https://www.whitehouse.gov/briefing-room/"
dictionary = pulling_from_url(url)
