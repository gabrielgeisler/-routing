import streamlit as st;
import Controllers.ClienteController as ClienteController
import models.Deposito as deposito
import streamlit.components.v1 as components
from streamlit_folium import st_folium
import folium

API_KEY = "AIzaSyCb9eryJMdKYEKQOAyE6wJF4JCIrEtc2tU"

def CreateDeposito():
    idAlteracao = st.experimental_get_query_params()
    depositoRecuperado = None
    if idAlteracao.get("id") != None:
        idAlteracao = idAlteracao.get("id")[0]
        depositoRecuperado = ClienteController.SelecionarByIdDeposito(idAlteracao)
        st.experimental_set_query_params(
            id=[depositoRecuperado.id]
        )
        st.title("Alterar Deposito")
    else:
        st.title("Incluir Deposito")

    with st.form(key="include_deposito"):
        if depositoRecuperado == None:
            input_name = st.text_input(label="Insira o seu nome")
            input_latitude = st.text_input(label="Insira a Latitude")
            input_longitude = st.text_input(label="Insira a Longitude")
            col1, col2 = st.columns((1, 1))
            input_horario_inicio = col1.time_input(label="Insira o horário de início de jornada do motorista")
            input_horario_fim = col2.time_input(label="Insira o horário de término de jornada do motorista")
        else:
            input_name = st.text_input(label="Insira o seu nome", value=depositoRecuperado.nome)
            input_latitude = st.text_input(label="Insira a Latitude", value=depositoRecuperado.latitude)
            input_longitude = st.text_input(label="Insira a Longitude", value=depositoRecuperado.longitude)
            col1, col2 = st.columns((1, 1))
            input_horario_inicio = col1.time_input(label="Insira o horário de início de jornada do motorista")
            input_horario_fim = col2.time_input(label="Insira o horário de término de jornada do motorista")
        input_button_submit = st.form_submit_button("Enviar")
        if input_latitude and input_longitude != '':
            #components.iframe(f"https://www.google.com/maps/embed/v1/place?key={API_KEY}&q={input_latitude},{input_longitude}", width=670, height=670)
            map = folium.Map(location=[input_latitude, input_longitude], tiles="OpenStreetMap", zoom_start=16)
            popup = folium.Popup(f"{input_name}", min_width=100, max_width=100)
            folium.Marker(location=[input_latitude, input_longitude], popup=popup).add_to(map)
            st_folium(map, width=670, height=670) 

    if input_button_submit:
        if input_name == '':
            st.warning('Favor informar um nome para o Depósito.', icon="⚠️")
        elif input_latitude == '':
            st.warning('Favor informar uma Latitude para o Depósito.', icon="⚠️")
        elif input_longitude == '':
            st.warning('Favor informar uma Longitude para o Depósito.', icon="⚠️")
        else:
            if depositoRecuperado == None:
                ClienteController.IncluirDeposito(deposito.Deposito(0, input_name, input_latitude, input_longitude, input_horario_inicio, input_horario_fim))
                st.success("Depósito incluido com sucesso!")
            else:
                st.experimental_set_query_params()
                ClienteController.AlterarDeposito(deposito.Deposito(depositoRecuperado.id, input_name, input_latitude, input_longitude, input_horario_inicio, input_horario_fim))
                st.success("Depósito alterado com sucesso!")

        