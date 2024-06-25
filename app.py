import streamlit as st
import joblib

model= joblib.load("sentiment-model.pkl")

sentiment_labels= {'1': 'positive','0':'negative'}

st.title("Sentiment Analysis")

user_input= st.text_area("enter your text here:")

if st.button("predict"):
    print(user_input)
    predicted_sentiment = model.predict([user_input])[0]
    print("predicted_label:"+ str(predicted_sentiment))
    predicted_sentiment_label = sentiment_labels[str(predicted_sentiment)]
    
    st.info(f"predicted sentiment : {predicted_sentiment_label}")
    