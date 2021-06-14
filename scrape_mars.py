# Seting up dependacies for MongoDB and Flask application

from splinter import Browser
from bs4 import BeautifulSoup as bs
import pandas as pd
import pymongo
import requests
import time

def init_browser():
    executable_path = {"executable_path": "/usr/local/bin/chromedriver"}
    return Browser("chrome", **executable_path, headless=False)

def scrape():
    browser = init_browser()

    # NASA Mars News define and retrive
    url = 'https://mars.nasa.gov/news/'
    browser.visit(url)
    time.sleep(1)
    html = browser.html
    mysoup = bs(html, "html.parser")
    # Scrape for title and text
    news_title = mysoup.find('li', class_='slide').find('div', class_='content_title').text
    news_p = mysoup.find('li', class_='slide').find('div', class_='article_teaser_body').text

    # Mars Images define and retrive
    image_url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    # web page gives 404 Error



    # Mars Facts
    # Have pandas read any tables on mars facts page
    facts_url = 'https://space-facts.com/mars/'
    fact_table = pd.read_html(facts_url)
    # Filter to table I want to work with
    fact_df = fact_table[0]
    # Rename columns
    fact_df.columns = ["Description", "Mars"]
    # Remove Index/set new
    facts = fact_df.set_index("Description")
    # Convert to html string & clean
    html_facts = facts.to_html()
    html_facts = html_facts.replace('\n', '')