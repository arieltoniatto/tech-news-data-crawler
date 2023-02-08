import requests
from parsel import Selector
from time import sleep

HEADERS = {"user-agent": "Fake user-agent"}


# Requisito 1
def fetch(url):
    try:
        sleep(1)
        response = requests.get(
            url,
            headers=HEADERS
        )
        if response.status_code == 200:
            return response.text
        return None
    except requests.ReadTimeout:
        return None


# Requisito 2
def scrape_updates(html_content):
    selector = Selector(html_content)
    news_urls = selector.css(".entry-title a::attr(href)").getall()
    if len(news_urls) == 0:
        return []
    return news_urls


# Requisito 3
def scrape_next_page_link(html_content):
    selector = Selector(html_content)
    next_url = selector.css(".next::attr(href)").get()
    if not next_url:
        return None
    return next_url


# Requisito 4
def scrape_news(html_content):
    """Seu código deve vir aqui"""


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
