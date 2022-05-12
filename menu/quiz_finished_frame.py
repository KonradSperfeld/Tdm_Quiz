import streamlit as st
from util.helper import insert_new_highscore_entry
class QuizFinished:
    def __init__(self):
        if st.session_state.show_ballons:
            st.balloons()
            st.session_state.show_ballons=False
        st.write(f'Geschafft: Du hast {st.session_state.num_correct_answers} von 20 Fragen korrekt beantwort und dafür {str(st.session_state.quiz_time//60)} Min. {str(st.session_state.quiz_time%60)} Sek. benötigt.')

        highscore_name=st.text_input(label="Mit diesem Namen möchte ich in die Bestenliste eingetragen werden")

        col1, col2, col3=st.columns([2,2,6])
        def toHighscoreWithEntry():
            if insert_new_highscore_entry(highscore_name)>=0:
                st.session_state.quiz_running=False
        def toHighscore():
            st.session_state.quiz_running=False
        col1.button("In die Bestenliste eintragen.",on_click=toHighscoreWithEntry)
        col2.button("Nicht in Bestenliste eintragen.",on_click=toHighscore)
        st.info("Wenn du wissen willst, worauf man achten muss um echte Bilder von künstlichen Bildern unterscheiden zu können oder wie in etwa neuronale Netze funktionieren, die solche Deep Fakes erzeugen, frag uns gerne. Normalerweise sitzen wir hier mit im Raum ;-). ")
