# 定义基本的 URL 和查询参数
urls = {
    "politica": "https://www.cnnbrasil.com.br/cnn-brasil-block-list-ajax",#政治
    "nacional": "https://www.cnnbrasil.com.br/cnn-brasil-block-list-ajax",#国家
    # "economia_negocios": "https://www.cnnbrasil.com.br/cnn-brasil-block-list-ajax",#经济商业
    # "economia_macroeconomia": "https://www.cnnbrasil.com.br/cnn-brasil-block-list-ajax",#宏观经济
    "internacional": "https://www.cnnbrasil.com.br/cnn-brasil-block-list-ajax",#国际
    "pop": "https://www.cnnbrasil.com.br/cnn-brasil-block-list-ajax",#娱乐
    "saude": "https://www.cnnbrasil.com.br/cnn-brasil-block-list-ajax",#健康
    "esportes_futebol": "https://www.cnnbrasil.com.br/cnn-brasil-block-list-ajax",#运动足球
    "tecnologia": "https://www.cnnbrasil.com.br/cnn-brasil-block-list-ajax",#技术
    "lifestyle": "https://www.cnnbrasil.com.br/cnn-brasil-block-list-ajax",#生活方式
    "viagemegastronomia": "https://www.cnnbrasil.com.br/cnn-brasil-block-list-ajax",#旅游与美食
    }
params = {
    "action": "cnnbrasilBlockListAjax",
    "nounce": "f06c6758c5",  # 这是一个用于防止 CSRF 攻击的安全标记（nonce），需每天更新
    "page": 1,
    "perpage": 5,   #请求新闻数量
    "limit": 10,    #返回新闻数量限制
    "items": 482,
    "type": "category",
    "postin": "[6877062,6876790,6876180,6876115,6873040,6874717,6872932,6873198,6873133,6832664]",  # 区分新闻栏目的参数，每天需更改
    "url": "BlockList"
}