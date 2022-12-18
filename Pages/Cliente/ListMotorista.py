import streamlit as st
import Controllers.ClienteController as ClienteController
import Pages.Cliente.Motorista as PageMotorista
import streamlit.components.v1 as components


def ListMotorista():
    params = st.experimental_get_query_params()
    if params.get("id") == None:
        st.experimental_set_query_params()
        colms = st.columns((1, 2, 1, 2, 1, 1, 1))
        campos = ['ID', 'Nome Motorista', 'Placa', 'Início', 'Fim', 'Excluir', 'Alterar']
        for col, campo_nome in zip(colms, campos):
            col.write(campo_nome)

        for x, item in enumerate(ClienteController.SelecionarTodosMotoristas()):
            col1, col2, col3, col4, col5, col6, col7 = st.columns((1, 2, 1, 2, 1, 1, 1))
            col1.write(item.id)
            col2.write(item.nome)
            col3.write(item.placa)
            col4.write(item.inicio.replace(':00.0000000', ''))
            col5.write(item.fim.replace(':00.0000000', ''))
            button_space_excluir = col6.empty()
            on_click_excluir = button_space_excluir.button(
                'Excluir', 'btnExcluir' + str(item.id))
            button_space_alterar = col7.empty()
            on_click_alterar = button_space_alterar.button(
                'Alterar', 'btnAlterar' + str(item.id))
            
            if on_click_excluir:
                ClienteController.ExcluirMotorista(item.id)
                st.experimental_rerun()
            if on_click_alterar:
                st.experimental_set_query_params(
                    id=[item.id]
                )
                st.experimental_rerun()

                
            
    else:
        on_click_voltar = st.button("Voltar")
        if on_click_voltar:
            st.experimental_set_query_params()
            st.experimental_rerun()
        PageMotorista.CreateMotorista()