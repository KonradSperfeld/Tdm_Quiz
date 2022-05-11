import streamlit as st
class QuizFinished:
    def __init__(self):
        st.balloons
        st.write(f'Geschafft: Du hast {st.session_state.num_correct_answers} von 20 Fragen korrekt beantwort.')
        def toHighscore():
            st.session_state.quiz_running=False
        st.button("Weiter zur Bestenliste",on_click=toHighscore)
