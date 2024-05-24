import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
st.write("Hello, let's learn how to build a streamlit app together")

chart_data = pd.DataFrame(
   {
       "col1": list(range(20)) * 3,
       "col2": np.random.randn(60),
       "col3": ["A"] * 20 + ["B"] * 20 + ["C"] * 20,
   }
)

st.bar_chart(chart_data, x="col1", y="col2", color="col3")
# df = pd.read_csv('data/cc_rfm.csv')
# st.dataframe(df)

# rand = np.random.normal(1, 2, size = 20)
# fig, ax = plt.subplots()
# ax.hist(rand, bins=15)
# st.pyplot(fig)
