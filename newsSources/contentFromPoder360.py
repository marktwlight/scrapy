
from DrissionPage import WebPage
from DrissionPage.errors import *
from add_content import transform_content
# 创建对象


website = 'https://www.poder360.com.br/'
categorys = ['governo','anuncios-do-governo','congresso','economia','justica','infraestrutura','poderdata','infograficos','eleicoes','internacional','tecnologia','midia','pesquisas','nieman']

# 获取需要的栏目链接
page = WebPage()


def getLinks(website):

    article_links = []
    
    for category in categorys:
        # 访问网页
        page.get(website + category + '/')
        # 等待页面跳转
        page.wait.doc_loaded()
        # page.ele('.load-more-posts-category-special button-1').click()
        try:
            # 尝试访问页面元素的代码块
            # 这里放置你的代码，例如访问页面元素
            links = page.eles('@class=box-queue__data')
            for link in links:
                link = link.ele('tag:a')
                print(link.link)
                article_links.append(link.link)
        except ElementLostError as e:
            print("页面元素失效：", e)
            continue 
        except ElementNotFoundError as e:
            print("未找到元素错误：", e)
            continue
        print(category+':'+str(len(article_links)))
    return article_links


def getContent():
    article_links = getLinks(website)
    print(len(article_links))
    # 关闭浏览器
    page.quit()
    page.change_mode('s')
    for link in article_links:
        print(link)
        page.get(link)
        #ElementNotFoundError:
        try:
            title = page.ele('.inner-page-section__title title-1').text
        except ElementNotFoundError as e:
            print("未找到元素错误：", e)
            continue
        articleContainer = page.ele('.inner-page-section__text')
        paragraphs = articleContainer.children('tag:p')
        if paragraphs is None:
            print("未找到内容")
            continue
        artilce = ''
        for paragraph in paragraphs:
            artilce += paragraph.text
        transform_content(title, artilce)


getContent()