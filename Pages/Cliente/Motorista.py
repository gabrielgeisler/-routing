import this
from turtle import onclick
import streamlit as st;
import Controllers.ClienteController as ClienteController
import models.Motorista as motorista
import Pages.Cliente.List as PageListCliente


def CreateMotorista():
    idAlteracao = st.experimental_get_query_params()
    motoristaRecuperado = None
    if idAlteracao.get("id") != None:
        idAlteracao = idAlteracao.get("id")[0]
        motoristaRecuperado = ClienteController.SelecionarMotoristaById(idAlteracao)
        st.experimental_set_query_params(
            id=[motoristaRecuperado.id]
        )
        st.title("Alterar Motorista")
    else:
        st.title("Cadastrar Motorista")

    with st.form(key="include_cliente"):
        
        if motoristaRecuperado == None:
            depositoSelecionado = st.selectbox('Selecionar Deposito', ClienteController.SelecionarTodosDepositos())
            input_name = st.text_input(label="Insira o seu nome do Motorista")
            input_placa = st.text_input(label="Insira a placa do veículo")
            col1, col2 = st.columns((1, 1))
            input_horario_inicio = col1.time_input(label="Insira o horário de início de jornada do motorista")
            input_horario_fim = col2.time_input(label="Insira o horário de término de jornada do motorista")
        else:
            input_name = st.text_input(label="Insira o seu nome do Motorista", value=motoristaRecuperado.nome)
            input_placa = st.text_input(label="Insira a Longitude", value=motoristaRecuperado.input_placa)
            input_horario_inicio = st.time_input(label="Insira a placa do veículo", value=motoristaRecuperado.input_horario_inicio)
            input_horario_fim = st.time_input   (label="Insira a placa do veículo", value=motoristaRecuperado.input_horario_fim)
            
        input_button_submit = st.form_submit_button("Enviar")


    if input_button_submit:
        if motoristaRecuperado == None:
            idDeposito = ClienteController.EncontrarIdDeposito(depositoSelecionado)
            ClienteController.IncluirMotorista(motorista.Motorista(0, input_name, input_placa, input_horario_inicio, input_horario_fim, idDeposito))
            st.success("Motorista incluido com sucesso!")
        else:
            st.experimental_set_query_params()
            ClienteController.AlterarMotorista(motorista.Motorista(motoristaRecuperado.id, input_name, input_placa, input_horario_inicio, input_horario_fim, idDeposito))
            st.success("Motorista alterado com sucesso!")
        
        