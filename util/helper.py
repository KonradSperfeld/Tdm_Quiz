import os
from PIL import Image

import streamlit as st

module_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

@st.cache(allow_output_mutation=True)
def load_logo_images():
    neiss_logo = Image.open(os.path.join(module_path, "images","logos", "neiss_logo_nn_pentagon01b2.png"))
    eu_fonds = Image.open(os.path.join(module_path, "images", "logos","logo_EU_Fonds.png"))
    eu_esf = Image.open(os.path.join(module_path, "images", "logos", "logo_EU_ESF.png"))
    mv_bm = Image.open(os.path.join(module_path, "images", "logos", "logo_MV_BM.png"))
    return neiss_logo, eu_fonds, eu_esf, mv_bm
