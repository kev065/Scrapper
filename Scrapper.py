from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

def get_static_content(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.content
    return None

def get_dynamic_content(url, chrome_driver_path):
    service = Service(chrome_driver_path)
    driver = webdriver.Chrome(service=Service)
    driver.get(url)
    dynamic_content = driver.page_source
    driver.quit()
    return dynamic_content

url = "https://google.com"

chrome_driver_path = "./chromedriver.exe"

static_content = get_static_content(url)
if static_content:
    soup_static = BeautifulSoup(static_content, 'html.parser')

dynamic_content = get_dynamic_content(url, chrome_driver_path)
if dynamic_content:
    soup_dynamic = BeautifulSoup(dynamic_content, 'html.parser')



if static_content:
    title = soup_static.title.text if soup_static.title else 'No Title found'
    print('Static Content Title:', title)

if dynamic_content:
    title_dynamic = soup_dynamic.title.text if soup_dynamic.titlt else "No title found"
    print('Dynamic Content Title:', title_dynamic)

