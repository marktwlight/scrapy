#计算文章的相似度
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


# # 创建TF-IDF向量化器
# vectorizer = TfidfVectorizer()


# def getSimilarity(before_text, after_tetx):
#     # 计算TF-IDF特征
#     try:
#         tfidf_matrix = vectorizer.fit_transform([before_text, after_text])
#     except Exception as e:
#         print(f"An error occurred while fitting TF-IDF vectorizer: {e}")
#         # 进行异常处理，例如提供默认值或者记录日志
#         tfidf_matrix = None  # 为了演示，这里简单地将 tfidf_matrix 设为 None

#     # 计算余弦相似度
#     cosine_sim = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:2])
#     print("Cosine Similarity:", cosine_sim[0][0])
#     return cosine_sim[0][0]
def getSimilarity(before_text, after_text):
    try:
        # 创建TF-IDF向量化器
        vectorizer = TfidfVectorizer()
        
        # 计算TF-IDF特征
        tfidf_matrix = vectorizer.fit_transform([before_text, after_text])

        # 计算余弦相似度
        cosine_sim = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:2])
        print("Cosine Similarity:", cosine_sim[0][0])
        return cosine_sim[0][0]
    except Exception as e:
        print(f"An error occurred while calculating similarity: {e}")
        # 在出现异常时返回一个默认的相似度值，例如 0
        return 0