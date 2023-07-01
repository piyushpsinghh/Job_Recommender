import streamlit as st
import pickle
import pandas as pd
import numpy as np
import nltk
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
pc=PorterStemmer()
# import the model

#model 1
model_1 = pickle.load(open('ml-model\model_1.pkl','rb'))
cv_1 = pickle.load(open('ml-model\\vectorizer_1.pkl', 'rb'))

#model 2
model_2 = pickle.load(open('ml-model\model_2.pkl', 'rb'))
cv_2 = pickle.load(open('ml-model\\vectorizer_2.pkl', 'rb'))

#model 3
model_3 = pickle.load(open('ml-model\model_3.pkl', 'rb'))
cv_3 = pickle.load(open('ml-model\\vectorizer_3.pkl', 'rb'))

# skill processing
def transfrom_text(x):
    y = nltk.word_tokenize(x.lower())
    z = []
    for i in y:
        if i.isalnum():
            z.append(i)
    y = z[:]
    z.clear()
    for i in y:
        if i not in stopwords.words('english'):
            z.append(i)
    y=z[:]
    z.clear()
    for i in y:
        z.append(pc.stem(i))
    return ' '.join(z)


#  funcion
def pred_1(x):
    pred = model_1.predict(cv_1.transform([transfrom_text(x)]))
    if pred==1:
        return "Fresher"
    elif pred==2:
        return "Junior"
    elif pred==3:
        return "Senior"
    elif pred==4:
        return "Lead"
    elif pred==5:
        return "Specialist"
    else:
        return "Other"

def pred_2(x):
    pred = model_2.predict(cv_2.transform([transfrom_text(x)]))
    if pred == 1:
        return "Software Engineering"
    elif pred == 2:
        return "Sales and Business"
    elif pred == 3:
        return "Marketing"
    elif pred == 4:
        return "Technical Management"
    elif pred == 5:
        return "Specialist"
    elif pred == 6:
        return "Operations"
    elif pred == 7:
        return "Design and Creative"
    elif pred == 8:
        return "Human Resources"
    elif pred == 9:
        return "Specialist"
    else:
        return "other"


def pred_3(jk):
    pred = model_3.predict(cv_3.transform([transfrom_text(jk)]))
    if pred == 1:
        return "Class 1"
    elif pred==2:
        return "Class 2"
    elif pred==3:
        return "Class 3"
    else:
        return "Class 4"


# predict no of jobs

def job_no(x):
    y=x.lower()
    ls=y.split(',')
    job_list=[]
    for i in ls:
        job=df[df.transfrom_skill.str.contains(i)].shape[0]
        job_list.append(job)

    return min(job_list)


df=pd.read_csv('dataset\\final_table.csv')
data = st.checkbox('click to see data')
df['transfrom_skill']=df.skills.map(transfrom_text)
if data:
    st.write(df)

df["skills"] = df["skills"].str.lower()
v=("*").join(df["skills"])
v=("*").join(df["skills"])
v=v.replace("*",",")
skill_list = v.split(",")

skill_dict=dict()
for i in set(skill_list):
    skill_dict[i] = skill_list.count(i)


st.title("Job Recommender")
skill = st.text_input("Enter the Skill/Skills")

if st.button('Search'):
    st.markdown(
        f"<h3 style='color: White;'>Most common Experience Level  : <span style='color : Red;'>{pred_1(transfrom_text(skill))} </span> </h3>",
        unsafe_allow_html=True)
    st.markdown(f"<h3 style='color: White;'>Most common Department  :  <span style='color : Red;'>{pred_2(transfrom_text(skill))} </span> </h3>", unsafe_allow_html=True)

    st.markdown(
        f"<h3 style='color: White;'>Most common Company class  :   <span style='color : Red;'>{pred_3(transfrom_text(skill))} </span> </h3>",
        unsafe_allow_html=True)

    st.markdown(
        f"<h3 style='color: White;'>Most Total Number of Jobs Available:   <span style='color : Red;'>{job_no(skill)} </span> </h3>",
        unsafe_allow_html=True)
