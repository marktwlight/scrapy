
from DrissionPage import WebPage
from DrissionPage.errors import *

# 创建对象
page = WebPage()

website = 'https://www.cnnbrasil.com.br'

# 获取需要的栏目链接


def getLinks(website):
    article_links = []
    # 访问网页
    page.get(website)
    page('.politica-2 menu-item politica').click()
    # 等待页面跳转
    page.wait.load_start()

    # 点击5次更多按键，获取到前5页的数据
    for i in range(5):
        try:
            # 尝试访问页面元素的代码块
            # 这里放置你的代码，例如访问页面元素
            page.ele('.block-list-get-more-btn').click()
        except ElementLostError as e:
            print("页面元素失效：", e)
            continue

    links = page.eles('.home__list__tag')
    # 修改为sessionPage 模式
    page.change_mode('s')
    for link in links:
        if link.link is not None:
            article_links.append(link.link)
    return article_links


article_links = getLinks(website)
print(len(article_links))