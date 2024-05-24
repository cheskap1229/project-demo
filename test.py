pip install matplotlib
pip install --upgrade streamlit matplotlib

import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
st.write("Hello, let's learn how to build a streamlit app together")



df = pd.read_csv("data/cc_rfm.csv")

st.dataframe(df)

df['trans_datetime'] = pd.to_datetime(df['trans_datetime'])

# Extract the day and create a new column
df['day_name'] = df['trans_datetime'].dt.day_name()
df['month'] = df['trans_datetime'].dt.month_name()

df['day_month_year'] = pd.to_datetime(df['day_month_year'], format='%d-%m-%Y')
df['month_year'] = df['trans_datetime'].dt.to_period('M')

total_amount_per_day = df.groupby('day_month_year')['amt'].sum().reset_index()
fig = px.scatter(total_amount_per_day,y="amt", x="day_month_year", trendline="ols");
st.pyplot(fig=fig, clear_figure=None, use_container_width=True, **kwargs)
