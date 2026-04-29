import streamlit as st
from datetime import datetime

# إعدادات الصفحة
st.set_page_config(page_title="Emoo ❤️", page_icon="💖")

# --- نظام الباسورد ---
def check_password():
    if "password_correct" not in st.session_state:
        st.markdown("<h3 style='text-align: center;'>هذا الموقع خاص جداً.. ادخلي كلمة السر 🔒</h3>", unsafe_allow_html=True)
        password = st.text_input("كلمة السر", type="password")
        if st.button("دخول"):
            if password == "emoo2026": 
                st.session_state["password_correct"] = True
                st.rerun()
            else:
                st.error("كلمة السر غلط يا ست الكل ❌")
        return False
    return True

if check_password():
    # استايل الألوان
    st.markdown("""
        <style>
        .main { background-color: #fff0f3; }
        h1 { color: #ff4d6d; text-align: center; }
        .stMetric { background-color: #ffb3c1; padding: 10px; border-radius: 15px; }
        .footer { position: fixed; left: 0; bottom: 10px; width: 100%; text-align: center; color: #c9184a; font-weight: bold; }
        </style>
        """, unsafe_allow_html=True)

    st.balloons()
    st.title("✨ Emoo ✨")

    # حساب الوقت
    now = datetime.now()
    birth_date = datetime(2005, 5, 5) # تاريخ الميلاد

    # --- رجعنا العداد التنازلي هنا ---
    next_birthday = datetime(now.year, 5, 5)
    if next_birthday < now:
        next_birthday = datetime(now.year + 1, 5, 5)
    diff = next_birthday - now

    st.subheader("🎁 ناقص قد إيه على عيد ميلادك الجاي:")
    st.success(f"باقي **{diff.days}** يوم و **{diff.seconds // 3600}** ساعة!")
    
    st.write("---")

    # عداد العمر التفصيلي
    st.subheader("⏳ رحلتك الجميلة حتى الآن:")
    total_diff = now - birth_date
    col1, col2, col3 = st.columns(3)
    col1.metric("أيام", f"{total_diff.days:,}")
    col2.metric("دقائق", f"{int(total_diff.total_seconds() // 60):,}")
    col3.metric("ثواني", f"{int(total_diff.total_seconds()):,}")

    st.write("---")
    st.info("🎮 عرفنا بعض من سنة 2021 في ببجي.. ومن يومها والدنيا أحلى!")
    st.markdown("<h2 style='text-align: center; color: #c9184a;'>فقط لأني أحبك للأبد ❤️</h2>", unsafe_allow_html=True)

    if st.button('اضغط هنا لشعور خاص 💖'):
        st.snow()

    # التوقيع باسمك
    st.markdown('<div class="footer">By Ahmed Samir</div>', unsafe_allow_html=True)
