import streamlit as st
from datetime import datetime

# إعدادات الصفحة
st.set_page_config(page_title="Emoo ❤️", page_icon="💖", layout="centered")

# --- نظام الباسورد بتعديل الرسالة ---
def check_password():
    if "password_correct" not in st.session_state:
        st.markdown("""
            <style>
            .stTextInput > div > div > input { background-color: #ffe5ec; border: 2px solid #ff4d6d; border-radius: 10px; color: #c9184a; }
            .stButton>button { background-color: #ff4d6d; color: white; border-radius: 10px; width: 100%; font-weight: bold; }
            .pass-text { text-align: center; color: #ff4d6d; font-family: 'Arial'; font-weight: bold; margin-bottom: 20px; }
            </style>
            <div class="pass-text"><h1>🔒 دخلي الكود يا ايمو</h1></div>
        """, unsafe_allow_html=True)
        password = st.text_input("كلمة السر", type="password", label_visibility="collapsed")
        if st.button("دخول ✨"):
            if password == "emoo2026": 
                st.session_state["password_correct"] = True
                st.rerun()
            else:
                st.error("الكود غلط يا ايمو ❌")
        return False
    return True

if check_password():
    # استايل المستطيل واللون البينك المتناسق
    st.markdown("""
        <style>
        /* الخلفية الأساسية للموقع */
        .stApp {
            background-color: #ffdae0; 
        }
        /* المستطيل الأبيض المنظم في النص */
        .block-container {
            background-color: #ffffff;
            padding: 40px !important;
            border-radius: 30px;
            border: 4px solid #ff4d6d;
            box-shadow: 0 15px 35px rgba(255, 77, 109, 0.4);
            margin-top: 30px;
        }
        h1 { color: #ff4d6d; text-align: center; font-size: 45px; font-weight: bold; }
        h3 { color: #c9184a; text-align: center; font-weight: bold; }
        /* استايل العدادات البينك */
        [data-testid="stMetricValue"] { color: #ff4d6d !important; font-size: 35px !important; }
        [data-testid="stMetricLabel"] { color: #c9184a !important; font-size: 18px !important; }
        .stMetric { background-color: #fff0f3; padding: 20px; border-radius: 20px; border: 2px solid #ffb3c1; text-align: center; }
        .footer { text-align: center; color: #ff4d6d; font-weight: bold; margin-top: 40px; font-size: 18px; border-top: 1px solid #ffb3c1; padding-top: 15px; }
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

    st.markdown("<h3>🎁 العد التنازلي لعيد ميلادك</h3>", unsafe_allow_html=True)
    st.success(f"باقي **{diff.days}** يوم و **{diff.seconds // 3600}** ساعة على يومك المميز!")
    
    st.write("---")

    # 2. عداد العمر (أيام - دقائق - ثواني)
    st.markdown("<h3>⏳ رحلتك الجميلة في الحياة</h3>", unsafe_allow_html=True)
    total_diff = now - birth_date
    col1, col2, col3 = st.columns(3)
    with col1: st.metric("أيام", f"{total_diff.days:,}")
    with col2: st.metric("دقائق", f"{int(total_diff.total_seconds() // 60):,}")
    with col3: st.metric("ثواني", f"{int(total_diff.total_seconds()):,}")

    st.write("---")
    
    # 3. الرسالة والزرار
    st.info("🎮 بدأت حكايتنا في 2021.. ومن يومها والدنيا أحلى بكثير!")
    st.markdown("<h2 style='text-align: center; color: #ff4d6d;'>فقط لأني أحبك للأبد ❤️</h2>", unsafe_allow_html=True)

    if st.button('اضغطي هنا للمفاجأة 💖'):
        st.snow()

    # التوقيع باسمك
    st.markdown('<div class="footer">By Ahmed Samir</div>', unsafe_allow_html=True)
