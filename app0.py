
##BackEnd
from dotenv import load_dotenv
load_dotenv()

import streamlit as st
import os
import sqlite3

import google.generativeai as genai

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

#Prompt to Sql

def get_gemini_response(question,prompt):
    model=genai.GenerativeModel('gemini-1.5-flash')
    response = model.generate_content([prompt[0],question])
    return response.text

#sql to Db

def read_sql_query(sql,db):
    con=sqlite3.connect(db)
    cur=con.cursor()
    cur.execute(sql)
    rows=cur.fetchall()
    con.commit()
    
    for row in rows :
        print(row)
    return rows
    
    

prompt=[
       """
    You are an expert in converting English questions to SQL query!
    The SQL database has the name STUDENT and has the following columns - NAME, CLASS, 
    SECTION.

    Important: 
    1. Do NOT include backticks (```) or the keyword "sql" in the SQL command output.
    2. Just return the plain SQL command without any markdown formatting.

    For example:
    Example 1 - How many entries of records are present? 
    SQL command: SELECT COUNT(*) FROM STUDENT;

    Example 2 - Tell me all the students studying in Data Science class? 
    SQL command: SELECT * FROM STUDENT WHERE CLASS = 'Data Science';

    """


]

##Front End
st.set_page_config(page_title="I can Retrive Any SQL query")
st.title("Prompt To SQL Data")
st.header("Convert your Prompts to get responses , NO need to learn DBMS 😎")

question = st.text_input("Input: ",key="input")

submit=st.button("Ask the question")

if submit:
    response = get_gemini_response(question,prompt)
    print(response)
    response=read_sql_query(response,"student.db")
    st.subheader("The Response is")
    
    for row in response:
        print(row)
        st.header(row)
        
