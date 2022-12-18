import this
from turtle import onclick
import streamlit as st;
import Controllers.ClienteController as ClienteController
import models.Cliente as cliente
import Pages.Cliente.List as PageListCliente


def Create():
    idAlteracao = st.experimental_get_query_params()
    clienteRecuperado = None
    if idAlteracao.get("id") != None:
        idAlteracao = idAlteracao.get("id")[0]
        clienteRecuperado = ClienteController.SelecionarById(idAlteracao)
        st.experimental_set_query_params(
            id=[clienteRecuperado.id]
        )
        st.title("Alterar cliente")
    else:
        st.title("Incluir cliente")

    with st.form(key="include_cliente"):
        if clienteRecuperado == None:
            input_name = st.text_input(label="Insira o seu nome")
            input_latitude = st.text_input(label="Insira a Latitude")
            input_longitude = st.text_input(label="Insira a Longitude")
        else:
            input_name = st.text_input(label="Insira o seu nome", value=clienteRecuperado.nome)
            input_latitude = st.text_input(label="Insira a Latitude", value=clienteRecuperado.latitude)
            input_longitude = st.text_input(label="Insira a Longitude", value=clienteRecuperado.longitude)
        input_button_submit = st.form_submit_button("Enviar")


    if input_button_submit:
        if clienteRecuperado == None:
            ClienteController.Incluir(cliente.Cliente(0, input_name, input_latitude, input_longitude))
            st.success("Cliente incluido com sucesso!")
        else:
            st.experimental_set_query_params()
            ClienteController.Alterar(cliente.Cliente(clienteRecuperado.id, input_name, input_latitude, input_longitude))
            st.success("Cliente alterado com sucesso!")
        
        