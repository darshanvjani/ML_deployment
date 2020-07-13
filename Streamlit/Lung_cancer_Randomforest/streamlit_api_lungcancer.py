import streamlit as st
import numpy as np
import pandas as pd 
import pickle 
import time
model = pickle.load(open('cancer_lr','rb'))

st.title("LUNG CANCER PREDICTION SYSTEM.")
st.text("")
st.text("")
st.text("Enter the variables:")

df = pd.read_excel("cancer_patient_data_sets.xlsx")

cols = ['Age', 'Gender', 'Air Pollution', 'Alcohol use',
       'Dust Allergy', 'OccuPational Hazards', 'Genetic Risk',
       'chronic Lung Disease', 'Balanced Diet', 'Obesity', 'Smoking',
       'Passive Smoker', 'Chest Pain', 'Coughing of Blood']

age = st.slider("Age",int(df.Age.min()),int(df.Age.max()),int(df.Age.mean()))

if st.selectbox("Gender",["M","F"]) == "M" :
    gender = 1
else:
    gender = 0

air_pollution = st.slider("air pollution",int(df['Air Pollution'].min()),int(df['Air Pollution'].max()),int(df['Air Pollution'].mean()))

alcohol_use = st.slider("alcohol use",int(df['Alcohol use'].min()),int(df['Alcohol use'].max()),int(df['Alcohol use'].mean()))

dust_allergy = st.slider("Dust Allergy",int(df['Dust Allergy'].min()),int(df['Dust Allergy'].max()),int(df['Dust Allergy'].mean()))

Occupation_hazards = st.text_input(label="Enter Occupation hazards")
    
genetic_risk = st.slider("genetic risk",int(df['Genetic Risk'].min()),int(df['Genetic Risk'].max()),int(df['Genetic Risk'].mean()))  

chronic = st.slider("chronic lung problem level",int(df['chronic Lung Disease'].min()),int(df['chronic Lung Disease'].max()),int(df['chronic Lung Disease'].mean())) 

diet = st.slider("balenced diet",int(df['Balanced Diet'].min()),int(df['Balanced Diet'].max()),int(df['Balanced Diet'].mean()))  

Obesity = st.slider("Obesity",int(df['Obesity'].min()),int(df['Obesity'].max()),int(df['Obesity'].mean()))  

Smoking = st.slider("Smoking",int(df['Smoking'].min()),int(df['Smoking'].max()),int(df['Smoking'].mean()))  

passive_smoker = st.slider("passive smoker",int(df['Passive Smoker'].min()),int(df['Passive Smoker'].max()),int(df['Passive Smoker'].mean()))  

chest_pain = st.slider("Chest Pain",int(df['Chest Pain'].min()),int(df['Chest Pain'].max()),int(df['Chest Pain'].mean()))  

cough_level = st.slider("Coughing of Blood",int(df['Coughing of Blood'].min()),int(df['Coughing of Blood'].max()),int(df['Coughing of Blood'].mean()))  

if st.button("Check the patient"):
    with st.spinner("loading...."):
        time.sleep(2)
    prediction = model.predict([[int(age),int(gender),int(air_pollution),int(alcohol_use),int(dust_allergy),int(Occupation_hazards),int(genetic_risk),int(chronic),int(diet),int(Obesity),int(Smoking),int(passive_smoker),int(chest_pain),int(cough_level)]])
    if prediction == 0:
        st.text("Patient has severe level of cancer")
    elif prediction ==1:
        st.text("Patient has moderate level of cancer")
    else:
        st.text("Patient has low level of cancer")
               
    