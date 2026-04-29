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
            if password == "emoo2026": # تقدر تغير الباسورد ده لأي كلمة تانية
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
        .stMetric { background-color: #ffb3c1; padding: 15px; border-radius: 15px; }
        .footer { position: fixed; left: 0; bottom: 10px; width: 100%; text-align: center; color: #c9184a; font-weight: bold; }
        </style>
        """, unsafe_allow_html=True)

    st.balloons()
    st.title("✨ Emoo ✨")

    # --- عداد الزيارات (بسيط) ---
    if 'count' not in st.session_state:
        st.session_state.count = 1
    else:
        st.session_state.count += 1
    
    st.sidebar.write(f"👁️ عدد الزيارات: {st.session_state.count}")

    # حساب الوقت
    now = datetime.now()
    birth_date = datetime(2005, 5, 5)

    st.subheader("⏳ رحلتك الجميلة:")
    total_diff = now - birth_date
    col1, col2, col3 = st.columns(3)
    col1.metric("أيام", f"{total_diff.days:,}")
    col2.metric("دقائق", f"{int(total_diff.total_seconds() // 60):,}")
    col3.metric("ثواني", f"{int(total_diff.total_seconds()):,}")

    st.write("---")
    st.markdown("<h2 style='text-align: center;'>فقط لأني أحبك للأبد ❤️</h2>", unsafe_allow_html=True)

    # توقيعك
    st.markdown('<div class="footer">By Ahmed Samir</div>', unsafe_allow_html=True)

    if st.button('اضغط هنا لشعور خاص 💖'):
        st.snow()
