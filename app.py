import streamlit as st
from datetime import datetime

# إعدادات الصفحة
st.set_page_config(page_title="Emoo ❤️", page_icon="💖")

# --- نظام الباسورد ---
if "password_correct" not in st.session_state:
    st.markdown("""
        <style>
        .stApp { background-color: #ffdae0; }
        .login-box { background-color: white; padding: 30px; border-radius: 20px; border: 5px solid #ff4d6d; text-align: center; }
        h1 { color: #ff4d6d !important; }
        </style>
        <div class="login-box">
            <h1>🔒 دخلي الكود يا ايمو</h1>
        </div>
    """, unsafe_allow_html=True)
    
    password = st.text_input("كلمة السر", type="password")
    if st.button("دخول ✨"):
        if password == "emoo2026":
            st.session_state["password_correct"] = True
            st.rerun()
        else:
            st.error("الكود غلط يا ايمو ❌")
    st.stop()

# --- التصميم الداخلي (بينك قوي ومنظم) ---
st.markdown("""
    <style>
    /* الخلفية الوردية */
    .stApp { background-color: #ff85a1; } 
    
    /* المستطيل الأبيض الأساسي */
    .block-container {
        background-color: white !important;
        padding: 25px !important;
        border-radius: 25px !important;
        border: 6px solid #ff4d6d !important;
        box-shadow: 0 10px 20px rgba(0,0,0,0.2);
        margin-top: 20px;
    }
    
    /* العناوين بألوان قوية */
    h1, h2, h3 { color: #c9184a !important; text-align: center !important; font-weight: bold !important; }
    
    /* استايل العدادات */
    [data-testid="stMetric"] {
        background-color: #ffe5ec !important;
        border: 3px solid #ff4d6d !important;
        border-radius: 15px !important;
        padding: 15px !important;
        margin-bottom: 15px !important;
    }
    [data-testid="stMetricValue"] { color: #ff4d6d !important; font-weight: bold !important; }
    
    .footer { text-align: center; color: #ff4d6d; font-weight: bold; margin-top: 30px; font-size: 20px; }
    </style>
""", unsafe_allow_html=True)

st.balloons()
st.markdown("<h1>✨ Emoo ✨</h1>", unsafe_allow_html=True)

# حساب الوقت
now = datetime.now()
birth_date = datetime(2005, 5, 5)
next_birthday = datetime(now.year, 5, 5)
if next_birthday < now:
    next_birthday = datetime(now.year + 1, 5, 5)
diff = next_birthday - now

# العداد التنازلي
st.markdown("<h3>🎁 باقي على عيد ميلادك:</h3>", unsafe_allow_html=True)
st.info(f"باقي {diff.days} يوم و {diff.seconds // 3600} ساعة")

st.write("---")

# العدادات تحت بعضها (عشان الموبايل)
st.markdown("<h3>⏳ رحلتك الجميلة:</h3>", unsafe_allow_html=True)
total_diff = now - birth_date
st.metric("أيام", f"{total_diff.days:,}")
st.metric("دقائق", f"{int(total_diff.total_seconds() // 60):,}")
st.metric("ثواني", f"{int(total_diff.total_seconds()):,}")

st.write("---")
st.markdown("<h2 style='text-align: center;'>أحبك للأبد ❤️</h2>", unsafe_allow_html=True)

if st.button('اضغطي هنا للمفاجأة 💖'):
    st.snow()

st.markdown('<div class="footer">By Ahmed Samir</div>', unsafe_allow_html=True)
