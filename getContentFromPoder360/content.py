import requests
from bs4 import BeautifulSoup
import pandas as pd
import os
from datetime import datetime,timedelta
import spinner
import requests
import re
from urls import urls, categoryNumber, category_number, payload
from date import month_mapping
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
    print(len(article_links))
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

def is_yesterday(time_text):
    # 假设time_text是ResultSet对象
    # 选择要处理的第一个元素
    first_time_element = time_text[0]  # 或者根据实际情况选择索引
    # 从选定的元素中提取文本
    time_text_str = first_time_element.text
    # 然后使用正则表达式搜索模式
    match = re.search(r'(\d+)\.(\w+)\.(\d+)', time_text_str)
    if match:
        # date_str = match.group(0)  # 提取匹配的日期字符串
        day = match.group(1)
        month = month_mapping.get(match.group(2))
        year = match.group(3)
        date_str = day+'.'+month+'.'+year
        # time_date = datetime.strptime(date_str, '%d.%b.%Y')     # 将日期字符串转换为日期对象
        yesterday = datetime.now() - timedelta(days=1)  # 获取昨天的日期
        yesterday_date = yesterday.date()  # 获取昨天日期的日期部分
        yesterday_date_str = yesterday_date.strftime('%#d.%b.%Y')
        return date_str == yesterday_date_str  # 比较日期部分是否相等

def check_excel_size(filepath):
    # 获取文件大小（以字节为单位）
    file_size = os.path.getsize(filepath)
    # 将字节转换为MB
    file_size_mb = file_size / (1024 * 1024)
    return file_size_mb<2

index=1
def parseContentToExcel(htmlContent, categoryNumber, category_number):

    # 使用BeautifulSoup解析HTML
    soup = BeautifulSoup(htmlContent, "html.parser")
    #提取新闻发布时间
    time_tags = soup.find_all("time", class_="inner-page-section__date")
    if not is_yesterday(time_tags):
        return
    # 提取标题
    title = soup.find("h1", class_="inner-page-section__title title-1")
    if title:
        title=title.text.strip()
        new_title = spinner.transform_text(title)
    else:
        print("未找到符合条件的标题标签")
        return
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
    new_article_body = spinner.transform_text(article_body)

    # 输出标题和正文内容
    print(category_number.get(categoryNumber), "标题:", new_title)
    print("\n", category_number.get(categoryNumber), "正文内容:", new_article_body)
   
    # 获取当前文件的绝对路径
    current_file_path = os.path.abspath(__file__)

    # 获取当前文件所在的文件夹路径
    current_folder = os.path.dirname(current_file_path)

    # filename = getDate() + " " + category_number.get(categoryNumber)+'.xlsx'
    filename = getDate() + " " + 'newsFrompoder360'+ str(index) +'.xlsx'

    absolute_path = os.path.join(current_folder, filename)

    # 创建DataFrame
    data = pd.DataFrame(
        {'文章标题（不能重复）': [new_title], '文章内容': [new_article_body]})
#     data.dropna(axis=0, inplace=True)
    if not os.path.exists(absolute_path):
        # if not check_excel_size(absolute_path):
        #     filename = getDate() + " " + 'newsFrompoder360'+ '_' + (index+1) +'.xlsx'
        data.to_excel(absolute_path, index=False, sheet_name='alizhizhuchi')
    else:
        with pd.ExcelFile(absolute_path) as xls:
            if 'alizhizhuchi' in xls.sheet_names:
                with pd.ExcelWriter(absolute_path, engine='openpyxl', mode='a', if_sheet_exists='overlay') as writer:
                    # if not check_excel_size(absolute_path):
                    #     filename = getDate() + " " + 'newsFrompoder360'+ '_' + (index+1) +'.xlsx'
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
