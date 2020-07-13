import streamlit as st
import numpy as np
import pandas as pd
st.title("HELLO, this page is created just for experimenting the features of Streamlit")
st.text("--------------------------------------")
st.title("this is the title!")

st.text("this is the text")
st.text("--------------------------------------")
df = pd.DataFrame({
    '1st_col':[1,2,3,4,5],
    '2nd_col':[10,9,8,7,6]
})
st.dataframe(df)

st.text("--------------------------------------")

chart_data = pd.DataFrame(
    np.random.randn(20,3),
    columns=['1st_col','2st_col','3st_col']
)

st.line_chart(chart_data)

st.text("--------------------------------------")

map_data = pd.DataFrame(
    np.random.randn(500,2) / [50,50] + [32.26-100],
    columns=["lat","lon"]
)

st.map(map_data)

st.text("--------------------------------------")

check_box_data = pd.DataFrame(
    np.random.randn(20,3),
    columns=['1st_col','2st_col','3st_col']
)

if st.checkbox("show details"):
      st.dataframe(check_box_data)

st.text("--------------------------------------")

select_box_data = pd.DataFrame(
    np.random.randn(20,3),
    columns=['1st_col','2st_col','3st_col']
)

col = st.selectbox('select the column to be displayed',select_box_data.columns)

st.line_chart(select_box_data[col])

st.text("--------------------------------------")

select_box_data_1 = pd.DataFrame(
    np.random.randn(20,3),
    columns=['1st_col','2st_col','3st_col']
)

col_m = st.multiselect('select the column to be displayed',select_box_data_1.columns)

st.line_chart(select_box_data_1[col_m])

st.text("--------------------------------------")

slider_data = pd.DataFrame(
    np.random.randn(1000,3),
    columns=['something_1','something_2','something_3']
)

if st.checkbox("show data"):
    st.write(slider_data.tail())
    
something_1_pred = st.slider("select the something_1 value",float(slider_data.something_1.min()),float(slider_data.something_2.max()),float(slider_data.something_3.mean()))


if st.button("get the prediction")==1:
    st.write("result1")