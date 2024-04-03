import pandas as pd
import spinner
from datetime import datetime
import os


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
        # 输出标题和正文内容
        print("标题:", new_title)
        print("\n正文内容:", new_article_body)
        # 获取当前文件的绝对路径
        current_file_path = os.path.abspath(__file__)
        # 获取当前文件所在的文件夹路径
        current_folder = os.path.dirname(current_file_path)
        filename = getDate() + '.xlsx'
        absolute_path = os.path.join(current_folder, filename)
        # 创建DataFrame
        data = pd.DataFrame(
            {'文章标题（不能重复）': [new_title], '文章内容': [new_article_body]})
    #     data.dropna(axis=0, inplace=True)

        if not os.path.exists(absolute_path):
            data.to_excel(absolute_path, index=False,
                          sheet_name='alizhizhuchi')
        else:

            with pd.ExcelFile(absolute_path) as xls:
                if 'alizhizhuchi' in xls.sheet_names:
                    with pd.ExcelWriter(absolute_path, engine='openpyxl', mode='a', if_sheet_exists='overlay') as writer:
                        data.to_excel(writer, index=False, sheet_name='alizhizhuchi',
                                      startrow=writer.sheets['alizhizhuchi'].max_row, header=False)
