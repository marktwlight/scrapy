
from DrissionPage import WebPage
from excel import parseContentToExcel


page = WebPage()
page.change_mode('s')


def getContent(article_links):
    for link in article_links:
        page.get(link)
        title = page.ele('.post__title').text
        articleContainer = page.ele('.post__content')
        paragraphs = articleContainer.children('tag:p')
        artilce = ''
        for paragraph in paragraphs:
            artilce += paragraph.text

        parseContentToExcel(title, artilce)
