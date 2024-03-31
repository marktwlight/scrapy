import requests
from bs4 import BeautifulSoup

# 获取列表页 HTML 内容


def get_list_page(url):
    try:
        response = requests.get(url, timeout=30)
        return response.text
    except requests.Timeout:
        print(f"请求超时: {url}")
        return None
    except requests.RequestException as e:
        print(f"请求发生错误: {url}, {e}")
        return None
    except Exception as e:
        print(f"其他异常: {url}, {e}")
        return None


article_links = []


def parse_new_link(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')

    for link in soup.find_all('a', class_='td-image-wrap'):
            article_links.append(link['href'])


# https://cinepop.com.br/category/noticias-101/page/4/


for i in range(1, 2):
    url = 'https://cinepop.com.br/category/noticias-101/page/' + str(i) + '/'
    print(url)
    htmlStr = get_list_page(url)
    if htmlStr is not None:
        parse_new_link(htmlStr)
    else:
        continue


print(len(article_links), "article_links")
