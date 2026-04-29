import streamlit as st
from datetime import datetime
import time

# إعدادات الصفحة عشان تظهر بقلوب حمرا
st.set_page_config(page_title="Happy Birthday Emoo ❤️", page_icon="💖")

# --- البيانات الأساسية ---
NAME = "Eman (Emoo)"
BIRTH_DATE = datetime(2005, 5, 5, 0, 0)
FIRST_MET_YEAR = 2021
MESSAGE = "فقط لأني أحبك للأبد ❤️"

# استايل الموقع (ألوان وردي وأحمر)
st.markdown("""
    <style>
    .main {
        background-color: #fff0f3;
    }
    h1 {
        color: #ff4d6d;
        text-align: center;
    }
    .stMetric {
        background-color: #ffb3c1;
        padding: 15px;
        border-radius: 15px;
        box-shadow: 2px 2px 5px rgba(0,0,0,0.1);
    }
    </style>
    """, unsafe_allow_html=True)

st.balloons()
st.title(f"✨ عالم {NAME} الخاص ✨")

# حساب الوقت الحالي
now = datetime.now()

# 1. عداد الوقت اللي ناقص على عيد ميلادها الجاي
next_birthday = datetime(now.year, BIRTH_DATE.month, BIRTH_DATE.day)
if next_birthday < now:
    next_birthday = datetime(now.year + 1, BIRTH_DATE.month, BIRTH_DATE.day)

diff_to_next = next_birthday - now
days_left = diff_to_next.days
hours_left = diff_to_next.seconds // 3600

st.subheader(f"🎁 الوقت المتبقي لعيد ميلادك الجاي:")
st.success(f"باقي **{days_left}** يوم و **{hours_left}** ساعة على يومك المميز!")

st.write("---")

# 2. عداد العمر التفصيلي (أيام، دقايق، ثواني)
st.subheader("⏳ رحلتك في الحياة حتى الآن:")
total_diff = now - BIRTH_DATE
total_days = total_diff.days
total_minutes = total_diff.total_seconds() // 60
total_seconds = total_diff.total_seconds()

col1, col2, col3 = st.columns(3)
col1.metric("أيام", f"{total_days:,}")
col2.metric("دقائق", f"{int(total_minutes):,}")
col3.metric("ثواني", f"{int(total_seconds):,}")

st.write("---")

# 3. ذكرى ببجي (2021)
st.subheader("🎮 ذكرى اللقاء الأول")
years_together = now.year - FIRST_MET_YEAR
st.info(f"منذ عام {FIRST_MET_YEAR} (لما بدأت الحكاية في ببجي).. بقالنا {years_together} سنين سوا!")

# 4. الرسالة الكبيرة والقلوب
st.write("---")
st.markdown(f"<h2 style='text-align: center; color: #c9184a;'>{MESSAGE}</h2>", unsafe_allow_html=True)

# إضافة قلوب وردي وحمرا في الصفحة
if st.button('اضغط هنا عشان تشوف قلبي 💖'):
    st.snow() # هتظهر قلوب/ندف تلج بشكل رومانسي
    st.write("💖💗💓💞💕❣❤️💔💘💝")

st.markdown("<p style='text-align: center;'>Made with ❤️ by Your Code Master</p>", unsafe_allow_html=True)
