import requests
from bs4 import BeautifulSoup
import pandas as pd
import os
from datetime import datetime
import spinner
import requests
import re
from urls import urls, categoryNumber, category_number, payload
# 获取文章链接列表,网络请求超时处理


def get_article_links(url_pattern, start_page, end_page, payload, categoryNumber):
    article_links = []
    payload["category"] = categoryNumber
    for i in range(start_page, end_page + 1):
        payload["paged"] = i

        try:
            response = requests.post(url_pattern, data=payload, timeout=30)
            if response.ok and 'text/html' in response.headers.get('content-type', ''):
                soup = BeautifulSoup(response.content, 'html.parser')

                items = soup.find_all('h3', class_='box-queue__subhead')

                for item in items:
                    links = item.find_all('a')  # 找到分页中的a链接
                    for link in links:
                        article_links.append(link['href'])  # 将链接直接添加到列表中
            else:
                print(f"Failed to fetch data from {url_pattern}")
        except requests.Timeout:
            continue
        except requests.RequestException as e:
            continue
        except Exception as e:
            continue

    return article_links


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


def parseContentToExcel(htmlContent, category, category_number):
    # 使用BeautifulSoup解析HTML
    soup = BeautifulSoup(htmlContent, "html.parser")
    # 提取标题
    title = soup.find(
        "h1", class_="inner-page-section__title title-1").text.strip()

    new_title = spinner.transform_text(title, False)
    # 标题相似度
    # title_rate = similiarRate.getSimilarity(title,new_title)
    # 判断相似值，
    article_body = ""
    # 提取正文内容
    # paragraphs = soup.find_all("p", class_="content-text__container")
    # paragraphs = soup.find_all("p")
    paragraphs = soup.find_all("p")
    for paragraph in paragraphs:
        # 忽略所有子元素，只获取纯文本内容
        text = paragraph.text.strip()
        article_body += text

    # 调用伪原创方法
    # git
    new_article_body = spinner.transform_text(article_body, True)

    # 输出标题和正文内容
    print(category, "标题:", new_title)
    print("\n", category, "正文内容:", new_article_body)
    # 获取当前文件的绝对路径
    current_file_path = os.path.abspath(__file__)

    # 获取当前文件所在的文件夹路径
    current_folder = os.path.dirname(current_file_path)

    filename = getDate() + " " + category_number.get(categoryNumber)+'.xlsx'

    absolute_path = os.path.join(current_folder, filename)

    # 创建DataFrame
    data = pd.DataFrame(
        {'文章标题（不能重复）': [new_title], '文章内容': [new_article_body]})
#     data.dropna(axis=0, inplace=True)

    if not os.path.exists(absolute_path):
        data.to_excel(absolute_path, index=False, sheet_name='alizhizhuchi')
    else:

        with pd.ExcelFile(absolute_path) as xls:
            if 'alizhizhuchi' in xls.sheet_names:
                with pd.ExcelWriter(absolute_path, engine='openpyxl', mode='a', if_sheet_exists='overlay') as writer:
                    data.to_excel(writer, index=False, sheet_name='alizhizhuchi',
                                  startrow=writer.sheets['alizhizhuchi'].max_row, header=False)


start_page = 1
end_page = 5  # 设置结束页码


def getHtmlContent(Urls):
    # 遍历所有的新闻种类
    for category, url in Urls.items():

        # 只有五条
        categoryNumber = category
        article_links = get_article_links(
            url, start_page, end_page, payload, categoryNumber)
        print(article_links)
        for link in article_links:

            htmlContent = get_list_page(link)
            if htmlContent is not None:
                parseContentToExcel(
                    htmlContent, categoryNumber, category_number)
            else:
                continue
