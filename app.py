import streamlit as st

st.title("🔥 RDH Engine")

def extract_digits(number):
    digits = list(str(number))
    top3 = sorted(set(digits), key=digits.count, reverse=True)[:3]
    return top3

user_input = st.text_input("ใส่ตัวเลข")

if user_input:
    result = extract_digits(user_input)
    st.write("Digits:", result)
