from nltk.corpus import wordnet as wn
from nltk.tokenize import sent_tokenize, word_tokenize

from nltk.downloader import download
# import nltk
from nltk.corpus import stopwords

import random
# 下载葡萄牙语的语言包
# download('own')
# download('stopwords')


def get_primary_synonym(word):
    synonyms = []
    synsets = wn.synsets(word, lang='por')
    if synsets:
        for synset in synsets:
            for lemma in synset.lemmas('por'):
                synonyms.append(lemma.name())
                break  # 获取第一个同义词即可
    return synonyms


stop_words = set(stopwords.words('portuguese'))


def preprocess_text(text, isArticle):
    sentences = sent_tokenize(text, language='portuguese')  # 分句
    processed_sentences = []
    if isArticle:
        sentences = sentences[:-1]  # 如果是最后一句话，则移除最后一句

    for sentence in sentences:
        if "whatsapp" in sentence.lower():
            continue  # 如果句子中包含"whatsapp"，则跳过这句话
        words = word_tokenize(sentence, language='portuguese')  # 分词
        new_words = []
        for word in words:
            if word.lower() in stop_words:
                new_words.append(word)
                continue
            synonyms = get_primary_synonym(word)
            if synonyms:
                new_word = random.choice(synonyms)  # 随机选择一个同义词
                new_words.append(new_word)
            else:
                new_words.append(word)
        processed_sentence = ' '.join(new_words)
        processed_sentences.append(processed_sentence)
    processed_text = ' '.join(processed_sentences)
    return processed_text

# 对文本进行词汇替换和句子重组
# ValueError: empty vocabulary; perhaps the documents only contain stop words


def transform_text(text, isArticle):
    transformed_text = preprocess_text(text, isArticle)
    # rate = similiarRate.getSimilarity(text, transformed_text)
    return transformed_text
