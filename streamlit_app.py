import os, streamlit as st

# Set up the Streamlit app
st.title("Stocks App pooo")
symbol = st.text_input("Enter a stock symbol", "AAPL")
if st.button("Get Quote"):
    quote = 45
    st.write(f"The last price for {symbol} is {quote}")
