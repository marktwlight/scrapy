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

    for link in soup.find_all('a', class_='feed-post-link'):
        if 'videos' not in link['href']:
            article_links.append(link['href'])


# 环球新闻
#  https://oglobo.globo.com/brasil/index/feed/pagina-4.ghtml
# santa-catarina
# https://g1.globo.com/sc/santa-catarina/index/feed/pagina-7.ghtml
for i in range(1, 10):
    url = 'https://oglobo.globo.com/brasil/index/feed/pagina-' + str(i) + '.ghtml'
    print(url)
    htmlStr = get_list_page(url)
    if htmlStr is not None:
        parse_new_link(htmlStr)
    else:
        continue


print(len(article_links), "article_links")
