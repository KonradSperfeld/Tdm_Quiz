from util.helper import show_current_image,quit_quiz_button
import streamlit as st

class QuestionFinished:
    def __init__(self):
        postfix="Dieses Bild ist echt!"
        if (not st.session_state.last_answer_was_real and st.session_state.last_answer_correct) or (st.session_state.last_answer_was_real and not st.session_state.last_answer_correct):
            postfix="Dieses Bild ist künstlich generiert!"
        if st.session_state.last_answer_correct:
            st.success("Richtig! " + postfix)
        else:
            st.error("Da lagst du leider falsch. " + postfix)
        show_current_image()
        def next_quiz_example():
            st.session_state.quiz_position+=1
            st.session_state.quiz_current_position_finished=False
            if st.session_state.quiz_position>20:
                st.session_state.show_ballons=True

        if st.session_state.quiz_position<20:
            col1,col2,col3,col4 = st.columns([2.3,2,2,8])
            with col1:
                st.button("Weiter zum nächsten Bild!",on_click=next_quiz_example)
            with col2:
                quit_quiz_button()
        else:
            st.button("Zur Auswertung!",on_click=next_quiz_example)
        st.write(f"Für die Beantwortung der Fragen hast du bisher {str(st.session_state.quiz_time//60)} Min. {str(st.session_state.quiz_time%60)} Sek. benötigt.")
        if st.session_state.last_answer_correct:
            st.success("Richtig! " + postfix)
        else:
            st.error("Da lagst du leider falsch. " + postfix)

