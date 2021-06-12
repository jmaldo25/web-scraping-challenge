from splinter import Browser
from bs4 import BeautifulSoup as bs
import pandas as pd
import pymongo
import requests
import time

def init_browser():
    executable_path = {"executable_path": "/usr/local/bin/chromedriver"}
    return Browser("chrome", **executable_path, headless=False)

