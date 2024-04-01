import requests
from bs4 import BeautifulSoup, NavigableString
import pandas as pd
import openpyxl
import os
import getUrl
from datetime import datetime
import spinner
import similiarRate
print("================================", len(getUrl.article_links))
# 获取列表页 HTML 内容
links = getUrl.article_links


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


def getDate():
    # 获取当前日期
    current_date = datetime.now()

    # 格式化日期为 YYYY-MM-DD 样式
    formatted_date = current_date.strftime('%Y-%m-%d')

    return formatted_date


def parseContentToExcel(htmlContent):
    # 使用BeautifulSoup解析HTML
    soup = BeautifulSoup(htmlContent, "html.parser")
    # 提取标题
    title = soup.find("h1", class_="post__title").text.strip()
    
    new_title = spinner.transform_text(title,False)
    # 标题相似度
    # title_rate = similiarRate.getSimilarity(title,new_title)
    #判断相似值，
    article_body = ""
    # 提取正文内容
    # paragraphs = soup.find_all("p")
    # paragraphs = soup.select('p',class_='post_content')
    # for paragraph in paragraphs:
    #     # 忽略所有子元素，只获取纯文本内容
    #     text = paragraph.text.strip()
    #     article_body += text
    # # 查找所有类名为 "post_content" 的 div 元素
    post_content_divs = soup.find_all("div", class_="post__content")

    # 遍历每个找到的 div 元素
    for post_content_div in post_content_divs:
        if type(post_content_div) is not NavigableString:
            # 在每个 div 元素中查找 p 标签
            paragraphs = post_content_div.find_all("p")
            # 遍历每个找到的 p 标签
            for paragraph in paragraphs:
                # 处理每个 p 标签,检查paragraph是否为空
                if paragraph:
                    text = paragraph.text.strip()
                    article_body += text
    # 调用伪原创方法
    print("\n正文内容:", article_body)
    new_article_body = spinner.transform_text(article_body,True)
    
    # 输出标题和正文内容
    print("标题:", new_title)
    print("\n伪原创正文内容:", new_article_body)
    # 获取当前文件的绝对路径
    current_file_path = os.path.abspath(__file__)

    # 获取当前文件所在的文件夹路径
    current_folder = os.path.dirname(current_file_path)

    filename = getDate() +" " + getUrl.news_category+'.xlsx'

    absolute_path = os.path.join(current_folder, filename)

    # 创建DataFrame
    data = pd.DataFrame({'文章标题（不能重复）': [new_title], '文章内容': [new_article_body]})
#     data.dropna(axis=0, inplace=True)

    if not os.path.exists(absolute_path):
        data.to_excel(absolute_path, index=False, sheet_name='alizhizhuchi')
    else:

        with pd.ExcelFile(absolute_path) as xls:
            if 'alizhizhuchi' in xls.sheet_names:
                with pd.ExcelWriter(absolute_path, engine='openpyxl', mode='a', if_sheet_exists='replace') as writer:
                    existing_data = pd.read_excel(absolute_path)
                    updated_data = pd.concat([existing_data, data], ignore_index=True)
                    updated_data.to_excel(writer, index=False, sheet_name='alizhizhuchi')
            else:
                data.to_excel(absolute_path, index=False, sheet_name='alizhizhuchi')


for link in links:
    print(link)
    htmlContent = get_list_page(link)
    if htmlContent is not None:
        parseContentToExcel(htmlContent)
    else:
        continue
