import streamlit as st
from streamlit_gsheets import GSheetsConnection
import pandas as pd

st.set_page_config(page_title="Radio SLB", page_icon="📻")
st.title("📻 Radio San Luis Beltrán")
st.subheader("Envía tu pedido musical")

conn = st.connection("gsheets", type=GSheetsConnection)

with st.form("pedidos", clear_on_submit=True):
    nombre = st.text_input("Tu Nombre:")
    curso = st.text_input("Tu Curso:")
    cancion = st.text_input("Canción y Artista:")
    enviar = st.form_submit_button("Enviar a Cabina 🚀")

    if enviar:
        if nombre and cancion:
            df = conn.read()
            nuevo = pd.DataFrame([{"Nombre": nombre, "Curso": curso, "Cancion": cancion}])
            df_final = pd.concat([df, nuevo], ignore_index=True)
            conn.update(data=df_final)
            st.success("¡Pedido enviado! Revisa el Excel.")
        else:
            st.error("Faltan datos.")
