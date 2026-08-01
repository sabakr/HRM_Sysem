import streamlit as st
import pandas as pd

st.set_page_config(page_title="نظام HRM System", layout="wide")

st.markdown("""
<style>
    .stApp { background-color: #F4F7F6; }
    .login-container {
        max-width: 450px; margin: 50px auto; padding: 40px;
        background-color: #FFFFFF; border-radius: 15px;
        box-shadow: 0 4px 8px rgba(0,0,0,0.1); text-align: center;
    }
    .dash-card {
        background-color: #FFFFFF; border-radius: 15px; padding: 20px;
        text-align: center; box-shadow: 0 4px 10px rgba(0,0,0,0.05);
        margin-bottom: 10px; border: 1px solid #EAEAEA;
    }
    .dash-card h4 { margin: 0; color: #333; font-weight: bold; }
    .dash-card .badge {
        background-color: #E2E2E2; color: #333; font-size: 12px;
        padding: 3px 10px; border-radius: 15px; margin-left: 10px;
    }
    .dash-card p { color: #888; font-size: 14px; margin-top: 15px; }
    div[data-testid="stButton"] > button { border-radius: 8px; font-weight: bold; }
</style>
""", unsafe_allow_html=True)

if 'logged_in' not in st.session_state:
    st.session_state['logged_in'] = False
if 'current_page' not in st.session_state:
    st.session_state['current_page'] = 'dashboard'

def show_login():
    with st.container():
        st.markdown("""
            <div class="login-container">
                <img src="https://img.icons8.com/color/96/000000/combo-chart.png" alt="logo" style="width: 60px;"/>
                <h2 style="color: #333; font-weight: bold; margin-top: 10px;">HRM System</h2>
                <p style="color: #666; margin-bottom: 30px;">تسجيل الدخول إلى لوحة التحكم (النسخة السحابية)</p>
            </div>
        """, unsafe_allow_html=True)
        
        c1, c2, c3 = st.columns([1, 2, 1])
        with c2:
            # قمنا بتغيير الـ Key هنا لتجنب أي تداخل قديم
            username = st.text_input("👤 اسم المستخدم", placeholder="أدخل اسم المستخدم", key="login_username")
            password = st.text_input("🔒 كلمة المرور", placeholder="أدخل كلمة المرور", type="password", key="login_password")
            
            if st.button("تسجيل الدخول ➡", use_container_width=True):
                if username == "admin" and password == "1234":
                    st.session_state['logged_in'] = True
                    st.session_state['current_page'] = 'dashboard'
                    st.rerun()
                else:
                    st.error("❌ اسم المستخدم أو كلمة المرور غير صحيحة. (استخدمي admin و 1234)")

def draw_card(col, title_en, title_ar, subtitle, page_target):
    with col:
        st.markdown(f"""
            <div class="dash-card">
                <h4>{title_en} <span class="badge">{title_ar}</span></h4>
                <p>{subtitle}</p>
            </div>
        """, unsafe_allow_html=True)
        if st.button(f"OPEN ➔", key=f"btn_{page_target}", use_container_width=True):
            st.session_state['current_page'] = page_target
            st.rerun()

def show_dashboard():
    col_title, col_logout = st.columns([4, 1])
    with col_title:
        st.title("🪟 Interactive Dashboard")
    with col_logout:
        st.write("") 
        if st.button("تسجيل خروج 🚪", use_container_width=True):
            st.session_state['logged_in'] = False
            st.rerun()
            
    st.write("---")
    
    row1_c1, row1_c2, row1_c3 = st.columns(3)
    draw_card(row1_c1, "Emp_info", "معلومات الموظفين", "Employee records", "emp_info")
    draw_card(row1_c2, "Emp_Salary", "الرواتب", "Salary & payroll", "emp_salary")
    draw_card(row1_c3, "Emp_Vacation", "الإجازات", "Leave requests", "emp_vacation")
    
    st.write("") 
    
    row2_c1, row2_c2, row2_c3 = st.columns(3)
    draw_card(row2_c1, "Punch_In_Out", "البصمة / الحضور", "Punch in & punch out", "punch_in_out")
    draw_card(row2_c2, "Report", "التقارير", "Analytics", "reports")
    draw_card(row2_c3, "Account_Requests", "طلبات الحسابات", "Create & password requests", "account_req")

def show_emp_info():
    if st.button("⬅ عودة للوحة التحكم"):
        st.session_state['current_page'] = 'dashboard'
        st.rerun()
st.title("معلومات الموظفين (Emp_info)")
st.write("---")
c1, c2, c3 = st.columns(3)
with c3:
        st.selectbox("الجنس", ["اختر الجنس", "ذكر", "أنثى"])
with c2:
        st.date_input("تاريخ الميلاد")
with c1:
        st.text_input("الرقم الوطني", placeholder="أدخل الرقم الوطني")
c4, c5, c6 = st.columns(3)
with c6:
        st.text_input("العنوان", placeholder="أدخل العنوان")
with c5:
        st.text_input("رقم الهاتف", placeholder="أدخل رقم الهاتف")
with c4:
        st.text_input("البريد الإلكتروني", placeholder="أدخل البريد الإلكتروني")
        st.date_input("تاريخ التوظيف *")
st.write("")
b1, b2, b3, b4, b5, b6 = st.columns(6)
    with b6: st.button("➕ إضافة", use_container_width=True)
    with b5: st.button("📝 تعديل", use_container_width=True)
    with b4: st.button("🗑 حذف", use_container_width=True)
    with b3: st.button("🔍 بحث", use_container_width=True)
    with b2: st.button("🖨 طباعة", use_container_width=True)
    with b1: st.button("📊 تصدير Excel", use_container_width=True)
    
    st.write("---")
    
    dummy_data = {
        "الرقم الوظيفي": [101, 102, 103],
        "الاسم": ["أحمد سعيد", "سارة محمد", "خالد عبدالله"],
        "القسم": ["تقنية المعلومات", "الموارد البشرية", "التسويق"],
        "الراتب": [5500, 4800, 6200]
    }
    df_hr = pd.DataFrame(dummy_data)
    st.dataframe(df_hr, use_container_width=True)

def show_placeholder(title):
    if st.button("⬅ عودة للوحة التحكم"):
        st.session_state['current_page'] = 'dashboard'
        st.rerun()
    st.title(title)
    st.info("هذه الصفحة قيد التطوير.")

if not st.session_state['logged_in']:
    show_login()
else:
    if st.session_state['current_page'] == 'dashboard':
        show_dashboard()
    elif st.session_state['current_page'] == 'emp_info':
        show_emp_info()
    elif st.session_state['current_page'] == 'emp_salary':
        show_placeholder("صفحة الرواتب (Emp_Salary)")
    elif st.session_state['current_page'] == 'emp_vacation':
        show_placeholder("صفحة الإجازات (Emp_Vacation)")
    elif st.session_state['current_page'] == 'punch_in_out':
        show_placeholder("صفحة البصمة (Punch_In_Out)")
    elif st.session_state['current_page'] == 'reports':
        show_placeholder("التقارير (Reports)")
    elif st.session_state['current_page'] == 'account_req':
        show_placeholder("طلبات الحسابات (Account_Requests)")
