import streamlit as st
import csv

@st.cache

foo = st.text_input("foo")
bar = st.text_input("bar")
baz = st.text_input("baz")

fields = [foo, bar, baz]

with open('C:\\Users\\Pol\\Documents\\Database.csv','a', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(fields)
