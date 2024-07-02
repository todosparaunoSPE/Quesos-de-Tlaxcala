# -*- coding: utf-8 -*-
"""
Created on Tue Jul  2 10:27:28 2024

@author: jperezr
"""

import streamlit as st

def main():
    st.title('Quesos de Tlaxcala, Tlax.')
    st.subheader('Precios')

    precios = {
        "Queso Oaxaca 1K": 150,
        "Queso Oaxaca 1/2 k": 80,
        "Queso Panela 1K": 150,
        "Queso Panela 1/2 K": 80,
        "Queso Botanero 1K": 200,
        "Queso Botanero 1/2 k": 100,
        "Requeson 1kg": 100,
        "Requeson 1/2 K": 60,
        "Queso Fresco redondo 3 piezas": 120,
        "Tlacoyos de requeson con chicharron 1 docena": 100,
        "Tlacoyos solo requeson 1 docena": 100
    }

    for producto, precio in precios.items():
        st.header(f"{producto}: ${precio}")

    st.sidebar.title("Informes")
    st.sidebar.write("Javier Horacio Pérez Ricárdez")
    st.sidebar.write("WhatsApp-1: +52 55 7425 5593")
    st.sidebar.write("WhatsApp-2: +52 99 3291 3812")
    st.sidebar.write("WhatsApp-3: +52 24 6159 3018") 
    st.sidebar.markdown("---")
    st.sidebar.write("© 2024 Quesos de Tlaxcala, Tlax. Todos los derechos reservados.")

if __name__ == "__main__":
    main()
