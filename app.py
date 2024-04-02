import  streamlit as st
import seaborn as sns
import pandas as pd

st.set_page_config(
    page_title="Penguins Explorer",
    page_icon="🐧",
    layout="centered",
    initial_sidebar_state="auto",
    menu_items=None
)

df = pd.read_csv("https://raw.githubusercontent.com/mcnakhaee/palmerpenguins/master/palmerpenguins/data/penguins.csv")

st.write(df)