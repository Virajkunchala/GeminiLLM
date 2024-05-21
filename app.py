from dotenv import load_dotenv
load_dotenv() 

import streamlit as st
import os
import PIL
from PIL import Image
import google.generativeai as genai

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
multi_model=genai.GenerativeModel('gemini-pro-vision')
text_model=genai.GenerativeModel("gemini-pro")

##Calling Gemini API
def text_model_gemini_response(input):
    response=text_model.generate_content(input)
    return response.text

def multi_model_gemini_response(prompt,image):
    response=multi_model.generate_content([prompt,image])
    return response.text

st.header("OCR Extractor Key-Value pairs")
input=st.text_input("Input Prompt: ",key="input")
file=st.file_uploader("Choose an image",type=["jpg","jpeg","png"])

submit=st.button("Give the info")


if file is not None:
    img=PIL.Image.open(file)
    st.image(img,caption="uploaded image")
    

if submit:
    if file is None:
        response=text_model_gemini_response(input)
        st.subheader("The response is:")
        st.write(response)
    else:
        img=PIL.Image.open(file)
        response=multi_model_gemini_response(input,img)
        st.subheader("The response is:")
        st.write(response)
        
