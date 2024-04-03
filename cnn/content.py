
from DrissionPage import WebPage
from DrissionPage.errors import *
from excel import parseContentToExcel
# 创建对象


website = 'https://www.cnnbrasil.com.br'

# 获取需要的栏目链接
page = WebPage()

# 获取Politica 的分页链接


def getPoliticaLinks(website):
    page = WebPage()
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
    print(links)
    # 修改为sessionPage 模式

    for link in links:

        if link.link is not None:
            article_links.append(link.link)
    return article_links

# 获取Economia中的分页链接


def getEconomiaLinks(website):
    page.change_mode('d')
    article_links = []
    # 访问网页
    page.get(website)
    print(page)
    page('.economia menu-item economia').click()
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

    for link in links:
        print(link)
        if link.link is not None:
            article_links.append(link.link)
    return article_links


# economia_links = getEconomiaLinks(website)


def getContent():
    article_links = getPoliticaLinks(website)
    page.change_mode('s')
    for link in article_links:
        page.get(link)
        title = page.ele('.post__title').text
        articleContainer = page.ele('.post__content')
        paragraphs = articleContainer.children('tag:p')
        artilce = ''
        for paragraph in paragraphs:
            artilce += paragraph.text
        parseContentToExcel(title, artilce)

getContent()