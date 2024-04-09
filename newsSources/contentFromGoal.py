# from translateArticle import translate_text
# from DrissionPage import WebPage
# from DrissionPage.errors import *
# from add_content import transform_content
# # 创建对象


# website = 'https://www.goal.com/en/news'

# # 获取需要的栏目链接
# page = WebPage()


# def getLinks(website):

#     article_links = []

#     # 点击5次更多按键，获取到前5页的数据
#     for i in range(5):
#         # 访问网页

#         page.get(website + '/' + str(i+1))
#         # 等待页面跳转
#         # page.wait.load_start()
#         try:
#             # 尝试访问页面元素的代码块
#             # 这里放置你的代码，例如访问页面元素
#             links = page.eles('@data-testid=card-title-url')
#             for link in links:
#                 if link.link is None:
#                     print("链接为空")
#                     continue
#                 if len(article_links) >= 60:
#                     return article_links
#                 print(link.link)
#                 article_links.append(link.link)

#         except ElementLostError as e:
#             print("页面元素失效：", e)
#             continue
#     print(len(article_links))

#     return article_links


# def getContent():
#     article_links = []
#     article_links = getLinks(website)
#     print(len(article_links))
#     # 关闭浏览器
#     page.quit()
#     page.change_mode('s')
#     for link in article_links:
#         page.get(link)
#         title_element = page.ele('@data-testid=article-title')
#         title = title_element.text.strip()
#         print("title", title)
#         articles = page.eles('@data-testid=article-body')

#         print(len(articles))
#         for paragraph in articles:
#             print(paragraph.ele('tag:p').strip().text)

#         # for paragraph in paragraphs:
#         #     article += paragraph.text

#         # print('article', article)
#         # title = translate_text(title)
#         # article = translate_text(article)
#         # print(title, article)
#         # transform_content(title, article)


# getContent()
