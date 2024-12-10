import streamlit as st

st.title("Calculadora")

num1 = st.number_input("Introduce el primer valor")
num2 = st.number_input("Introduce el segundo valor")

st.write("Resultado: ", num1 + num2)