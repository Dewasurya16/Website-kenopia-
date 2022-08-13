import pickle
import tensorflow as tf
from transformers import TFBertForSequenceClassification
import pandas as pd
import os

bert_tokenizer = pickle.load(open('model/bert_tokenizer.pkl', 'rb')) # Load tokenizer
PRE_TRAINED_MODEL = 'indobenchmark/indobert-base-p2'  # Pre-trained model
bert_load_model = TFBertForSequenceClassification.from_pretrained(PRE_TRAINED_MODEL, num_labels=5) # Load model
bert_load_model.load_weights('model/bert-model.h5') # Load model weight
quotes = pd.read_csv("Quotes.csv") # Load data



def predict1(input): # Fungsi prediksi
    # Prediksi query user termasuk emosi apa
    emosi_labels = ['Senang\U0001F604','Cinta\U0001F970','Marah\U0001F621','Takut\U0001F628','Sedih\U0001F625']
    input_text = input
    input_text_tokenized = bert_tokenizer.encode(input_text,
                                             truncation=True,
                                             padding='max_length',
                                             return_tensors='tf')

    bert_predict = bert_load_model(input_text_tokenized)          # Lakukan prediksi
    bert_output = tf.nn.softmax(bert_predict[0], axis=-1) # Softmax
    

    label = tf.argmax(bert_output, axis=1) # Ambil label
    label = label.numpy() # Ambil label

    return emosi_labels[label[0]]  # Kembalikan label
    
    