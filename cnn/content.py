import links
from DrissionPage import WebPage
from excel import parseContentToExcel
article_links = links.links

page = WebPage()
page.change_mode('s')
for link in article_links:
    page.get(link)
    # title
    # article
    title = page.ele('.post__title').text
    articleContainer = page.ele('.post__content')
    paragraphs = articleContainer.children('tag:p')
    artilce = ''
    for paragraph in paragraphs:
        artilce += paragraph.text
    print('标题------', title)
    print('文章------', artilce)
    # parseContentToExcel(title, artilce)
