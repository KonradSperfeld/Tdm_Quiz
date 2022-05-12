from util.helper import show_current_image,is_answer_correct,quit_quiz_button
import streamlit as st
import asyncio

class Question:
    def __init__(self):
        st.write('## Ist das Bild echt oder ein Deep Fake?')
        show_current_image()
        def answer(is_real):
            st.session_state.last_answer_correct=is_answer_correct(is_real)
            if is_answer_correct(is_real):
                st.session_state.num_correct_answers+=1
            st.session_state.last_answer_was_real=is_real
            st.session_state.quiz_current_position_finished=True
        col1, col2, col3, col4=st.columns([1.5,2.5,2,8])
        col1.button("Das Bild ist Echt!",on_click=answer,args=(True,))
        col2.button("Das Bild ist künstlich generiert!",on_click=answer,args=(False,))
        with col3:
            quit_quiz_button()
        async def watch(time_frame):
            while st.session_state.quiz_running and not st.session_state.quiz_current_position_finished:
                time_frame.write(f"Für die Beantwortung der Fragen hast du bisher  {str(st.session_state.quiz_time//60)} Min. {str(st.session_state.quiz_time%60)} Sek. benötigt.")
                r = await asyncio.sleep(1)
                st.session_state.quiz_time+=1
        st.info("Klicke auf die richtige Antwort!")
        time_frame=st.empty()
        asyncio.run(watch(time_frame))

