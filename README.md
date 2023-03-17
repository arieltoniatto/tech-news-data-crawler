# Tech News Data Crawler  :space_invader:
Seja bem vindo ao Tech News Data Crawler. Este projeto foi desenvolvido durante o módulo de ciências da computação da [Trybe](https://www.betrybe.com/).


## Sobre o projeto :information_source:

  Você fará um projeto que tem como principal objetivo fazer consultas em notícias sobre tecnologia.
  Foi utilizado como fonte principal para raspagem de dados o [_blog da Trybe_](https://blog.betrybe.com). 
  As informações obtidas foram extraídas do HTML e armazenadas em um banco de dados NoSQL _MongoDB_.

## Tecnologias
- Python
- MongoDB
- Pymongo
- Parsel
- Pytest
- Requests
- Re
- Typing
- Sys 
- Docker

## Rodando o projeto
1. clone o repositório para a sua máquina através do seu terminal utilizando o comando 

* `git clone git@github.com:arieltoniatto/tech-news-data-crawler.git`

2. Crie o ambiente virtual para o projeto

* `python3 -m venv .venv && source .venv/bin/activate`
  
 3. Instale as dependências

* `python3 -m pip install -r dev-requirements.txt`

4. Rode o MongoDB via docker

* `docker-compose up -d mongodb`

## Funcionalidades

  Abra um terminal Python importando estas funções através do comando:

  `python3 -i tech_news/scraper.py`

  Agora invoque as funções utilizando diferentes parâmetros.
  Exemplo:

* Raspar os dados
  ```python
  html = fetch(url_da_noticia)
  scrape_news(html)
  ```
 
 * Atualizar os dados
	  ```python
	  html = fetch(url_da_noticia)
	  scrape_updates(html)
	  ```

* Acessar o menu interativo

	`python3 -i tech_news/menu.py`

Chame pela função `analyzer_menu()` e escolha uma das 5 opções.


## Contato

* Email: ariel.toniatto@gmail.com
* LinkedIn: https://www.linkedin.com/in/ariel-toniatto/
