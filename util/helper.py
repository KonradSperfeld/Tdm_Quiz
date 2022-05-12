import os
from PIL import Image

import streamlit as st
from util.config_io import get_config, set_config

module_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
highscore_filepath = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "util", "highscore.json")
r = "real"
f = "fake"
solutionList = [None, r, f, f, r, f, r, r, f, r, f, f, r, f, f, r, f, r, r, f, r]
hs_attr_name = "name"
hs_attr_time = "time"
hs_attr_correct_answers = "correct_answers"
conf_attr_hs = "highscore"


@st.cache(allow_output_mutation=True)
def load_logo_images():
    neiss_logo = Image.open(os.path.join(module_path, "images", "logos", "neiss_logo_nn_pentagon01b2.png"))
    eu_fonds = Image.open(os.path.join(module_path, "images", "logos", "logo_EU_Fonds.png"))
    eu_esf = Image.open(os.path.join(module_path, "images", "logos", "logo_EU_ESF.png"))
    mv_bm = Image.open(os.path.join(module_path, "images", "logos", "logo_MV_BM.png"))
    return neiss_logo, eu_fonds, eu_esf, mv_bm


def show_current_image():
    cur_Image = Image.open(os.path.join(module_path, "images", "quiz", str(st.session_state.quiz_position) + ".jpeg"))
    st.write(f'Bild Nr {st.session_state.quiz_position}/20');
    st.image(cur_Image, width=700)
    st.text('Quelle: https://www.whichfaceisreal.com/index.php')


def is_answer_correct(current_image_is_real):
    if (solutionList[st.session_state.quiz_position] == r and current_image_is_real) or (
            solutionList[st.session_state.quiz_position] == f and not current_image_is_real):
        return True
    return False


def validate_new_hs_conf_name(hs_conf, new_name):
    if new_name is None or new_name == "":
        st.error(f'Bitte trage einen Namen in das obige Textfeld ein um dich in die Bestenliste einzutragen.')
        return -1
    elif len(new_name)>20:
        st.error(f'Der Name "{new_name}" ist zu lang. Bitte verwende einen Namen mit maximal 20 Zeichen.')
        return -1
    for element in hs_conf["highscore"]:
        if new_name == element[hs_attr_name]:
            st.error(
                f'Der Name "{new_name}" is leider schon vergeben. Bitte wähle einen anderen Namen aus um dich in die Bestenliste einzutragen.')
            return -1
    return 0


def insert_new_highscore_entry(name):
    hs_conf = get_highscore_conf()
    if validate_new_hs_conf_name(hs_conf, name) >= 0:
        insert_index = -1
        insert_index_found = False
        for index in range(len(hs_conf[conf_attr_hs])):
            if not insert_index_found:
                if hs_conf[conf_attr_hs][index][hs_attr_correct_answers] < st.session_state.num_correct_answers or (
                        hs_conf[conf_attr_hs][index][hs_attr_correct_answers] == st.session_state.num_correct_answers and
                        hs_conf[conf_attr_hs][index][hs_attr_time] > st.session_state.quiz_time):
                    insert_index = index
                    insert_index_found = True
        new_hs_element={hs_attr_name:name,hs_attr_correct_answers:st.session_state.num_correct_answers,hs_attr_time:st.session_state.quiz_time}
        if insert_index>=0:
            hs_conf[conf_attr_hs].insert(insert_index,new_hs_element)
        else:
            hs_conf[conf_attr_hs].append(new_hs_element)
        set_config(hs_conf,allow_new=True)
        return 0
    return -1


def get_highscore_conf():
    hs_conf = get_config(highscore_filepath)
    if conf_attr_hs not in hs_conf.keys():
        hs_conf[conf_attr_hs] = []
    return hs_conf

def get_highscore():
    return get_highscore_conf()[conf_attr_hs]
