import pandas as pd
import spinner
from datetime import datetime
import os
import add_content


def getDate():
    # 获取当前日期
    current_date = datetime.now()

    # 格式化日期为 YYYY-MM-DD 样式
    formatted_date = current_date.strftime('%Y-%m-%d')

    return formatted_date


def parseContentToExcel(title, article):

    new_title = spinner.transform_text(title)
    new_article_body = spinner.transform_text(article)
    if len(new_article_body.split('.')) > 2:
        add_content.add_content(new_title, new_article_body)
