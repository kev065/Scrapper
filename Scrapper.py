import requests
from bs4 import BeautifulSoup
import pandas as pd
import os


base_url = "https://github.com"
topics_url = 'https://github.com/topics'


def parse_star_count(stars_str):
    stars_str = stars_str.strip()
    if stars_str[-1] == 'k':
        return int(float(stars_str[:-1])*1000)
    return (int(stars_str))


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

doc = get_topic_page(topics_url)

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


def scrape_topic(topic_url, path):
    if os.path.exists(path):
        print(f"The file {path} already exists. Skipping")
    topic_df = get_topic_repos(get_topic_page(topic_url))
    topic_df.to_csv(path, index = None)


def get_topic_title(doc):
    title_selection = "f3 lh-condensed mb-0 mt-1 Link--primary"
    topic_title_tags = doc.find_all('p', class_=title_selection)
    topic_titles = []
    for tag in topic_title_tags:
        topic_titles.append(tag.text)
    return topic_titles

def get_topic_description(doc):
    description = 'f5 color-fg-muted mb-0 mt-1'
    topic_descs = doc.find_all('p', class_ = description)
    topic_descriptions = []
    for tag in topic_descs:
        topic_descriptions.append(tag.text.strip())
    return topic_descriptions

def get_topic_urls(doc):
    link = "no-underline flex-grow-0"
    topic_link_tags = doc.find_all('a',class_ =link)
    topic_URLs = []
    base_url = "https://github.com"
    for tag in topic_link_tags:
        topic_URLs.append(base_url+tag['href'])
    return topic_URLs

def scrape_topics():
    topics_url = 'https://github.com/topics'
    response = requests.get(topics_url)
    if response.status_code != 200:
        raise Exception('Failed to load page {}'.format(topics_url))
    
    topics_dictionary = {
        'title': get_topic_title(doc),
        'description': get_topic_description(doc),
        'url': get_topic_urls(doc)
    }
    return pd.DataFrame(topics_dictionary)


def scrape_topics_repos():
    print('Scraping list of topics')
    topics_df = scrape_topics()
    os.makedirs('data',exist_ok=True)
    for index, row in topics_df.iterrows():
        print('Scraping top repositories for "{}"'.format(row['title']))
        scrape_topic(row['url'], 'data/{}.csv'.format(row['title']))
    return 'Scrapping Completed'



if __name__ == '__main__':
    scrape_topics_repos()