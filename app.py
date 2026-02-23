import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# -------------------
# ตั้งค่าหน้าเว็บ
# -------------------
st.set_page_config(page_title="RDH Engine Pro", layout="centered")

st.title("🔥 RDH Engine Pro")
st.subheader("ระบบวิเคราะห์ตัวเลขอัตโนมัติ")

# -------------------
# รับค่าจากผู้ใช้
# -------------------
number_input = st.text_area(
    "ใส่ตัวเลข (คั่นด้วยเว้นวรรค)",
    placeholder="เช่น 250 137 160 917"
)

# -------------------
# ปุ่มคำนวณ
# -------------------
if st.button("🔍 คำนวณ"):

    if number_input.strip() == "":
        st.warning("กรุณาใส่ตัวเลขก่อน")
    else:
        # แยกตัวเลข
        numbers = number_input.split()

        # สร้าง DataFrame
        df = pd.DataFrame(numbers, columns=["เลข"])

        # นับความถี่
        counts = df["เลข"].value_counts().sort_values(ascending=False)

        # แสดงผล
        st.subheader("📊 ความถี่ตัวเลข")
        st.dataframe(counts)

        # -------------------
        # กราฟ
        # -------------------
        st.subheader("📈 กราฟแสดงความถี่")

        fig, ax = plt.subplots()
        counts.plot(kind="bar", ax=ax)
        plt.xticks(rotation=45)

        st.pyplot(fig)

        st.success("วิเคราะห์เสร็จเรียบร้อย ✅")
