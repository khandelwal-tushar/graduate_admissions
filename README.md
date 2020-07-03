# Graduate Admissons Predictor using STREAMLIT

### Deploying ML models in a web app is usually done through Flask, but **Streamlit** seems to be a bit faster and better than Flask.
### You can try out the web app [here](https://grad-adm.herokuapp.com/).

![Preview](https://i.ibb.co/L0qrTXr/Screenshot-300.png)

The main aim of this project was to try if streamlit is faster than flask in deploying models so that a ML enthusiast could focus more on development of the model rather than the web app.

The dataset for this project was taken from [kaggle](https://www.kaggle.com/mohansacharya/graduate-admissions) and the algorithm used here is the Random Forest Regressor. The model predicts the admission chances into a university taking in the parameters - 

* GRE Score (out of 340)
* TOEFL SCORE (out of 120)
* University Rating (out of 5 )
* Statement of Purpose and Letter of Recommendation Strength (out of 5 )
* Undergraduate GPA (out of 10 )
* Research Experience (either 0 or 1 )

and predicts the admission chances (ranging from 0 to 1).



