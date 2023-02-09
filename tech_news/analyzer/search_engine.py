from datetime import datetime
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
    try:
        formated_date = datetime.fromisoformat(date).strftime("%d/%m/%Y")

        get_news = search_news({"timestamp": formated_date})
        news_list = []
        for news in get_news:
            news_list.append((news["title"], news["url"]))
        return news_list
    except ValueError:
        raise ValueError("Data inválida")


# Requisito 9
def search_by_category(category):
    get_news = search_news({"category": {"$regex": category, "$options": "i"}})
    news_list = []
    for news in get_news:
        news_list.append((news["title"], news["url"]))
    return news_list
