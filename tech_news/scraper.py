import requests
import re
from parsel import Selector
from time import sleep
# from bs4 import BeautifulSoup


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
    return selector.css(".entry-title a::attr(href)").getall()


# Requisito 3
def scrape_next_page_link(html_content):
    selector = Selector(html_content)
    next_url = selector.css(".next::attr(href)").get()
    if not next_url:
        return None
    return next_url


# Requisito 4
def scrape_news(html_content):
    selector = Selector(html_content)
    dict_news = dict()
    dict_news["url"] = get_url(selector)
    dict_news["title"] = selector.css("h1.entry-title::text").get().strip()
    dict_news["timestamp"] = selector.css("li.meta-date::text").get()
    dict_news["writer"] = selector.css(".author a::text").get()
    dict_news["reading_time"] = get_reading_time(selector)
    dict_news["summary"] = remove_html_tags_from_str(selector).strip()
    dict_news["category"] = selector.css("span.label::text").get()
    return dict_news


def get_url(selector: Selector):
    complete_url = selector.css(
        "div.pk-share-buttons-facebook a::attr(href)"
    ).get()
    url = complete_url.split("https://www.facebook.com/sharer.php?u=")[1]
    return url


def get_reading_time(selector: Selector):
    full_time = selector.css("li.meta-reading-time::text").get()
    return int(full_time.split(" ")[0])


def remove_html_tags_from_str(selector: Selector) -> str:
    text = selector.css(".entry-content p").get()
    remover = re.compile(r'<.*?>')
    return remover.sub('', text)


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
