urls = {
    # category  governo<==>9
    '9': 'https://www.poder360.com.br/wordpress/wp-admin/admin-ajax.php'
}
Page = '1'
categoryNumber = 9
category_number = {
    "9": "category"
}
payload = {
    'action': 'leia_mais_posts_categoria_especial',
    'paged': Page,  # 页码，表示第几页
    'category': categoryNumber,  # 分类
    # 其他键值对...
}
