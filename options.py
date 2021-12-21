import streamlit as st
import pandas as pd
import csv

f = open('C:/Users/Pol/Documents/Database.csv', 'w')

user_id = st.text_input("User ID")
foo = st.slider("foo", 0, 100)
bar = st.slider("bar", 0, 100)

writer = csv.writer(f)

if st.button("Add row"):
    
    df = [{"UserID": user_id, "foo": foo, "bar": bar}]
    df = pd.DataFrame(df)

writer.writerow(df)

f.close()
