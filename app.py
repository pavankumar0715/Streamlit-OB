import streamlit as st

st.write("""
# Largest of 3 numbers
""")
#Get Input

st.header('Enter the numbers:')

def user_input_features():
    first_number = st.number_input("Number 1:")
    second_number = st.number_input("Number 2:")
    third_number = st.number_input("Number 3:")
    return max(first_number,second_number,third_number)

x=user_input_features()
st.subheader('Largest Number:')
st.write(x)