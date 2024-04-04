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


def preprocess_text(text):
    sentences = sent_tokenize(text, language='portuguese')  # 分句
    processed_sentences = []

    for sentence in sentences:
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


def transform_text(text):
    transformed_text = preprocess_text(text)
    return transformed_text
