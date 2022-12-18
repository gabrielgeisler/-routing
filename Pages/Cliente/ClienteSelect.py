import streamlit as st
import Controllers.ClienteController as ClienteController
import Pages.Cliente.ClienteSelect as PaceClienteSelect
import streamlit.components.v1 as components
import requests

API_KEY = "AIzaSyCb9eryJMdKYEKQOAyE6wJF4JCIrEtc2tU"

def ListCliente():
    st.title("Roteirizar")
    clienteSelecionado = st.selectbox('Selecionar Cliente', ClienteController.SelecionarTodosClientes())
    depositoSelecionado = st.selectbox('Selecionar Deposito', ClienteController.SelecionarTodosDepositos())
    if clienteSelecionado == depositoSelecionado:
        st.warning('Favor informar depósitos distintos', icon="⚠️")
    else:
        def CatchLatLong():
            origem = ClienteController.SelecionarLatLongOrigem(clienteSelecionado)
            destino = ClienteController.SelecionarLatLongDestino(depositoSelecionado)

            url = f"https://maps.googleapis.com/maps/api/distancematrix/json?origins={origem[0]}%2C{origem[1]}&destinations={destino[0]}%2C{destino[1]}&units=metric&key={API_KEY}"
            payload={}
            headers = {}
            response = requests.request("GET", url, headers=headers, data=payload)
            data = response.json()
            distanciaTrajeto = data["rows"][0]["elements"][0]["distance"]["text"]

            latLongOrigem = origem[0] + origem[1]
            latLongDestino = destino[0] + destino[1]
            components.iframe(f"https://www.google.com/maps/embed/v1/directions?key={API_KEY}&origin={latLongOrigem}&destination={latLongDestino}&zoom=15", width=703, height=703 )
            
            st.write("Distância do depósito para o cliente: " + distanciaTrajeto)    
            
        st.button("Roteirizar", on_click=CatchLatLong, disabled=False)