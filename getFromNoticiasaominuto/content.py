
from DrissionPage import WebPage
from DrissionPage.errors import *
from excel import parseContentToExcel
# 创建对象


website = 'https://www.noticiasaominuto.com/'
categorys = ['politica','economia','desporto','fama','pais','mundo','tech','cultura','lifestyle']

# 获取需要的栏目链接
page = WebPage()


def getLinks(website):

    article_links = []
    
    for category in categorys:
        # 访问网页
        page.get(website + category)
        # 等待页面跳转
        page.wait.doc_loaded()
        try:
            # 尝试访问页面元素的代码块
            # 这里放置你的代码，例如访问页面元素
            links = page.eles('@class=article-thumb-text')
            for link in links:
                link = link.ele('tag:a')
                print(link.link)
                article_links.append(link.link)
        except ElementLostError:
            print("页面元素失效：")
            continue
        except ElementNotFoundError:
            print("未找到匹配的a标签")
            continue
        print(category+':'+str(len(article_links)))
    return article_links


def getContent():
    article_links = []
    article_links = getLinks(website)
    print(len(article_links))
    # 关闭浏览器
    page.quit()
    page.change_mode('s')
    for link in article_links:
        print(link)
        page.get(link)
        title = page.ele('.news-headline article-title').text
        articleContainer = page.ele('.news-main-text content')
        paragraphs = articleContainer.children('tag:p')
        if paragraphs is None:
            print("未找到内容")
            continue
        artilce = ''
        for paragraph in paragraphs:
            artilce += paragraph.text
        parseContentToExcel(title, artilce)

