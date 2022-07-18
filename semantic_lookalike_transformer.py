# -*- coding: utf-8 -*-
"""
Created on tuesday 17-June-2021
@author: rishabbh-sahu
"""

import numpy
import argparse  ## this will allow us to send the arguments to this script from the command line
from readers.reader import Reader
import random
from sklearn.metrics.pairwise import cosine_similarity
from text_preprocessing.vectorizer import TRANSFORMER
from text_preprocessing import preprocessing

# read command-line parameters
parser = argparse.ArgumentParser("Semantic similarity using sent2vec")
parser.add_argument('--config_file_path', '-c', help = 'Path to the config file', type = str, required = True)
args = parser.parse_args()

config = {}
config.update(Reader.read_yaml_from_file(args.config_file_path))

print("read data ...")
df = Reader.read_dataframes(config["data_path"])
df.columns = ["intent",'query']
print(f"Number of records: {df.shape[0]}")
print(f"Number of cols: {df.shape[1]} are {', '.join(df.columns)}")

sentences = df["query"].tolist()

# randomly select one sentence from the input data as targeted sentence
# We will try to find semantic look alike sentences for this targeted sentence
target_sentence_index = random.sample(range(0,len(sentences)),1)[0]
target_sentence = sentences[target_sentence_index:target_sentence_index+1]

# Instantiate transformer 
transformer = TRANSFORMER(transformer_model_path=config["model_path"],
                          max_seq_length=config["MAX_SEQ_LEN"],
                          transformer_model_name=config["model_name"])

sentences_as_words_list = preprocessing.text_to_word_list(sentences)
target_sentence_words_list = sentences_as_words_list[target_sentence_index:target_sentence_index+1]

target_sentence_vector = transformer.sentenceToVector(target_sentence_words_list)
sentences_vectors = transformer.sentenceToVector(sentences_as_words_list)

# Angular distance using consine similarity to identify similar sentences placed near by into n-dim space
cosine_similarities = cosine_similarity(target_sentence_vector,sentences_vectors).flatten()
most_similar_sent_indices = numpy.argsort(cosine_similarities, axis=0)[:-config["top_k_similar_sentences"]-1:-1]

print(f"Sentence to vector dimension : {len(target_sentence_vector[0])}")
print(f"Targeted sentence index : {target_sentence_index}")
print(f"Targeted sentence : {target_sentence}")
print(f"Top {config['top_k_similar_sentences']} semantic similar sentences are : ")
_ = [print(f"{i}:{sentences[idx]}",sep="\n") for i, idx in enumerate(most_similar_sent_indices)]
