import streamlit as st
from datetime import datetime

# إعدادات الصفحة
st.set_page_config(page_title="Emoo ❤️", page_icon="💖", layout="centered")

# --- نظام الباص ---
if "password_correct" not in st.session_state:
    st.markdown("""
        <style>
        .stApp { background-color: #fff0f3; }
        .login-box { 
            background-color: white; 
            padding: 30px; 
            border-radius: 20px; 
            border: 3px solid #ffb3c1; 
            text-align: center;
            box-shadow: 0 4px 15px rgba(0,0,0,0.1);
        }
        h1 { color: #ff4d6d !important; }
        </style>
        <div class="login-box">
            <h1>🔒 دخلي الكود يا ايمو</h1>
        </div>
    """, unsafe_allow_html=True)
    
    password = st.text_input("", type="password", placeholder="اكتبي الكود هنا...")
    if st.button("دخول ✨"):
        if password == "emoo2026":
            st.session_state["password_correct"] = True
            st.rerun()
        else:
            st.error("الكود غلط يا ايمو ❌")
    st.stop()

# --- الاستايل الرايق (بينك متناسق) ---
st.markdown("""
    <style>
    .stApp { background-color: #fff0f3; } /* خلفية بينك هادية */
    
    .block-container {
        background-color: white !important;
        padding: 30px !important;
        border-radius: 25px !important;
        border: 2px solid #ffb3c1 !important;
        box-shadow: 0 10px 25px rgba(255, 179, 193, 0.2);
        margin-top: 20px;
    }
    
    h1 { color: #ff4d6d !important; text-align: center !important; margin-bottom: 0px; }
    .love-text { color: #c9184a; text-align: center; font-size: 20px; font-weight: bold; margin-bottom: 20px; }
    h3 { color: #ff758f !important; text-align: center !important; }
    
    [data-testid="stMetric"] {
        background-color: #fffafb !important;
        border: 1px solid #ffdae0 !important;
        border-radius: 15px !important;
        text-align: center !important;
    }
    
    .footer { text-align: center; color: #ffb3c1; font-weight: bold; margin-top: 30px; font-size: 14px; }
    </style>
""", unsafe_allow_html=True)

st.balloons()

# العنوان والجملة تحت بعض مباشرة
st.markdown("<h1>✨ Emoo ✨</h1>", unsafe_allow_html=True)
st.markdown('<p class="love-text">فقط لأني أحبك.. أحبك للأبد ❤️</p>', unsafe_allow_html=True)

st.write("---")

# حساب الوقت
now = datetime.now()
birth_date = datetime(2005, 5, 5)
next_birthday = datetime(now.year, 5, 5)
if next_birthday < now:
    next_birthday = datetime(now.year + 1, 5, 5)
diff = next_birthday - now

# العدادات
st.markdown("<h3>🎁 العد التنازلي لعيد ميلادك</h3>", unsafe_allow_html=True)
st.success(f"باقي {diff.days} يوم و {diff.seconds // 3600} ساعة")

st.write("---")

st.markdown("<h3>⏳ رحلتك الجميلة</h3>", unsafe_allow_html=True)
total_diff = now - birth_date
col1, col2, col3 = st.columns(3)
col1.metric("أيام", f"{total_diff.days:,}")
col2.metric("دقائق", f"{int(total_diff.total_seconds() // 60):,}")
col3.metric("ثواني", f"{int(total_diff.total_seconds()):,}")

st.write("---")
if st.button('اضغطي هنا للمفاجأة 💖'):
    st.snow()

# التوقيع
st.markdown('<div class="footer">By Ahmed Samir</div>', unsafe_allow_html=True)
