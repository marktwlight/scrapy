urls = {
    '9'     : 'https://www.poder360.com.br/wordpress/wp-admin/admin-ajax.php',# category<==>number
    '10'    : 'https://www.poder360.com.br/wordpress/wp-admin/admin-ajax.php',
    '11'    : 'https://www.poder360.com.br/wordpress/wp-admin/admin-ajax.php',
    '13'    : 'https://www.poder360.com.br/wordpress/wp-admin/admin-ajax.php',
    '14'    : 'https://www.poder360.com.br/wordpress/wp-admin/admin-ajax.php',
    '15'    : 'https://www.poder360.com.br/wordpress/wp-admin/admin-ajax.php',
    '157619': 'https://www.poder360.com.br/wordpress/wp-admin/admin-ajax.php',
    '150786': 'https://www.poder360.com.br/wordpress/wp-admin/admin-ajax.php',
    '48035' : 'https://www.poder360.com.br/wordpress/wp-admin/admin-ajax.php',
    '13340' : 'https://www.poder360.com.br/wordpress/wp-admin/admin-ajax.php',
    '1113'  : 'https://www.poder360.com.br/wordpress/wp-admin/admin-ajax.php',
    '692'   : 'https://www.poder360.com.br/wordpress/wp-admin/admin-ajax.php',
    '4907'  : 'https://www.poder360.com.br/wordpress/wp-admin/admin-ajax.php',
}

Page = '1'
categoryNumber = 9

category_number = {
    "9"     : "governo",                #政府
    "157619": "anuncios-do-governo" ,   #政府公告
    "10"    : "congresso",              #国会
    "13"    : "economia",               #经济
    "11"    : "justica",                #正义
    "150786": "infraestrutura",         #基础设施
    "48035" : "poderdata",              #poder数据
    "13340" : "infograficos",           #信息图表
    "14"    : "eleicoes",               #选举
    "1113"  : "internacional",          #国际的
    "13062" : "tecnologia",             #技术
    "15"    : "midia",                  #媒体
    "692"   : "pesquisas",              #研究
    "4907"  : "nieman",                 #nieman
}

#POST请求参数
payload = {
    'action'    : 'leia_mais_posts_categoria_especial',
    'paged'     : Page,  # 页码，表示第几页
    'category'  : categoryNumber,  # 分类数字
    # 其他键值对...
}
