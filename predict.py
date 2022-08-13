import pickle
import tensorflow as tf
from transformers import TFBertForSequenceClassification
import pandas as pd
import os

bert_tokenizer = pickle.load(open('model/bert_tokenizer.pkl', 'rb'))
PRE_TRAINED_MODEL = 'indobenchmark/indobert-base-p2' 
bert_load_model = TFBertForSequenceClassification.from_pretrained(PRE_TRAINED_MODEL, num_labels=5)
bert_load_model.load_weights('model/bert-model.h5')
quotes = pd.read_csv("Quotes.csv")

def search_quotes(label): # Mencari quotes sesuai dengan emosi user

    quotes_list = []
    if ((label== 0) or (label==1)):
        quotes_choice = quotes[quotes.label == 6].sample(1)
        quotes_list.append(quotes_choice.iloc[0].teks)
    elif ((label== 2)):
        quotes_choice = quotes[quotes.label == 8].sample(1)
        quotes_list.append(quotes_choice.iloc[0].teks)
    elif ((label== 3)):
        quotes_choice = quotes[quotes.label == 7].sample(1)
        quotes_list.append(quotes_choice.iloc[0].teks)
    elif ((label== 4)):
        quotes_choice = quotes[quotes.label == 8].sample(1)
        quotes_choice_2 = quotes[quotes.label == 7].sample(1)
        quotes_list.append(quotes_choice.iloc[0].teks)
        quotes_list.append(quotes_choice_2.iloc[0].teks)
    
    return quotes_list


def predict(input): # Fungsi prediksi
    # Prediksi query user termasuk emosi apa
    emosi_labels = ['senang','cinta','marah','takut','sedih']
    input_text = input
    input_text_tokenized = bert_tokenizer.encode(input_text,
                                             truncation=True,
                                             padding='max_length',
                                             return_tensors='tf')

    bert_predict = bert_load_model(input_text_tokenized)          # Lakukan prediksi
    bert_output = tf.nn.softmax(bert_predict[0], axis=-1)
    

    label = tf.argmax(bert_output, axis=1) # Ambil label
    label = label.numpy()

    # Mencari quotes sesauai dengan emosi user
    quotes_list = search_quotes(label[0]) # Kembalikan label
    response = ""
    for teks in quotes_list: # Menampilkan quotes
        response = response + " " + teks
    prediction = response


    return quotes_list[0] # Kembalikan label 