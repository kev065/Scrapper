import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


topics_url = 'https://github.com/topics'
response = requests.get(topics_url)
# print(response.status_code)
# print(len(response.text))
page_content = response.text

with open('webpage.html', 'w') as topics_list:
    topics_list.write(page_content)

print(topics_list)






