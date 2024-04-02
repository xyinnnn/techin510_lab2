import  streamlit as st
import seaborn as sns
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="Penguins Explorer",
    page_icon="🐧",
    layout="centered",
    initial_sidebar_state="auto",
    menu_items=None
)

st.title("🐧Penguins Explorer")

st.markdown("")

df = pd.read_csv("https://raw.githubusercontent.com/mcnakhaee/palmerpenguins/master/palmerpenguins/data/penguins.csv")



bill_length_slider  = st.slider(
    "Bill Length (mm)"
    min(df["bill_length_mm"]),
    max(df["bill_length_mm"]),
)



species_filter = st.selectbox(
    "Species", 
    df["species"].unique,
    index=None
)


island_filter = st.multiselectx("Island", df["island"].unique())




if species_filter:
    df = df[df["species"] == species_filter]

if island_filter:
    df = df[df["island"].isin(island_filter)]

df = df[df["bill_length_mm"] > bill_length_slider]

st.write(df)

fig = px.histogram(
    df,
    x="bill_length_mm"
)
st.plotly_chart(fig)

fig2 = px.scatter(
    df,
    x="bill_length_mm",
    y="bill_depth_mm"
)

st.plotly_chart(fig2)
