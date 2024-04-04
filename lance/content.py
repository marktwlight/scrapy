
from DrissionPage import WebPage
from DrissionPage.errors import *
from excel import parseContentToExcel
# 创建对象


website = 'https://www.lance.com.br'

# 获取需要的栏目链接
page = WebPage()


def getLinks(website):

    article_links = []
    # 访问网页
    page.get(website)
    # page.ele('.hideScrollbar')
    print('hideScrollbar', page.ele('.hideScrollbar'))
    # 等待页面跳转
    page.wait.load_start()


def getContent():
    article_links = []
    links = getLinks(website)
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
