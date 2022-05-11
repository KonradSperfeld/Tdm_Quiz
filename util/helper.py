import os
from PIL import Image

import streamlit as st

module_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
r="real"
f="fake"
solutionList=[None,r,f,f,r,f,r,r,f,r,f,f,r,f,f,r,f,r,r,f,r]

@st.cache(allow_output_mutation=True)
def load_logo_images():
    neiss_logo = Image.open(os.path.join(module_path, "images","logos", "neiss_logo_nn_pentagon01b2.png"))
    eu_fonds = Image.open(os.path.join(module_path, "images", "logos","logo_EU_Fonds.png"))
    eu_esf = Image.open(os.path.join(module_path, "images", "logos", "logo_EU_ESF.png"))
    mv_bm = Image.open(os.path.join(module_path, "images", "logos", "logo_MV_BM.png"))
    return neiss_logo, eu_fonds, eu_esf, mv_bm

def show_current_image():
    cur_Image=Image.open(os.path.join(module_path, "images","quiz", str(st.session_state.quiz_position)+".jpeg"))
    st.image(cur_Image,width=700)

def is_answer_correct(current_image_is_real):
    if (solutionList[st.session_state.quiz_position]==r and current_image_is_real) or (solutionList[st.session_state.quiz_position]==f and not current_image_is_real):
        return True
    return False

