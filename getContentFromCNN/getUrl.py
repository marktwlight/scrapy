import requests
import re
from bs4 import BeautifulSoup
from Urls import urls,params
# 获取文章链接列表,网络请求超时处理


def get_article_links(url_pattern):
    article_links = []
    print(url_pattern)
    try:
        response = requests.get(url_pattern,params=params, timeout=30)
        if response.ok and 'text/html' in response.headers.get('content-type', ''):
            soup = BeautifulSoup(response.content, 'html.parser')
            links = soup.find_all('a', class_='home__list__tag')
            # links = soup.select('a[href*="/noticia/"]')
            for link in links:
                href= link['href']
                # 只采集文本类的新闻链接politica
                # if re.search(r'/noticia/', href):
                # if re.search(r'/politica/', href):
                article_links.append(href)
        else:
            print(f"Failed to fetch data from {url_pattern}")
    except requests.Timeout:
        pass
    except requests.RequestException as e:
        pass
    except Exception as e:
        pass 
        

    return article_links


# ITAPETININGA E REGIÃO   2024/3/22
# https://falkor-cda.bastian.globo.com/tenants/g1/instances/66162329-e22a-4ff4-8091-0f4c7c933510/posts/page/4
# GOIÁS 2024/3/22
# https://falkor-cda.bastian.globo.com/tenants/g1/instances/5de8a589-29a6-4e3b-add5-8cb4040717f4/posts/page/6
# POLÍTICA 2024/3/22
# https://falkor-cda.bastian.globo.com/tenants/g1/instances/1b9deafa-9519-48a2-af13-5db036018bad/posts/page/4
# Esporte 2024/3/22
# https://falkor-cda.bastian.globo.com/tenants/ge/instances/10045b9c-e4d8-4a1a-9909-02240f8ef217/posts/page/4
# SANTOS E REGIÃO 2024/3/22
# https://falkor-cda.bastian.globo.com/tenants/g1/instances/a6244a3c-a5eb-45ae-b958-1d317208434d/posts/page/4
# CARROS 2024/3/22
# https://falkor-cda.bastian.globo.com/tenants/g1/instances/97f461e5-0b30-4257-a2a3-501d24eb9e70/posts/page/4
# Mais 2024/3/22
# https://falkor-cda.bastian.globo.com/tenants/gshow/instances/1838c598-21e3-4d74-bc3d-bd7d19d87a9a/posts/page/4

# Brasil 2024/3/25
#https://falkor-cda.bastian.globo.com/tenants/oglobo/instances/76021b97-8e0f-425c-87a6-a933ffe47320/posts/page/6
# urls = {
#     "ITAPETININGA E REGIÃO": "https://falkor-cda.bastian.globo.com/tenants/g1/instances/66162329-e22a-4ff4-8091-0f4c7c933510/posts/page/{}",
#     "GOIÁS": "https://falkor-cda.bastian.globo.com/tenants/g1/instances/5de8a589-29a6-4e3b-add5-8cb4040717f4/posts/page/{}",
#     "POLÍTICA": "https://falkor-cda.bastian.globo.com/tenants/g1/instances/1b9deafa-9519-48a2-af13-5db036018bad/posts/page/{}",
#     "Esporte": "https://falkor-cda.bastian.globo.com/tenants/ge/instances/10045b9c-e4d8-4a1a-9909-02240f8ef217/posts/page/{}",
#     "SANTOS E REGIÃO": "https://falkor-cda.bastian.globo.com/tenants/g1/instances/a6244a3c-a5eb-45ae-b958-1d317208434d/posts/page/{}",
#     # "CARROS": "https://falkor-cda.bastian.globo.com/tenants/g1/instances/97f461e5-0b30-4257-a2a3-501d24eb9e70/posts/page/{}",  新闻太少
#     "Mais": "https://falkor-cda.bastian.globo.com/tenants/gshow/instances/1838c598-21e3-4d74-bc3d-bd7d19d87a9a/posts/page/{}",
#     "Brasil": "https://falkor-cda.bastian.globo.com/tenants/oglobo/instances/76021b97-8e0f-425c-87a6-a933ffe47320/posts/page/{}",
#     "politica": "https://www.cnnbrasil.com.br/cnn-brasil-block-list-ajax?action=cnnbrasilBlockListAjax&nounce=66f60a595b&page=1&perpage=100"
# }

# 打印字典中的键和对应的 URL


# 定义列表页 URL 模板和起始页码、结束页码
# url_pattern = 'https://falkor-cda.bastian.globo.com/tenants/oglobo/instances/76021b97-8e0f-425c-87a6-a933ffe47320/posts/page/{}'
start_page = 1
end_page = 5  # 设置结束页码
news_category = list(urls.keys())[0]
# 获取文章链接列表
article_links = get_article_links(urls[news_category]) 

# 打印文章链接数量
print(len(article_links), "article links")
print(article_links)
