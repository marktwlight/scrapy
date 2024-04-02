Urls = {
    '9': 'https://www.poder360.com.br/wordpress/wp-admin/admin-ajax.php'#category  governo<==>9
}
Page = '1'
categoryNumber = 9
category_number = {
    "9": "category"
}
payload = {
        'action': 'leia_mais_posts_categoria_especial',
        'paged': Page,   #页码，表示第几页
        'category': categoryNumber,    #分类
        # 其他键值对...
    }
# 定义payload参数
# paged = [1,2,3,4,5,6,7,8,9,10]
# category = [1,2,3,4,5,6,7,8,9,10]
# i=0
# payloadList = []
# for value in paged:
#     payload = {
#         'action': 'leia_mais_posts_categoria_especial',
#         'paged': paged[i],   #页码，表示第几页
#         'category': '9',    #分类
#         # 其他键值对...
#     }
#     payloadList.append(payload)
#     i+=1
# page = list(payloadList[5].values())[1]
# print("\n",page)