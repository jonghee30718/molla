import streamlit as st
import pandas as pd

df = pd.read_csv("Delivery.csv")

st.title("📦 배달 데이터 분석 웹앱")

st.subheader("데이터 미리보기")
st.dataframe(df.head())

column = st.selectbox("분석할 열을 선택하세요", df.columns)
st.subheader(f"'{column}' 열의 통계")
st.write(df[column].describe())

if df[column].dtype == 'object':
    value = st.selectbox("특정 값 보기", df[column].unique())
    st.write(df[df[column] == value])
