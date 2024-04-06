
from DrissionPage import WebPage
from DrissionPage.errors import *
from add_content import transform_content
# 创建对象


website = 'https://www.goal.com/en/news'

# 获取需要的栏目链接
page = WebPage()


def getLinks(website):

    article_links = []
    
    # 点击5次更多按键，获取到前5页的数据
    for i in range(5):
        # 访问网页
        page.get(website + '/' + str(i+1))
        # 等待页面跳转
        page.wait.load_start()
        try:
            # 尝试访问页面元素的代码块
            # 这里放置你的代码，例如访问页面元素
            links = page.eles('@data-testid=card-title-url')
            for link in links:
                if link.link is None:
                    print("链接为空")
                    continue
                print(link.link)
                article_links.append(link.link)
        except ElementLostError as e:
            print("页面元素失效：", e)
            continue 
    print(len(article_links))
    return article_links


def getContent():
    article_links = []
    article_links = getLinks(website)
    print(len(article_links))
    # 关闭浏览器
    page.quit()
    page.change_mode('s')
    for link in article_links:
        page.get(link)
        title_elements = page.eles('@data-testid=article-title')
        title = ""
        for title_element in title_elements:
            title += title_element.text.strip() + " "
            if not title.strip():
                print("未找到标题")
                continue
            articleContainers = page.eles('@data-testid=article-body')
            for articleContainer in articleContainers:
                if articleContainer is None:
                    print("未找到内容")
                    continue
                paragraphs = articleContainer.children('tag:p')
                if paragraphs is None:
                    print("未找到内容")
                    continue
        artilce = ''
        for paragraph in paragraphs:
            artilce += paragraph.text
        transform_content(title, artilce)


