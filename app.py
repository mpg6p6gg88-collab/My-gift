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
            padding: 30px; border-radius: 20px; 
            border: 2px solid #ff4d6d; text-align: center;
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

# --- الاستايل الأسود الرايق ---
st.markdown("""
    <style>
    .stApp { background-color: #0e1117; color: white; }
    .block-container {
        background-color: #1a1c23 !important;
        padding: 25px !important;
        border-radius: 20px !important;
        border: 1px solid #333 !important;
        margin-top: 20px;
    }
    h1 { color: #ff4d6d !important; text-align: center !important; margin-bottom: 5px; }
    .love-text { color: #ffffff; text-align: center; font-size: 18px; margin-bottom: 20px; }
    
    /* استايل الرسالة المخفية */
    .stDetails {
        background-color: #262730 !important;
        border-radius: 10px !important;
        border: 1px solid #ff4d6d !important;
    }
    
    /* استايل العدادات */
    [data-testid="stMetric"] {
        background-color: #262730 !important;
        border: 1px solid #ff4d6d !important;
        border-radius: 10px !important;
        padding: 10px !important;
        margin-bottom: 10px;
    }
    .footer { text-align: center; color: #555; margin-top: 30px; font-size: 14px; }
    </style>
""", unsafe_allow_html=True)

st.balloons()

# 1. العنوان والجملة
st.markdown("<h1>✨ Emoo ✨</h1>", unsafe_allow_html=True)
st.markdown('<p class="love-text">فقط لأني أحبك.. أحبك للأبد ❤️</p>', unsafe_allow_html=True)

# 2. خيار "رسالة مني ليك"
with st.expander("💌 دي رسالة مني ليكي (افتحيها)"):
    st.write("""
    الموقع ده ذكري مني لو الايام خدتنا وبعدنا عن بعض 
    بدأتها بحاجه حزينه صح؟ 😂😂
    مش هقدر اقول كلام كتير بس انتي عندي حاجه كبيره جدا واختي ويومي مش بيكمل من غيرك ساعات بعاتب الدنيا انك مش جنبي واختي فعلا 
    بس حتي لو بعدتنا المسافات انا بحبك ❤️
    
    احلا حد في الدنيا كده كده 💗
    """)

st.write("---")

# حساب الوقت
now = datetime.now()
birth_date = datetime(2005, 5, 5)
next_birthday = datetime(now.year, 5, 5)
if next_birthday < now:
    next_birthday = datetime(now.year + 1, 5, 5)
diff = next_birthday - now

# 3. العدادات (تحت بعض للموبايل)
st.markdown("<h3 style='text-align:center; color:#ffb3c1;'>🎁 العد التنازلي لعيد ميلادك</h3>", unsafe_allow_html=True)
st.success(f"باقي {diff.days} يوم و {diff.seconds // 3600} ساعة")

st.write("---")

st.markdown("<h3 style='text-align:center; color:#ffb3c1;'>⏳ رحلتك الجميلة</h3>", unsafe_allow_html=True)
total_diff = now - birth_date
st.metric("أيام", f"{total_diff.days:,}")
st.metric("دقائق", f"{int(total_diff.total_seconds() // 60):,}")
st.metric("ثواني", f"{int(total_diff.total_seconds()):,}")

st.write("---")

# 4. زر المفاجأة والتوقيع
if st.button('اضغطي هنا للمفاجأة 💖'):
    st.snow()

st.markdown('<div class="footer">By Ahmed Samir</div>', unsafe_allow_html=True)
