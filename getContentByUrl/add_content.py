import requests


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
    except Exception as e:
        print("请求失败：", e)
