from util.helper import load_logo_images
from menu import highscore_frame,question_frame,question_finished_frame,quiz_finished_frame
import streamlit as st

class Main:
    def __init__(self):
        st.set_page_config(layout="wide")
        if "quiz_running" not in st.session_state:
            st.session_state.quiz_running=False
        self.sidebar()
        self.quiz()


    def sidebar(self):
        st.sidebar.latex("\\text{\large{Tag der Mathematik - 2022}}")
        st.sidebar.latex("\\text{\Huge{Quiz}}")
        st.sidebar.latex("\\text{\Large{Erkennst du Deep Fakes?}}")
        logo_frame, heading_frame = st.sidebar.columns([1,2])
        #heading_frame.latex("\\text{\Huge{Quiz}}")




        neiss_logo, eu_fonds, eu_esf, mv_bm = load_logo_images()



        st.sidebar.markdown("### Gefördert durch")
        col1, col2 = st.sidebar.columns([1,2])
        col1.image(neiss_logo)
        col2.latex("\\text{\large{NEISS - Projekt}}")
        # Include EU Logos
        st.sidebar.image(eu_fonds)
        colesf, colbm = st.sidebar.columns(2)
        colesf.image(eu_esf)
        colbm.image(mv_bm)

    def quiz(self):
        if st.session_state.quiz_running:
            if st.session_state.quiz_position>=21:
                quiz_finished_frame.QuizFinished()
            else:
                if st.session_state.quiz_current_position_finished:
                    question_finished_frame.QuestionFinished()
                else:
                    question_frame.Question()
                def quitQuiz():
                    st.session_state.quiz_running=False
                st.button("Quiz abbrechen",on_click=quitQuiz)
        else:
            highscore_frame.Highscore()


