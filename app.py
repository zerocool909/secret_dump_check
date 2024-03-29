import streamlit as st
import os

# Everything is accessible via the st.secrets dict:
st.write("DB username:", st.secrets["db_username"])
st.write("DB password:", st.secrets["db_password"])
st.write("My cool secrets:", st.secrets["my_cool_secrets"]["things_i_like"])

# And the root-level secrets are also accessible as environment variables:
st.write(
    "Has environment variables been set:",
    os.environ["db_username"] == st.secrets["db_username"],
)

if "Python" in st.secrets["my_cool_secrets"]["things_i_like"]:
    st.write("Python encountered")
if "Streamlit" in st.secrets["my_cool_secrets"]["things_i_like"]:
    st.write("Streamlit found")

if "Streamlit112" in st.secrets["my_cool_secrets"]["things_i_like"]:
    st.write("Streamlit found")
else:
    st.write("unauthorised")
