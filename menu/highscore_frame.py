import streamlit as st
from util.helper import get_highscore,hs_attr_name,hs_attr_time,hs_attr_correct_answers

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
        st.markdown(self.build_highscore_table_string())

    def build_highscore_table_string(self):
        highscore=get_highscore()
        tablestring = (
            "Platzierung | Name | Richtige Antworten | Benötigte Zeit \n -----|-----|-------|-------"
        )
        rank_number=0
        for element in highscore:
            rank_number+=1
            tablestring+=(
                "\n"
                + str(rank_number)
                + " | "
                + element[hs_attr_name]
                + " | "
                + str(element[hs_attr_correct_answers])
                + " | "
                + f'{str(element[hs_attr_time]//60)} Min. {str(element[hs_attr_time]%60)} Sek.'
            )
        return tablestring

