import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
# import pillow as pil

st.title('Welcome to Rohit WEB App')
st.header("python")
# st.subheader('Data Sets')
st.success('Data Sets')

# a = st.text_input('Name') 
df =pd.read_csv('practice2.csv')
st.dataframe(df)
# fig = plt.figure()
# plt.plot(df)
# st.pyplot(fig)

Name = st.text_input("Enter Your Name :")
Domain = st.selectbox("Enter Your Domain :",("AI With Python", "Full Stack Developer With Java"))
Project = st.text_input("Enter Your Project Name :")
Nsti = st.selectbox("Enter Your Nsti City :",(" Allahabad","Bengaluru","Bhubneshwar","Calicut","Dehradun","Howrah","Jodhpur","Kanpur","Kolkata","Noida","Mumbai","Noida","Patna","Ramanthapur","Trivandrum","Vidyanagar"))
Active_student = st.selectbox("Enter Active Student Number :",(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50))

# Name = "Name"
# Domain = "AI"
# Project = "Project"
# Nsti = "Nsti"
# Active_student = "number"

button = st.button("Submit")
if button:
    # Create a dictionary to hold the data
    data = {
        "Attribute": ["Name", "Domain", "Project", "Nsti", "Active_student"],
        "Value": [Name, Domain, Project, Nsti, Active_student]
    }

    # Convert the dictionary to a DataFrame
    df = pd.DataFrame(data)

    # Display the DataFrame as a table
    st.table(df)
 