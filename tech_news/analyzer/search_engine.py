from tech_news.database import search_news


# Requisito 7
def search_by_title(title):
    get_news = search_news({"title": {"$regex": title, "$options": "i"}})
    news_list = []
    for news in get_news:
        news_list.append((news["title"], news["url"]))
    return news_list


# Requisito 8
def search_by_date(date):
    """Seu código deve vir aqui"""


# Requisito 9
def search_by_category(category):
    get_news = search_news({"category": {"$regex": category, "$options": "i"}})
    news_list = []
    for news in get_news:
        news_list.append((news["title"], news["url"]))
    return news_list
