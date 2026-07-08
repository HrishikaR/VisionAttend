import streamlit as st

# Monkey patch st.space to avoid AttributeError in screens
if not hasattr(st, "space"):
    st.space = lambda: st.markdown("<div style='margin: 15px 0;'></div>", unsafe_allow_html=True)

from src.screens.home_screen import home_screen
from src.screens.teacher_screen import teacher_screen
from src.screens.student_screen import student_screen

from src.components.dialog_auto_enroll import auto_enroll_dialog

def main():
    st.set_page_config(
        page_title='VisionAttend - Making Attendance faster using AI',
        page_icon= "https://i.ibb.co/YTYGn5qV/logo.png"
    )
    if 'login_type' not in st.session_state:
        st.session_state['login_type'] = None

    match st.session_state['login_type']:
        case 'teacher':
            teacher_screen()

        case 'student':
            student_screen()
            if "join-code" in st.query_params:
                auto_enroll_dialog(st.query_params["join-code"])
        
        case None:
            home_screen()

if __name__ == "__main__":
    main()

