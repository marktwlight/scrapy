import requests
from bs4 import BeautifulSoup

import pandas as pd
import openpyxl
import os

import getHtml

print("================================",len(getHtml.article_links) )
# 获取列表页 HTML 内容\
    
links = getHtml.article_links
    
def get_list_page(url):
    try:
      response = requests.get(url, timeout=30)
      return response.text
    except requests.Timeout:
            print(f"请求超时: {url}")
            return None
    except requests.RequestException as e:
            print(f"请求发生错误: {url}, {e}")
            return None
    except Exception as e:
            print(f"其他异常: {url}, {e}")
            return None

def parseContentToExcel(content):
    # 使用BeautifulSoup解析HTML
    soup = BeautifulSoup(htmlContent, "html.parser")
    # 提取标题
    title = soup.find("h1", class_="content-head__title").text.strip()

    article_body = ""
    # 提取正文内容
    paragraphs = soup.find_all("p", class_="content-text__container")
    for paragraph in paragraphs:
        # 忽略所有子元素，只获取纯文本内容
        text = paragraph.text.strip()
        article_body += text
    # 输出标题和正文内容
    print("标题:", title)
    print("\n正文内容:", article_body)
    # 创建DataFrame
    data = pd.DataFrame({'文章标题（不能重复）': [title], '文章内容': [article_body]})
    current_directory = os.getcwd()
    filename = 'content.xlsx'
    absolute_path = os.path.join(current_directory,"getContent" ,filename)
    with pd.ExcelWriter(absolute_path, engine='openpyxl', mode='a',if_sheet_exists='overlay') as writer:
        data.to_excel(writer, index=False, sheet_name='alizhizhuchi', startrow=writer.sheets['alizhizhuchi'].max_row, header=False)

for link in links:
    print(link)
    htmlContent = get_list_page(link)
    if htmlContent is not None:
      parseContentToExcel(htmlContent)
    else: 
      continue



