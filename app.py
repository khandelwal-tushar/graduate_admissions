import numpy as np
import pickle
import pandas as pd
import streamlit as st 
from PIL import Image


pickle_in = open("graduate_admissions.pickle","rb")
model=pickle.load(pickle_in)

#@app.route('/')
def welcome():
    return "Welcome All"

#@app.route('/predict',methods=["Get"])
def calc_chances(gre_score, toefl_score, university_rating, sop, lor, cgpa, research):

    x = np.zeros(7)
    x[0] = gre_score
    x[1] = toefl_score
    x[2] = university_rating
    x[3] = sop
    x[4] = lor
    x[5] = cgpa
    x[6] = research
    chances = model.predict([x])[0]
    print(chances)
    return chances


def main():
    #st.title("Graduate Admissions Chances Predictor")
    html_temp ="""
    <html>
    <head></head>
    <body style="background-color:#A9A9A9">
    <div style="background-color:#6441a5;padding:8px">
    <h1 style="color:white;text-align:center;">Graduate Admissions Chances Predictor</h1>
    
    <div style="background-color:#4462b5;padding:4x">
    <h3 style="color:white;text-align:center;">Deployed using Streamlit!</h3>
    </div>
    </body>
    </html>
    """

    st.markdown(html_temp,unsafe_allow_html=True)
    gre_score = st.text_input("GRE SCORE (0-340)")
    toefl_score = st.text_input("TOEFL SCORE (0-120)")
    university_rating = st.slider("University Rating (0-5)",0,5)
    sop = st.number_input("Statement of Purpose (0-5)",0.0,5.0,step=0.1)
    lor = st.number_input("Letter of Recommendation strength (0-5)",0.0,5.0,step=0.1)
    cgpa = st.number_input("CGPA (0-10)",0.0,10.0)
    research = st.slider("RESEARCH (1-Yes, 0-No)",0,1)
    result=0
    if st.button("PREDICT"):
        result = calc_chances(gre_score, toefl_score, university_rating, sop, lor, cgpa, research)
        st.success(f"Your admission chance is : {round(result*100,2)}%.")
   
    if st.button("About"):
        st.text("tusharkhandelwal.work@gmail.com")
        st.text("Github:SinOfPride07")

if __name__=='__main__':
    main()
    