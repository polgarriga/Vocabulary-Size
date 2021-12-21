import streamlit as st
import csv

foo = st.text_input("foo")
bar = st.text_input("bar")
baz = st.text_input("baz")

fields = [foo, bar, baz]

if st.button("Add row"):
    with open('C:\\Users\\Pol\\Documents\\Database.csv','a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(fields)
