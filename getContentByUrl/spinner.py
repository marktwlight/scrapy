from nltk.corpus import wordnet as wn
from nltk.tokenize import sent_tokenize, word_tokenize

from nltk.downloader import download
import nltk

import similiarRate
import random
# 下载葡萄牙语的语言包
# download('own')


def get_primary_synonym(word):
    synonyms = []
    for synset in wn.synsets(word, lang='por'):

        for lemma in synset.lemmas('por'):

            synonyms.append(lemma.name())

            break  # 获取第一个同义词即可
    return synonyms


def preprocess_text(text,isLast):
    sentences = sent_tokenize(text, language='portuguese')  # 分句
    processed_sentences = []
    for i, sentence in enumerate(sentences):
        if isLast:   # 不处理标题
            if i == len(sentences) - 1:  # 如果是最后一句话，则跳过
               continue
              
        words = word_tokenize(sentence, language='portuguese')  # 分词
        new_words = []
        for word in words:
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


def transform_text(text,isLast):
    transformed_text = preprocess_text(text,isLast)
    rate = similiarRate.getSimilarity(text, transformed_text)
    return transformed_text
