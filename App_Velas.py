# Aplicación - Gráfico de Velas 

# Importar Librerías 
import streamlit as st
import yfinance as yf
import plotly.express as px
import plotly.graph_objects as go



# Definición inicial de la App
st.set_page_config(
    page_title = "Gráfico de Velas", 
    page_icon = "📈", 
    layout = "wide")

# Construcción del Dashboard 
st.markdown(
    "<h1 style='text-align: center;'>Gráfico de Velas </h1>",
    unsafe_allow_html = True)

st.markdown(
    "<h2 style='text-align: center;'>💵 Información extraida de Yahoo Finance </h1>",
    unsafe_allow_html = True)


# Variables iterables 
Text_Ticker = st.text_input("Inserta el Ticker", "NVDA")
Ticker = yf.Ticker(Text_Ticker)

Text_Period = st.text_input("Inserta el periodo para descargar datos históricos", "1y")
Text_Granularity = st.text_input("Inserta la Granularidad deseada:", "1d")
DH = Ticker.history(Text_Period, interval = Text_Granularity)



left, space, right = st.columns([3, 1, 4])

with left: 
    News = Ticker.news[1]
    Title = News["content"]["title"]    
    Summary = News["content"]["summary"]  
    st.header(Title)
    st.write(Summary)    

    News = Ticker.news[3]
    Title = News["content"]["title"]    
    Summary = News["content"]["summary"]  
    st.header(Title)
    st.write(Summary)    


with right: 
    fig = go.Figure(go.Candlestick(
        x = DH.index, 
        open = DH["Open"], 
        high = DH["High"], 
        low = DH["Low"], 
        close = DH["Close"]))    

    st.plotly_chart(fig)
    
    st.header("Últimos 7 precios de Cierre")
    st.dataframe(
        DH.tail(7), 
        use_container_width = True, 
        height = 200)




