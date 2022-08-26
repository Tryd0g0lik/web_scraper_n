from scraper.news_yandex import Yandex_news

if __name__ == ('__main__'):
  print("Для поиска в Яндекс Новости")
  search_word = input(": ")

  search_word = search_word.replace(" ", "+")
  print(search_word)
  news_today = Yandex_news()
  news = news_today.search_news(search_word)
  print(news)