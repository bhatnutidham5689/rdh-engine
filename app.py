import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from itertools import combinations

st.set_page_config(page_title="RDH Engine Pro", layout="centered")

st.title("🔥 RDH Engine Pro")
st.subheader("วิเคราะห์คู่เลขแบบผสมทุกหลัก")

number_input = st.text_area(
    "ใส่ตัวเลขย้อนหลัง (เว้นวรรคคั่น)",
    placeholder="เช่น 250 137 160 917"
)

if st.button("🔍 วิเคราะห์คู่เลข"):

    if number_input.strip() == "":
        st.warning("กรุณาใส่ข้อมูลก่อน")
    else:
        numbers = number_input.split()
        pairs = []

        # จับคู่ทุกหลักในเลขเดียวกัน
        for num in numbers:
            digits = list(num)
            if len(digits) >= 2:
                for combo in combinations(digits, 2):
                    pair = "".join(combo)
                    pairs.append(pair)

        pair_df = pd.DataFrame(pairs, columns=["Pair"])
        pair_counts = pair_df["Pair"].value_counts().sort_values(ascending=False)

        st.subheader("🔥 ความถี่คู่เลข")
        st.dataframe(pair_counts)

        if len(pair_counts) > 0:
            top_pair = pair_counts.index[0]
            st.success(f"คู่เลขเด่นที่สุดคือ: {top_pair}")

        # กราฟ
        st.subheader("📊 กราฟความถี่คู่เลข (Top 10)")

        fig, ax = plt.subplots()
        pair_counts.head(10).plot(kind="bar", ax=ax)
        st.pyplot(fig)

        st.success("วิเคราะห์เสร็จเรียบร้อย ✅")
