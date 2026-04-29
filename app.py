import streamlit as st
from datetime import datetime

# إعدادات الصفحة
st.set_page_config(page_title="Emoo ❤️", page_icon="💖", layout="centered")

# --- نظام الباسورد ---
def check_password():
    if "password_correct" not in st.session_state:
        st.markdown("""
            <style>
            .stTextInput > div > div > input { background-color: #ffe5ec; border: 2px solid #ffb3c1; border-radius: 10px; }
            .stButton>button { background-color: #ff4d6d; color: white; border-radius: 10px; width: 100%; }
            </style>
            <h3 style='text-align: center; color: #c9184a;'>🔒 هذا الموقع خاص جداً</h3>
        """, unsafe_allow_html=True)
        password = st.text_input("ادخلي كلمة السر", type="password")
        if st.button("دخول"):
            if password == "emoo2026": 
                st.session_state["password_correct"] = True
                st.rerun()
            else:
                st.error("كلمة السر خطأ ❌")
        return False
    return True

if check_password():
    # استايل التصميم المنظم (بينك ومستطيل)
    st.markdown("""
        <style>
        .main { background-color: #fff0f3; }
        .block-container {
            background-color: #ffffff;
            padding: 30px;
            border-radius: 25px;
            border: 3px solid #ffb3c1;
            box-shadow: 0 10px 25px rgba(255, 179, 193, 0.3);
            margin-top: 50px;
        }
        h1 { color: #ff4d6d; text-align: center; font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; }
        h3 { color: #c9184a; }
        .stMetric { background-color: #ffe5ec; padding: 15px; border-radius: 15px; border: 1px solid #ffb3c1; }
        .footer { text-align: center; color: #ff758f; font-weight: bold; margin-top: 50px; padding-bottom: 20px; }
        </style>
    """, unsafe_allow_html=True)

    st.balloons()
    st.title("✨ Emoo ✨")

    # حساب الوقت
    now = datetime.now()
    birth_date = datetime(2005, 5, 5)

    # 1. العداد التنازلي لعيد الميلاد
    next_birthday = datetime(now.year, 5, 5)
    if next_birthday < now:
        next_birthday = datetime(now.year + 1, 5, 5)
    diff = next_birthday - now

    st.markdown("<h3 style='text-align: center;'>🎁 العد التنازلي لعيد ميلادك</h3>", unsafe_allow_html=True)
    st.success(f"باقي **{diff.days}** يوم و **{diff.seconds // 3600}** ساعة على يومك المميز!")
    
    st.write("---")

    # 2. عداد العمر المنظم
    st.markdown("<h3 style='text-align: center;'>⏳ رحلتك الجميلة</h3>", unsafe_allow_html=True)
    total_diff = now - birth_date
    col1, col2, col3 = st.columns(3)
    with col1: st.metric("أيام", f"{total_diff.days:,}")
    with col2: st.metric("دقائق", f"{int(total_diff.total_seconds() // 60):,}")
    with col3: st.metric("ثواني", f"{int(total_diff.total_seconds()):,}")

    st.write("---")
    
    # 3. الرسالة والثلج
    st.info("🎮 بدأت حكايتنا في 2021.. ومن يومها والدنيا أحلى بكثير!")
    st.markdown("<h2 style='text-align: center; color: #ff4d6d;'>فقط لأني أحبك للأبد ❤️</h2>", unsafe_allow_html=True)

    if st.button('اضغطي هنا للمفاجأة 💖'):
        st.snow()

    # التوقيع باسمك في آخر المستطيل
    st.markdown('<div class="footer">By Ahmed Samir</div>', unsafe_allow_html=True)
