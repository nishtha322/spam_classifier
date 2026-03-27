import streamlit as st
import pickle
import string
import nltk


nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('stopwords')

def transform_text(text):
    text = text.lower()
    text = nltk.word_tokenize(text)

    y = []
    for i in text:
        if i.isalnum():
            y.append(i)

    text = y[:]
    y.clear()

    for i in text:
        if i not in nltk.corpus.stopwords.words('english') and i not in string.punctuation:
            y.append(i)

    text = y[:]
    y.clear()

    for i in text:
        y.append(nltk.stem.PorterStemmer().stem(i))

    return " ".join(y)
tfidf=pickle.load(open('vectorizer.pkl','rb'))
model=pickle.load(open('model.pkl','rb'))
st.title('Spam Classifier')
input_sms=st.text_area('Enter the message')
if st.button('Predict'):
 #1. preprocess
       transformed_sms=transform_text(input_sms)
#2. vectorize
       vectorized_sms=tfidf.transform([transformed_sms])
#3. predict
       result=model.predict(vectorized_sms)[0]
#4. display
       if result == 1:
             st.header("Spam")
       else:
             st.header("Not Spam")
