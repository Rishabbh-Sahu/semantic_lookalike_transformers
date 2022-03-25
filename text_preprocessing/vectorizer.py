# -*- coding: utf-8 -*-
"""
@author: rishabbh-sahu
"""

class TRANSFORMER(object):

    def __init__(self,transformer_model_path,max_seq_length,transformer_model_name='bert-base-uncased'):
        """
        transformer_model_path: tensorflow-hub path, to download transformer based model like bert, albert etc.
        max_seq_length: int - maximum number of tokens to keep in a sequence
        """
        # Importing Bert model from Huggingface library. This space entails many pre-trained models.
        from transformers import BertTokenizerFast
        import tensorflow_hub as hub
        super(TRANSFORMER,self).__init__()
        self.max_seq_length = max_seq_length
        self.transformer_model_path = transformer_model_path
        self.fastTokenizer = BertTokenizerFast.from_pretrained(transformer_model_name)

        print(f'loading the model layer...')
        self.transformer = hub.KerasLayer(self.transformer_model_path, trainable=True, name='bert_layer')
        print(f'model - {self.transformer_model_path} successfully loaded..')

    def create_transformer_input(self,encodings):
        """create numpy array as the transformer input from the transformer's encoded object"""
        import numpy as np
        return {'input_word_ids': np.array(encodings.input_ids),
                'input_mask': np.array(encodings.attention_mask),
                'input_type_ids': np.array(encodings.token_type_ids),
                }

    def sentenceToVector(self,sentences):
        """
        Generate sentence vector using transformer's pooled output. This output is normally being 
        used further for sentence level classification tasks
        """
        encondings = self.fastTokenizer(sentences, is_split_into_words=True, max_length=self.max_seq_length, padding=True,
                                      return_offsets_mapping=True, truncation=True)
        sent_input_to_transformers = self.create_transformer_input(encondings)
        sent_to_vector = self.transformer(sent_input_to_transformers)['pooled_output'].numpy()
        return sent_to_vector
