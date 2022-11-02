import streamlit as st
import numpy as np
import joblib

st.set_page_config(page_title = 'Aplicação web') # Muda o nome da página que aparece lá encima nas abas
modelo = joblib.load('regressao_linear.pkl')

def homepage():
    st.markdown("# Objetivo:")
    st.text('O objetivo dessa aplicação web é praticar o novos conhecimentos adquiridos sobre streamlit para futuramente aprender a realizar um deploy em cloud !')

def previsao():
    st.markdown("# Previsão:")
    codigo_loja = int(st.number_input('Qual o código da sua loja ?'))
    if codigo_loja != 0:
        st.success(f'O código da sua loja é: {str(codigo_loja)}')
    else:
        st.error('Digite o código da loja !')
    
    opcao_feriado = ['Sim', 'Não']
    feriado = st.selectbox('É feriado ?', opcao_feriado) # Cria uma caixa com uma lista suspensa
    st.write('Você selecionou que é feriado? ', feriado) # Mostra a opção selecionada
    if feriado == 'Sim':
        feriado = 1
    else:
        feriado = 0
    
    temperatura = int(st.number_input('Digite a temperatura em fahrenheit ?'))
    if temperatura != 0:    
        st.success(f'A temperatura foi de: {str(temperatura)} fahrenheit')
    else:
        st.error('Digite a temperatura da semana!')

    preco_gas = st.number_input('Digite o preço da gasolina ?')
    if preco_gas != 0:    
        st.success(f'O preço foi de: {str(preco_gas)}')
    else:
        st.error('Digite o preço da gasolina!')

    taxa = st.number_input('Digite a taxa de inflação ?')
    if taxa != 0:    
        st.success(f'A taxa foi de: {str(taxa)}')
    else:
        st.error('Digite a taxa de inflação!')

    desemprego = st.number_input('Digite a taxa de desemprego ?')
    if desemprego != 0:    
        st.success(f'A taxa foi de: {str(desemprego)}')
    else:
        st.error('Digite a taxa de desemprego!')

    lista = [codigo_loja, feriado, temperatura, preco_gas,
     taxa, desemprego]

    array = np.array(lista)

    if st.button('Calcular previsão: '):
        prev = modelo.predict(array.reshape(1, -1))
        st.success(f'A previsão do faturamento foi de: {prev}')

def main():
    options = ['Pagina inicial', 'Previsão']
    # Cria um menu suspenso com as opções do "options"
    page_option = st.sidebar.selectbox('Options', options)
    
    if page_option == 'Pagina inicial':
        homepage()
    else:
        previsao()

main()