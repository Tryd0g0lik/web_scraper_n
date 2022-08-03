from scraper.news_yandex import Yandex_news

if __name__ == ('__main__'):

  news_today = Yandex_news()
  news = news_today.search_news('газпром')
  print(news)