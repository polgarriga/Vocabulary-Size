import streamlit as st
import pandas as pd

@st.cache(allow_output_mutation=True)
def get_data():
    return []

user_id = st.text_input("User ID")
foo = st.slider("foo", 0, 100)
bar = st.slider("bar", 0, 100)

if st.button("Add row"):
    get_data().append({"UserID": user_id, "foo": foo, "bar": bar})

st.write(pd.DataFrame(get_data()))
