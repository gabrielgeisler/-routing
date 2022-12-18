from cgitb import text
from multiprocessing import Value
from os import write
from turtle import onclick, onscreenclick
from typing import List
from numpy.core.fromnumeric import size
import streamlit as st
import Pages.Cliente.Create as PageCreateCliente
import Pages.Cliente.List as PageListCliente
import Pages.Cliente.ListDeposito as PageListDeposito
import Pages.Cliente.CreateDeposito as PageCreateDeposito
import Pages.Cliente.ClienteSelect as PageClienteSelect
import Pages.Cliente.Motorista as PageMotorista
import Pages.Cliente.ListMotorista as PageListMotorista

st.set_page_config(page_title='Routing')

#CONFIGURAÇÕES DA PÁGINA

hide_menu = """<style>
#MainMenu{
    visibility:hidden;
}
footer{
    visibility:hidden;
}
</style>"""
#CONFIGURAÇÕES DA PÁGINA

st.markdown(hide_menu, unsafe_allow_html=True)


Page_cliente = st.sidebar.selectbox(
    'Menu', ['Início', 'Cadastrar Cliente', 'Consultar Clientes', 'Cadastrar Depósito', 'Consultar Depósito', 'Cadastrar Motorista', 'Consultar Motorista'], 0)

if Page_cliente == 'Consultar Clientes':
    PageListCliente.List()
if Page_cliente == 'Cadastrar Cliente':
    st.experimental_set_query_params()
    PageCreateCliente.Create()
    
if Page_cliente == 'Cadastrar Depósito':
    st.experimental_set_query_params()
    PageCreateDeposito.CreateDeposito()
if Page_cliente == 'Consultar Depósito':
    PageListDeposito.ListDeposito()
    
if Page_cliente == 'Início':
    st.experimental_set_query_params()
    PageClienteSelect.ListCliente()
    
if Page_cliente == 'Cadastrar Motorista':
    st.experimental_set_query_params()
    PageMotorista.CreateMotorista()

if Page_cliente == 'Consultar Motorista':
    st.experimental_set_query_params()
    PageListMotorista.ListMotorista()
    