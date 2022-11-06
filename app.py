import streamlit as st
import joblib

model=joblib.load('spam-ham') #we are loading the pipelined model using joblib
st.title('SPAM-HAM CLASSIFIER') #it creates a title in webapp
ip=st.text_input('Enter the message') #it create a text box in thw webapp
op=model.predict([ip])
if st.button('predict'):
  st.title(op[0]) #st.button will create a button with the name predict
  #st.title(op[0]) #the zeroth element in op variable is displayed as a title

  
  
  
  
