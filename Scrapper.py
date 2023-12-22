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

topics_df .to_csv('Topics.csv')

#########

topic_page_url = topic_URLs[0]
# print(topic_page)
response = requests.get(topic_page_url)
# print(response.status_code)



topic_doc = BeautifulSoup(response.text, 'html.parser')
h3_selector = 'f3 color-fg-muted text-normal lh-condensed'
repo_tags = topic_doc.find_all('h3', class_ = h3_selector)

# print(len(repo_tags))
# print(repo_tags[2])
a_tags = repo_tags[0].find_all('a')
# print(a_tags[0])
username = a_tags[0].text.strip()
# print(username)
repo_name = a_tags[1].text.strip()
# print(repo_name)
repo_url = base_url + a_tags[1]['href']
# print(repo_url)

stars_selector = "Counter js-social-count"
star_tags = topic_doc.find_all("span",class_ = stars_selector )
# print(star_tags[0].text)

def parse_star_count(stars_str):
    stars_str = stars_str.strip()
    if stars_str[-1] == 'k':
        return int(float(stars_str[:-1])*1000)
    return (int(stars_str))

# print(parse_star_count(star_tags[5].text.strip()))

# topic_repos_dict = {
#     'Username': [],
#     'Repo_name': [],
#     'Stars': [],
#     'Repo_URL': []
# }

# for i in range(len(repo_tags)):
#     repo_info = get_repo_info(repo_tags[i], star_tags[i])
#     topic_repos_dict['Username'].append(repo_info[0])
#     topic_repos_dict['Repo_name'].append(repo_info[1])
#     topic_repos_dict['Stars'].append(repo_info[2])
#     topic_repos_dict['Repo_URL'].append(repo_info[3])

def get_topic_page(topics_url):
    response = requests.get(topics_url)
    if response.status_code != 200:
        raise Exception('Failed to load page {}'.format(topics_url))
    
    topic_doc = BeautifulSoup(response.text, 'html.parser')

    return topic_doc

def get_repo_info(h3_tag, star_tags):
    a_tags = h3_tag.find_all('a')
    username = a_tags[0].text.strip()
    repo_name = a_tags[1].text.strip()
    repo_url = base_url + a_tags[1]['href']
    stars = parse_star_count(star_tags.text.strip())
    return username, repo_name, stars, repo_url

def get_topic_repos(topic_doc):  
    h3_selector = 'f3 color-fg-muted text-normal lh-condensed'
    repo_tags = topic_doc.find_all('h3', class_ = h3_selector)

    stars_selector = "Counter js-social-count"
    star_tags = topic_doc.find_all("span",class_ = stars_selector )

    topic_repos_dict = {
        'Username': [],
        'Repo_name': [],
        'Stars': [],
        'Repo_URL': []
    }

    for i in range(len(repo_tags)):
        repo_info = get_repo_info(repo_tags[i], star_tags[i])
        topic_repos_dict['Username'].append(repo_info[0])
        topic_repos_dict['Repo_name'].append(repo_info[1])
        topic_repos_dict['Stars'].append(repo_info[2])
        topic_repos_dict['Repo_URL'].append(repo_info[3])

    return pd.DataFrame(topic_repos_dict)



# url7 = topic_URLs[7]
# topic7_doc = get_topic_page(url7)
# topic7_repos = get_topic_repos(topic7_doc)

# print(topic7_repos)

get_topic_repos(get_topic_page(topic_URLs[4])).to_csv('Android.csv', index = None)

def get_topic_title(doc):
    title_selection = "f3 lh-condensed mb-0 mt-1 Link--primary"
    topic_title_tags = doc.find_all('p', class_=title_selection)
    topic_titles = []
    for tag in topic_title_tags:
        topic_titles.append(tag.text)
    return topic_titles

def get_topic_description(doc):
    

def scrape_topics():
    topics_url = 'https://github.com/topics'
    response = requests.get(topics_url)
    if response.status_code != 200:
        raise Exception('Failed to load page {}'.format(topics_url))
    
    description = 'f5 color-fg-muted mb-0 mt-1'
    topic_description = doc.find_all('p', class_ = description)

    link = "no-underline flex-grow-0"
    topic_link_tags = doc.find_all('a',class_ =link)

    

    topic_desc = []
    for tag in topic_description:
        topic_desc.append(tag.text.strip())

    topic_URLs = []
    base_url = "https://github.com"
    for tag in topic_link_tags:
        topic_URLs.append(base_url+tag['href'])




def scrape_topics_repos():
