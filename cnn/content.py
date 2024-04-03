
from DrissionPage import WebPage
from DrissionPage.errors import *
from excel import parseContentToExcel
# 创建对象


website = 'https://www.cnnbrasil.com.br'

# 获取需要的栏目链接
page = WebPage()


new_category = {
    'Política': '.politica-2 menu-item politica',
    'Economia': '.economia menu-item economia',
    'Esportes': '.esportes menu-item esportes',
    'Pop': '.entretenimento-2 menu-item pop',
}


def getLinks(website, item):

    article_links = []
    # 访问网页
    page.get(website)
    page(item).click()
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
    for link in links:

        if link.link is not None:
            article_links.append(link.link)
    return article_links


def getContent():
    article_links = []
    for category, item in new_category.items():
        links = getLinks(website, item)
        article_links.extend(links)

    # 关闭浏览器
    page.quit()
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
