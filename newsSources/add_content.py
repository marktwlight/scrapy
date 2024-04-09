import requests
import spinner
from translateArticle import translate_text


def add_content(title, content):
    # 请求 URL
    url = "http://yzh76.fymkz.cn/admin/inc/api.php?c=info_add&t=c_title&object_id=1"

    # 请求头，包含 cookie
    headers = {
        "Cookie": "PHPSESSID=f8aeu1c14109g9u8cob8n7ct49; _ga=GA1.1.2055165949.1711784019; _ga_0SYLZG66HW=GS1.1.1712204747.10.1.1712206218.49.0.0"
    }
    try:
        # 发起 POST 请求
        response = requests.post(url, headers=headers, data={
            "title": title,
            "content": content
        })

        # 判断响应内容是否为 "ok"
        if response.text.strip() == "ok":
            print("内容添加成功！")
        else:
            print("内容添加失败！")
            print("响应内容：", response.text)
            return
    except Exception as e:
        print("请求失败：", e)


def transform_content(title, article):
    title = translate_text(title)
    article = translate_text(article)

    if len(article.split('.')) > 2:
        # 输出标题和正文内容
        print("标题:", title)
        print("\n正文内容:", article)
        try:
            add_content(title, article)
        except Exception as e:
            print("上传内容发生异常：", e)
            return
