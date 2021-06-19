# Semantic lookalike using Transformers
This repo enable us to find look alike sentences leveraging sent2vec concept.

#### How it works:
Most of the pre-trained language models learn a lot of common lanugage understanding that exists in the corpora. This way, sub-words embeddings would align themselves to learn semantics based on the given context in the sentence. An extension to this is to generate sentence vectors (build up from tokens of the sentence) aka sent2vec from the transformer's(BERT in this scenario) pooled output.
 
#### Getting started
- create virtual environment
- install requirements 
- Open config.yaml file and modify parameters as per your setup

#### For finding semantic look alike sentences
Run below cmd from the python terminal: <br> 
python semantic_lookalike_transformer.py --config_file_path=config.yaml 


#### Where to use:
- To find unique semantic patterns exist in the corpus 
- For labeling un-tagged data based on targeted sentence   

#### Output example (top 5 lookalike sentences based on semantic similarity): 
**Sentence to vector dimension : 128** <br> 
Targeted sentence index : 2841 <br>
Targeted sentence : [' i want to fly from boston to denver with a stop in philadelphia'] <br>
Top 5 semantic similar sentences are : <br>
0: i want to fly from boston to denver with a stop in philadelphia <br>
1: i want to fly from philadelphia to dallas and make a stopover in atlanta <br>
2: i want a flight originating in denver going to pittsburgh and atlanta in either order <br>
3: i want a flight on twa from boston to denver <br>
4: i need to go to san diego from toronto but i want to stopover in denver <br>

Note: This output will change based on the targeted sentence     

#### References:
Kinldy download the data from the below link - <br>
https://www.kaggle.com/hassanamin/atis-airlinetravelinformationsystem 
