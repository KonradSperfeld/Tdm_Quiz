import streamlit as st

class Highscore:
    def __init__(self):
        def startQuiz():
            st.session_state.quiz_running=True
            st.session_state.quiz_position=1
            st.session_state.quiz_current_position_finished=False
            st.session_state.quiz_time=0
            st.session_state.num_correct_answers=0
        st.button("Starte Neues Quiz",on_click=startQuiz)
        self.show_highscore()

    def show_highscore(self):
        st.markdown("# Aktuelle Bestenliste")
        st.write("TODO")
