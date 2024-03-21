import requests

# 获取文章链接列表,网络请求超时处理
def get_article_links(url_pattern, start_page, end_page):
    article_links = []
    for i in range(start_page, end_page + 1):
        url = url_pattern.format(i)
        print(url)
        try:
            response = requests.get(url, timeout=30)
            if response.ok and 'application/json' in response.headers.get('content-type', ''):
                data = response.json()
                items = data.get('items', [])
                for item in items:
                    content = item.get('content', {})
                    url = content.get('url','')
                    if 'edicao' not in url and 'videos' not in url:
                        article_links.append(url)
            else:
                print(f"Failed to fetch data from {url}")
        except requests.Timeout:
                continue
        except requests.RequestException as e:
                continue
        except Exception as e:
                continue
   
    return article_links

# ITAPETININGA E REGIÃO 
# https://falkor-cda.bastian.globo.com/tenants/g1/instances/66162329-e22a-4ff4-8091-0f4c7c933510/posts/page/4
# GOIÁS
# https://falkor-cda.bastian.globo.com/tenants/g1/instances/5de8a589-29a6-4e3b-add5-8cb4040717f4/posts/page/6

# 定义列表页 URL 模板和起始页码、结束页码
url_pattern = 'https://falkor-cda.bastian.globo.com/tenants/g1/instances/66162329-e22a-4ff4-8091-0f4c7c933510/posts/page/{}'
start_page = 1
end_page = 100  # 设置结束页码

# 获取文章链接列表
article_links = get_article_links(url_pattern, start_page, end_page)

# 打印文章链接数量
print(len(article_links), "article links")
print(article_links)
