import requests

# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service


topics_url = 'https://github.com/topics'
response = requests.get(topics_url)
# print(response.status_code)
# print(len(response.text))
page_content = response.text

with open('webpage.html', 'w') as topics_list:
    topics_list.write(page_content)


from bs4 import BeautifulSoup

doc = BeautifulSoup(page_content, 'html.parser')
# print(type(doc))
title_selection = "f3 lh-condensed mb-0 mt-1 Link--primary"
topic_title_tags = doc.find_all('p', class_=title_selection)
# print(topic_title_tags)

description = 'f5 color-fg-muted mb-0 mt-1'
topic_description = doc.find_all('p', class_ = description)
# print(topic_description)

link = "no-underline flex-grow-0"
topic_link_tags = doc.find_all('a',class_ =link)

topic1_url = "https://github.com" + topic_link_tags[1]['href']
# print(topic1_url)
# print(topic_title_tags[12].text)

topic_titles = []
for tag in topic_title_tags:
    topic_titles.append(tag.text)

# print(topic_titles[:5])

topic_desc = []
for tag in topic_description:
    topic_desc.append(tag.text.strip())

# print(topic_desc[:5])

topic_URLs = []
base_url = "https://github.com"
for tag in topic_link_tags:
    topic_URLs.append(base_url+tag['href'])
# print(topic_URLs[:5]) 

import pandas as pd

topics_dictionary = {
    'Topic Title': topic_titles,
    'Topic Description': topic_desc,
    'Topic URLs': topic_URLs
}

topics_df = pd.DataFrame(topics_dictionary)

# print(topics_df)

