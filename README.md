# Semantic lookalike using Transformers
This repo enable us to find look-alike(closest) sentences leveraging sent2vec concept.

#### How it works
Most of the pre-trained language models learn a lot of common lanugage understanding that exists in the corpora. This way, sub-words embeddings would align themselves to learn semantics based on the given context in the sentence. An extension to this is to generate sentence vectors (build up from tokens of the sentence) aka sent2vec from the transformer's(BERT in this scenario) as a numeric representation of this semantic relationship. Now, given two vectors, we can find the similarity using cosine similarity. 
 
#### Getting started
- create virtual environment
- install requirements 
- Open config.yaml file and modify parameters as per your setup

#### Getting semantic look alike sentences
Run below cmd from the python terminal: <br> 
python semantic_lookalike_transformer.py --config_file_path=config.yaml 

#### Semantic similarity vs. tf-idf text vectorization
1. Best representation of a sentence based on the context and words relationship which can not be achieved using tf-idf (does not consider word orders for example)
2. Tf-idf might not be able to generate a proper vector if the sentence have way too many out of vacob words while transformers outperformed most of the text vectorization on this aspect.
3. Sentences (search space) need not to have same words to be identified as lookalike ones to the targeted sentence.  

#### Where to use
- To find unique semantic patterns exist in the corpus 
- For labeling un-tagged data based on targeted sentence   
- To find similar documents or articles

#### Output example (top 5 lookalike sentences based on semantic similarity)
**Sentence to vector dimension : 128** (Try to increase this dims by trying different BERT configuration, to get even better results for longer sentences)<br> 
Targeted sentence index : 2841 (A random index) <br>
**Targeted sentence :** [*'i want to fly from boston to denver with a stop in philadelphia'*] <br>
**Top 5 semantic similar sentences are :** <br>
0 : i want to fly from boston to denver with a stop in philadelphia <br>
1 : i want to fly from philadelphia to dallas and make a stopover in atlanta <br>
2 : i want a flight originating in denver going to pittsburgh and atlanta in either order <br>
3 : i want a flight on twa from boston to denver <br>
4 : i need to go to san diego from toronto but i want to stopover in denver<br>

Note: This output will vary based on the targeted sentence     

#### Further improvement
- Increase the dimension of transformer embedding layer (currently 128) to learn more language representation hence more close/better look alike sentences. Kindly try 256, 512 or 768 embedding dims in order to increase the overall performance. 
- flairNLP also provide some good ways to create sentence/document level embeddings.

#### Reference
Kinldy download the data from the below link - <br>
https://www.kaggle.com/hassanamin/atis-airlinetravelinformationsystem 
