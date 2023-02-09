import sys
from tech_news.scraper import get_tech_news
from tech_news.analyzer.search_engine import (
    search_by_title,
    search_by_date,
    search_by_category,
)
from tech_news.analyzer.ratings import top_5_categories


MENU_OPTIONS = """Selecione uma das opções a seguir:
 0 - Popular o banco com notícias;
 1 - Buscar notícias por título;
 2 - Buscar notícias por data;
 3 - Buscar notícias por categoria;
 4 - Listar top 5 categorias;
 5 - Sair."""


def _get_tech_news(input_value):
    return get_tech_news(input_value)


def _search_by_title(input_value):
    return search_by_title(input_value)


def _search_by_date(input_value):
    return search_by_date(input_value)


def _search_by_category(input_value):
    return search_by_category(input_value)


def _top_5_categories():
    return top_5_categories()


CHOICE_HANDLER = {
    "0": {
        "question": "Digite quantas notícias serão buscadas:",
        "callback": _get_tech_news,
    },
    "1": {
        "question": "Digite o título:",
        "callback": _search_by_title,
    },
    "2": {
        "question": "Digite a data no formato aaaa-mm-dd:",
        "callback": _search_by_date,
    },
    "3": {
        "question": "Digite a categoria:",
        "callback": _search_by_category,
    },
    "4": {
        "callback": _top_5_categories,
    },
}


# Requisitos 11 e 12
def analyzer_menu():
    choice = input(MENU_OPTIONS)

    if not choice.isdigit() or int(choice) > 5:
        print(ValueError("Opção inválida"), file=sys.stderr)
        return

    if int(choice) == 5:
        print("Encerrando script")
        return

    options = CHOICE_HANDLER[choice]
    response = ""

    if "question" not in options:
        response = options["callback"]()

    if "question" in options:
        param = input(options["question"])
        response = options["callback"](param)

    return response
