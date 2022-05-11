from util.helper import load_logo_images
import streamlit as st

class Main:
    def __init__(self):
        self.sidebar()

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


