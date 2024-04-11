
from DrissionPage import WebPage
from DrissionPage.errors import *
from add_content import transform_content
# 创建对象


website = 'https://www.sapo.pt/'
categorys = ['noticias/ultimas', 'noticias/desporto', 'noticias/economia', 'noticias/entretenimento', 'noticias/viagens',
             'noticias/fama', 'noticias/tecnologia', 'noticias/planeta', 'noticias/regioes',
             'tag/israel', 'tag/ucrania', 'tag/habitacao']

# 获取需要的栏目链接
page = WebPage()


def getLinks(website):

    article_links = []
    tag = 0
    for category in categorys:
        # 访问网页
        page.get(website + category)
        # 等待页面跳转
        page.wait.doc_loaded()
        # page.ele('.load-more-posts-category-special button-1').click()
        try:
            # 尝试访问页面元素的代码块
            # 这里放置你的代码，例如访问页面元素
            links = page.eles('tag:article')
            for link in links:
                link = link.ele('tag:a')
                if tag >= 40:
                    return article_links
                print(link.link)
                article_links.append(link.link)
                tag += 1
        except ElementLostError as e:
            print("页面元素失效：", e)
            continue
        except ElementNotFoundError as e:
            print("未找到元素错误：", e)
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
        # ElementNotFoundError:
        try:
            title = page.ele('tag:h1').text
        except ElementNotFoundError as e:
            print("未找到标题：", e)
            continue
        try:
            # data-activity-map=article-content
            articel_content = page.ele('.article-body-ctn')
            paragraphs = articel_content.eles('tag:p')
            # paragraphs = articel_content.eles('tag:p:not(:has(a))')
        except ElementNotFoundError as e:
            print("未找到内容模块：", e)
            continue
        # for content in articel_content:
        # if paragraphs is None:
        #     print("未找到内容")
        #     continue
        artilce = ''
        for paragraph in paragraphs:
            artilce += paragraph.text
        transform_content(title, artilce)


getContent()
