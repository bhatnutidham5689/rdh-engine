import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
plt.style.use('ggplot')

# ---------- PAGE CONFIG ----------
st.set_page_config(
    page_title="RDH Engine",
    page_icon="🔥",
    layout="wide"
)

# ---------- HEADER ----------
st.title("🔥 RDH Engine Pro")
st.markdown("### ระบบวิเคราะห์ตัวเลขอัตโนมัติ")

st.divider()

# ---------- INPUT SECTION ----------
col1, col2 = st.columns([3,1])

with col1:
    number_input = st.text_input("ใส่ตัวเลข (เว้นวรรคได้)", placeholder="เช่น 250 137 160 917")

with col2:
    calculate = st.button("🚀 คำนวณ")

# ---------- PROCESS ----------
if calculate and number_input:

    clean_number = number_input.replace(" ", "")
    digits = list(clean_number)

    df = pd.DataFrame({
        "ตำแหน่ง": range(1, len(digits)+1),
        "ตัวเลข": digits
    })

    st.divider()
    st.subheader("📊 ตารางผลลัพธ์")
    st.dataframe(df, use_container_width=True)

    # ---------- STATISTICS ----------
    st.subheader("📈 สถิติ")

    digit_counts = df["ตัวเลข"].value_counts().sort_index()

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("จำนวนตัวเลขทั้งหมด", len(digits))

    with col2:
        st.metric("ตัวเลขไม่ซ้ำ", digit_counts.count())

    with col3:
        most_common = digit_counts.idxmax()
        st.metric("ตัวที่พบมากสุด", most_common)

    # ---------- CHART ----------
    st.subheader("📊 กราฟการกระจายตัวเลข")

    fig, ax = plt.subplots()
    digit_counts.plot(kind='bar', ax=ax)
    ax.set_xlabel("ตัวเลข")
    ax.set_ylabel("จำนวนครั้ง")
    st.pyplot(fig)

    st.success("วิเคราะห์เสร็จสมบูรณ์ ✅")
    import matplotlib.pyplot as plt

# นับความถี่
counts = df['เลข'].value_counts().sort_values(ascending=False)

st.subheader("📊 กราฟเรียงจากมากไปน้อย")

fig2, ax2 = plt.subplots()
counts.plot(kind='bar', ax=ax2)
ax2.set_xlabel("ตัวเลข")
ax2.set_ylabel("จำนวนครั้ง")
st.pyplot(fig2)
st.subheader("🥧 สัดส่วนการกระจายตัวเลข")

fig3, ax3 = plt.subplots()
ax3.pie(counts, labels=counts.index, autopct='%1.1f%%')
ax3.set_title("สัดส่วนตัวเลขทั้งหมด")
st.pyplot(fig3)
