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
    st.title("GRADUATE ADMISSION CHANCES PREDICTOR")
    html_temp = """
    <div style="background-color:tomato;padding:10px">
    <h2 style="color:white;text-align:center;">A Demonstration Of Streamlit Web App </h2>
    </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)
    gre_score = st.text_input("GRE SCORE","Type Here")
    toefl_score = st.text_input("TOEFL SCORE","Type Here")
    university_rating = st.text_input("UNIVERSITY RATING","Type Here")
    sop = st.text_input("SOP","Type Here")
    lor = st.text_input("LOR","Type Here")
    cgpa = st.text_input("CGPA","Type Here")
    research = st.text_input("RESEARCH","Type Here")
    result=""
    if st.button("Predict"):
        result = calc_chances(gre_score, toefl_score, university_rating, sop, lor, cgpa, research)
    st.success('The output is {}'.format(result))
    if st.button("About"):
        st.text("Lets LEarn")
        st.text("Built with Streamlit")

if __name__=='__main__':
    main()
    