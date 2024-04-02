#计算文章的相似度
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


# 创建TF-IDF向量化器
vectorizer = TfidfVectorizer()


def getSimilarity(before_text, after_tetx):
    # 计算TF-IDF特征
    tfidf_matrix = vectorizer.fit_transform([before_text, after_tetx])

    # 计算余弦相似度
    cosine_sim = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:2])
    print("Cosine Similarity:", cosine_sim[0][0])
    return cosine_sim[0][0]
