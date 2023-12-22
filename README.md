# GitHub Topic Scraper
This Python script is a web scraping tool developed to extract information about the top repositories hosted on GitHub across various topics. It utilizes Requests library for fetching web pages and BeautifulSoup for parsing HTML content. The extracted data includes repository names, usernames, star counts, and URLs.

# Purpose
The script aims to assist in gathering insights into trending repositories within specific topics on GitHub. It provides a means to systematically retrieve information about repositories that are popular or trending under different thematic categories.

# Requirements
- Python 3.x
- Requests library (pip install requests)
- BeautifulSoup (pip install beautifulsoup4)
- Pandas (pip install pandas)


# How to Use
- Clone or download the repository.
- Install the required Python libraries using pip.
- Run the script in your Python environment.
    python <Scrapper.py>

# Functions

## parse_star_count(stars_str)
    Parses star counts from strings ending with 'k' (e.g., 2.3k) into integer values.
## get_topic_page(topics_url)
    Fetches the HTML content of the GitHub Topics page using Requests and BeautifulSoup.
## get_repo_info(h3_tag, star_tags)
    Extracts information about the repository (username, repository name, stars, and repository URL) from HTML tags.
## get_topic_repos(topic_doc)
    Retrieves information about repositories listed under a specific topic.
## scrape_topic(topic_url, path)
    Scrapes repositories under a topic and saves the data to a CSV file.
## get_topic_title(doc), get_topic_description(doc), get_topic_urls(doc)
    Functions to extract topic titles, descriptions, and URLs from the GitHub Topics page.
# scrape_topics()
    Scrapes information about various topics available on GitHub.
# scrape_topics_repos()
    Initiates the scraping process for all topics and saves data into individual CSV files.

# Usage
Upon execution, the script performs the following actions:
- Fetches a list of GitHub topics.
- Retrieves details about each topic, including titles, descriptions, and URLs.
- Scrapes repositories for each topic and stores the collected data in CSV files within a 'data' directory.