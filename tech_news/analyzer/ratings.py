from tech_news.database import search_news
from collections import Counter


# Requisito 10
def top_5_categories():
    all_news = search_news({})

    category_list = []

    for news in all_news:
        category_list.append(news["category"])

    count_list = Counter(category_list).items()

    sort_categories = sorted(
        count_list, key=lambda d: (-d[1], d[0])
    )

    top_5 = []

    for category in sort_categories:
        top_5.append(category[0])

    if len(top_5) > 5:
        top_5 = top_5[:5]

    return top_5
