import streamlit as st
from datetime import datetime

# إعدادات الصفحة
st.set_page_config(page_title="Emoo ❤️", page_icon="💖", layout="centered")

# --- نظام الباسورد ---
if "password_correct" not in st.session_state:
    st.markdown("""
        <style>
        .stApp { background-color: #0e1117; }
        .login-box { 
            background-color: #1a1c23; 
            padding: 30px; 
            border-radius: 20px; 
            border: 2px solid #ff4d6d; 
            text-align: center;
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

# --- الاستايل الأسود المتناسق (Dark Theme) ---
st.markdown("""
    <style>
    .stApp { background-color: #0e1117; } /* خلفية سوداء شيك */
    
    .block-container {
        background-color: #1a1c23 !important;
        padding: 25px !important;
        border-radius: 20px !important;
        border: 1px solid #3d3d3d !important;
        margin-top: 20px;
    }
    
    h1 { color: #ff4d6d !important; text-align: center !important; margin-bottom: 0px; font-size: 40px; }
    .love-text { color: #ffffff; text-align: center; font-size: 18px; margin-top: 5px; margin-bottom: 30px; }
    h3 { color: #ffb3c1 !important; text-align: center !important; }
    
    /* استايل العدادات في الأسود */
    [data-testid="stMetric"] {
        background-color: #262730 !important;
        border: 1px solid #ff4d6d !important;
        border-radius: 10px !important;
        padding: 10px !important;
    }
    [data-testid="stMetricValue"] { color: #ff4d6d !important; }
    
    .footer { text-align: center; color: #555; font-weight: bold; margin-top: 30px; }
    </style>
""", unsafe_allow_html=True)

st.balloons()

# 1. الترتيب المطلوب: الاسم وتحته الجملة مباشرة
st.markdown("<h1>✨ Emoo ✨</h1>", unsafe_allow_html=True)
st.markdown('<p class="love-text">فقط لأني أحبك.. أحبك للأبد ❤️</p>', unsafe_allow_html=True)

# حساب الوقت
now = datetime.now()
birth_date = datetime(2005, 5, 5)
next_birthday = datetime(now.year, 5, 5)
if next_birthday < now:
    next_birthday = datetime(now.year + 1, 5, 5)
diff = next_birthday - now

st.write("---")

# 2. العداد التنازلي
st.markdown("<h3>🎁 العد التنازلي لعيد ميلادك</h3>", unsafe_allow_html=True)
st.success(f"باقي {diff.days} يوم و {diff.seconds // 3600} ساعة")

st.write("---")

# 3. عداد العمر (تحت بعض عشان الموبايل ميبوظش)
st.markdown("<h3>⏳ رحلتك الجميلة</h3>", unsafe_allow_html=True)
total_diff = now - birth_date
st.metric("أيام", f"{total_diff.days:,}")
st.metric("دقائق", f"{int(total_diff.total_seconds() // 60):,}")
st.metric("ثواني", f"{int(total_diff.total_seconds()):,}")

st.write("---")

# 4. زر المفاجأة
if st.button('اضغطي هنا للمفاجأة 💖'):
    st.snow()

# التوقيع
st.markdown('<div class="footer">By Ahmed Samir</div>', unsafe_allow_html=True)
