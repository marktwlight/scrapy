import requests
from bs4 import BeautifulSoup

import pandas as pd
import openpyxl
import os

import getHtml

print("================================", len(getHtml.article_links))
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


def parseContentToExcel(htmlContent):
    # 使用BeautifulSoup解析HTML
    soup = BeautifulSoup(htmlContent, "html.parser")
    # 提取标题
    title = soup.find("h1", class_="tdb-title-text").text.strip()
    print(title)
    
    article_body = ""
    # 提取正文内容
    paragraphs = soup.find_all("p", attrs={"ppad": "true"})
    for paragraph in paragraphs:
        # 忽略所有子元素，只获取纯文本内容
        text = paragraph.text.strip()
        article_body += text
    # 输出标题和正文内容
    print("标题:", title)
    print("\n正文内容:", article_body)
    return
    # 获取当前文件的绝对路径
    current_file_path = os.path.abspath(__file__)

    # 获取当前文件所在的文件夹路径
    current_folder = os.path.dirname(current_file_path)

    filename = 'content.xlsx'

    absolute_path = os.path.join(current_folder, filename)

    # 创建DataFrame
    data = pd.DataFrame({'文章标题（不能重复）': [title], '文章内容': [article_body]})
#     data.dropna(axis=0, inplace=True)

    if not os.path.exists(absolute_path):
        data.to_excel(absolute_path, index=False, sheet_name='alizhizhuchi')
    else:

        with pd.ExcelFile(absolute_path) as xls:
            if 'alizhizhuchi' in xls.sheet_names:
                with pd.ExcelWriter(absolute_path, engine='openpyxl', mode='a', if_sheet_exists='overlay') as writer:
                    data.to_excel(writer, index=False, sheet_name='alizhizhuchi',
                                  startrow=writer.sheets['alizhizhuchi'].max_row, header=False)


for link in links:
    print(link)
    htmlContent = get_list_page(link)
    print(htmlContent)
    if htmlContent is not None:
        parseContentToExcel(htmlContent)
    else:
        continue
