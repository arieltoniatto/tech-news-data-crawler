from tech_news.database import search_news


# Requisito 10
def top_5_categories():
    all_news = search_news({}).sort(key="timestamp")  # TA ERRADO
    print(all_news)
    if len(all_news) > 5:
        all_news = all_news[:5]
    list_top_5 = []
    for news in all_news:
        list_top_5.append((news["title"], news["url"]))
    return list_top_5
