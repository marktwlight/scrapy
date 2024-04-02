import links
from DrissionPage import WebPage

article_links = links.links

page = WebPage()
page.change_mode('s')
for link in article_links:
    page.get(link)
    print(page.html)
