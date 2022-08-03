import requests
import bs4
import webbrowser
import sys


class Yandex_news():

  def search_news(self, word ):
    word
    heder_var = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                 'Accept-Encoding': 'gzip, deflate, br',
                 'Accept-Language': 'ru,en;q=0.9',
                 'Cache-Control': 'max-age=0',
                 'Connection': 'keep-alive',
                 'Cookie': 'nc=search-visits-per-week=2:1659501979000; is_gdpr=0; is_gdpr_b=CNzDcxCCfCgC; '
                           'yandexuid=5680675011656748105; yuidss=5680675011656748105; _ym_uid=1656758354240876561; amcuid=6533897611656790850; gdpr=0; L=W0pBYV9uVWd8BAFaYmNGf0JAV3ledH1kFSIcU2Q9fgMmIA==.1656820923.15027.374392.0e080a7ce21ffd13e837e176960c19dc; yandex_login=Tryd0g0lik; mda=0; my=YwA=; ymex=1972108111.yrts.1656748111#1972182285.yrtsi.1656822285; font_loaded=YSv1; _ym_d=1658187370; i=+2f2XAbTHsYoA6mLLKcxjOKUFCSyRm9RP3/iVFqrqRE3s/PAAwGAyXiHel+vYrmjKyPWXrV0iW2gA/2NCu1TGd04Jbc=; Session_id=3:1659321669.5.0.1656820923030:-XOubQ:3.1.1:czoxNjQ3MTQ5NjU2NTI5OkFYS3ViUTo1Mw.2:1|69125096.-1.2|3:10256103.449382.9cCY46lcOwgoM8jVhEU-ta-DxAA; sessionid2=3:1659321669.5.0.1656820923030:-XOubQ:3.1.1:czoxNjQ3MTQ5NjU2NTI5OkFYS3ViUTo1Mw.2:1.499:1|69125096.-1.2|3:10256103.102765.SxOZ00BvmDoiHneZltco1cNzuQg; sae=0:0D1CC87D-BC41-4059-8340-0AF6D7ECB056:p:22.7.1.806:w:d:RU:20211127; _ym_isad=2; yabs-frequency=/5/6W0T01B-wM8F_UHY/; _yasc=c2zDeYTqQWf2OfeuWlwReFoJmJGJyQuXwbPlZSrwylVUZYiS63hleAyeHcqt9AQuO0neeA==; ys=svt.1#def_bro.1#ead.A861E561#wprid.1659503775964227-12705760278426553124-vla1-2557-vla-l7-balancer-exp-8080-BAL-6200#ybzcc.ru#newsca.native_cache; yp=1659588511.uc.ru#1659588511.duc.ru#1688284111.cld.2226550#1659512348.gpauto.55_030197:82_920433:100000:3:1659505148#1962612516.multib.1#1964426882.pcs.1#1664834882.sz.1880x877x2#1671225140.szm.1_100000023841858:1920x1080:1745x855#1972180923.udn.cDpUcnlkMGcwbGlr#1660255335.csc.1#1659919038.mcl.1s9mb7b#1660106897.mcv.0; substantial=1',
                 'Host': 'newssearch.yandex.ru',
                 'Referer': 'https://yandex.ru/',
                 'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="102", "Yandex";v="22"',
                 'sec-ch-ua-mobile': '?0',
                 'sec-ch-ua-platform': "Windows",
                 'Sec-Fetch-Dest': 'document',
                 'Sec-Fetch-Mode': 'navigate',
                 'Sec-Fetch-Site': 'same-site',
                 'Sec-Fetch-User': '?1',
                 'Upgrade-Insecure-Requests': '1',
                 'User-Agent': '''Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.134 YaBrowser/22.7.1.806 Yowser/2.5 Safari/537.36Y-Browser-Experiments: NjEzNTk5LDAsLTE='''}
    word = str(word).replace("+", " ")

    response = requests.get(f'https://newssearch.yandex.ru/news/search?text={word}', headers = heder_var)
    response_txt = response.text
    soup = bs4.BeautifulSoup(response_txt, features='html.parser')


    object_soup = soup.find_all('article', class_="news-search-story news-search__main-item mg-grid__item")
    dict_var = []

    for object_link_soup in object_soup:
      # print("object_link_soup:_", object_link_soup)
      try:
        object_div = object_link_soup.find('div', class_='news-search-story__head')
        objeck_h2_link = object_div.find('h2', class_='news-search-story__title')
        object_link = object_div.find('a', class_="news-search-story__title-link")
        object_time_link = object_div.find('span', class_="news-search-story__time").text

        prwie_news = soup.find('div', class_='mg-text-cut mg-snippet__description')
        prewie_work = prwie_news.find_all('em', class_='news-search-story__searched')

      except (AttributeError, UnboundLocalError) as re:
#         print(f"""{re}
# and
# {sys.exc_info()}""")
        pass
      for w in word.split(" "):
        for em in prewie_work:

          em = em.text
          if str(object_link_soup).lower().find(word[:-1]) != -1 or str(em).find(w[:-1]) != -1:
            href = object_link['href']
            # print(object_link.text, '-------', object_time_link, '-------', href)
            dict_var.append({str(object_link.text).replace('\xa0', '') : [object_time_link, href]})


          elif str(object_link_soup).lower().find(word) == -1:
            # print("11111")
            pass
    return dict_var






    # print(object_soup)