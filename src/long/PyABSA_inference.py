import argparse
import os
from itertools import chain

import pandas as pd
from nltk import sent_tokenize
from pyabsa import ATEPCCheckpointManager
from tqdm import tqdm


def parser_args():

    # 현재 위치 확인
    cwd = os.getcwd()
    print("current location is :", cwd)

    parser = argparse.ArgumentParser()
    # input data PATH
    parser.add_argument("-i", "--input", default="./../../data/output_morphological.csv")

    return parser.parse_args()


def preprocessing_for_pyABSA(news):

    headlines = news['Headlines']
    articles = []

    for article in tqdm(headlines.values):
        line_list = Morphological(article)
        articles.append(line_list)
        # print(articles)

    return articles


def Morphological(articles):

    headlines = articles

    tokenized_as_line = sent_tokenize(headlines)
    # print(tokenized_as_line)

    return tokenized_as_line


def pyABSA(articles_list):
    aspect_extractor = ATEPCCheckpointManager.get_aspect_extractor(
        checkpoint='english',
        auto_device=True  # False means load model on CPU
    )

    # You can inference from a list of setences or a DatasetItem from PyABSA
    examples = articles_list
    inference_source = examples
    atepc_result = aspect_extractor.extract_aspect(
        inference_source=inference_source,
        pred_sentiment=True,  # Predict the sentiment of extracted aspect terms
    )

    return print(atepc_result)


# 함수들 호츌
if __name__ == "__main__":
    args = parser_args()
    news = pd.read_csv(args.input, encoding="utf-8")  # input 파일 읽기
    articles_list = preprocessing_for_pyABSA(news)
    articles_list = list(chain(*articles_list))

    # print(articles_list[:5])
    pyABSA(articles_list[:5])
