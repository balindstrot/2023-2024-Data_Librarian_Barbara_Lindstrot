# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
""
import streamlit as st
import pandas as pd

st.write("Tabelle:")

df = pd.DataFrame({
    'first column': [1,2,3,4],
    'second column': [10,20,30,40]
    })

df
"""

#learn more about streamlit: https://docs.streamlit.io/

import streamlit as st
import pyterrier as pt
import pickle

if not pt.started():
    pt.init()
    
st.write("Suche zum Thema Forschungszentrum Jülich")

def init():

    index = pt.IndexFactory.of("./juelich2_index_mult/data.properties")
    st.session_state["engine"] = pt.BatchRetrieve(index, wmodel="TF_IDF")
   # st.session_state["data"] = pickle.load(open("/pyterrier_uebung2.", "rb"))
    st.session_state["data"] = pickle.load(open("juelich2_publicaions.pkl", "rb"))

def search(query):

    res = st.session_state["engine"].search(query)
    fields_to_show = ['text', 'tags', 'url', 'author', 'description']

    for _, row in res.iterrows():
        score = round(row['score'], 2)
        entry = st.session_state["data"][st.session_state["data"]['docno'] == row['docno']].iloc[0]

        for field in fields_to_show:
            if field == "text":
                st.title(entry[field])
            else:
                st.write(f"{field.capitalize()}: \t {entry[field]}")

        st.write(f"Score: {score}")
        st.divider()


if not "engine" in st.session_state:
    init()

query = st.sidebar.text_input("Query")
st.sidebar.button("Search", on_click=search, args=(query,))


