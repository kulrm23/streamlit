import streamlit as st
from datetime import datetime, date, timedelta
import pandas as pd

st.title("Stock Tracking Dashboard")

option = st.sidebar.selectbox("Watchlist?", ('Daily_review', 'CURRENT', 'ETF', 'DWM'))

timing = st.sidebar.selectbox("What Timeframe?", ('Daily', 'Weekly', 'Multi'))

st.header(option)


if option == "Daily_review":
    symbols=['SPY', 'QQQ', 'IWM', 'DIA', 'VTI', 'IWO', 'MDY', 'RSP', 'QQQE', 'SDS', 'XLK', 'SMH', 'IGV', 'TAN', 'IYW', 'QTEC', 'FFTY', 'VGT', 'CIBR', 'SKYY', 'AIQ', 'BOTZ', 'IBIT', 'AAPL', 'AMZN', 'MSFT', 'GOOGL', 'META', 'NFLX', 'NVDA', 'TSLA', 'AMD', 'COST', 'ADBE', 'NOW', 'AVGO', 'ASML', 'LRCX', 'KLAC', 'AMAT', 'TSM', 'PANW', 'CRWD', 'ZS', 'DDOG', 'SMCI', 'XLF', 'XLE', 'XLP', 'XLV', 'XLI', 'XLK', 'XLU', 'XLY', 'XLB', 'XOP', 'XHB', 'XME', 'OIH', 'XLC', 'ITB', 'PAVE', 'JETS', 'XBI', 'ARKK', 'ARKW', 'ARKF']

    if timing == "Daily":
        for stock in symbols:
            st.image(f"https://charts2-node.finviz.com/chart.ashx?cs=l&t={stock}&tf=d&s=linear&ct=candle_stick&o[0][ot]=sma&o[0][op]=50&o[0][oc]=FF8F33C6&o[1][ot]=ema&o[1][op]=10&o[1][oc]=DCB3326D&o[2][ot]=ema&o[2][op]=21&o[2][oc]=DC32B363&o[3][ot]=patterns&o[3][op]=&o[3][oc]=000")

    if timing == "Weekly":
        for stock in symbols:
            st.image(f"https://charts2-node.finviz.com/chart.ashx?cs=l&t={stock}&tf=w&s=linear&ct=candle_stick&o[0][ot]=sma&o[0][op]=40&o[0][oc]=FF8F33C6&o[1][ot]=sma&o[1][op]=30&o[1][oc]=DCB3326D&o[2][ot]=sma&o[2][op]=10&o[2][oc]=DC32B363&o[3][ot]=patterns&o[3][op]=&o[3][oc]=000")

    if timing == "Multi":
        for stock in symbols:
            st.image(f"https://charts2-node.finviz.com/chart.ashx?cs=l&t={stock}&tf=m&s=linear&ct=candle_stick&o[0][ot]=sma&o[0][op]=5&o[0][oc]=FF8F33C6&o[1][ot]=sma&o[1][op]=10&o[1][oc]=DCB3326D&o[2][ot]=sma&o[2][op]=20&o[2][oc]=DC32B363&o[3][ot]=patterns&o[3][op]=&o[3][oc]=000")
            st.image(f"https://charts2-node.finviz.com/chart.ashx?cs=l&t={stock}&tf=w&s=linear&ct=candle_stick&o[0][ot]=sma&o[0][op]=40&o[0][oc]=FF8F33C6&o[1][ot]=sma&o[1][op]=30&o[1][oc]=DCB3326D&o[2][ot]=sma&o[2][op]=10&o[2][oc]=DC32B363&o[3][ot]=patterns&o[3][op]=&o[3][oc]=000")
            st.image(f"https://charts2-node.finviz.com/chart.ashx?cs=l&t={stock}&tf=d&s=linear&ct=candle_stick&o[0][ot]=sma&o[0][op]=50&o[0][oc]=FF8F33C6&o[1][ot]=ema&o[1][op]=10&o[1][oc]=DCB3326D&o[2][ot]=ema&o[2][op]=21&o[2][oc]=DC32B363&o[3][ot]=patterns&o[3][op]=&o[3][oc]=000")


if option == "CURRENT":
    with open('daily') as f:
        symbols=[i.strip() for i in f.readlines()]

    if timing == "Daily":
        for stock in symbols:
            st.image(f"https://charts2-node.finviz.com/chart.ashx?cs=l&t={stock}&tf=d&s=linear&ct=candle_stick&o[0][ot]=sma&o[0][op]=50&o[0][oc]=FF8F33C6&o[1][ot]=ema&o[1][op]=10&o[1][oc]=DCB3326D&o[2][ot]=ema&o[2][op]=21&o[2][oc]=DC32B363&o[3][ot]=patterns&o[3][op]=&o[3][oc]=000")


    if timing == "Weekly":
        for stock in symbols:
            st.image(f"https://charts2-node.finviz.com/chart.ashx?cs=l&t={stock}&tf=w&s=linear&ct=candle_stick&o[0][ot]=sma&o[0][op]=40&o[0][oc]=FF8F33C6&o[1][ot]=sma&o[1][op]=30&o[1][oc]=DCB3326D&o[2][ot]=sma&o[2][op]=10&o[2][oc]=DC32B363&o[3][ot]=patterns&o[3][op]=&o[3][oc]=000")

    if timing == "Multi":
        for stock in symbols:
            st.image(f"https://charts2-node.finviz.com/chart.ashx?cs=l&t={stock}&tf=m&s=linear&ct=candle_stick&o[0][ot]=sma&o[0][op]=5&o[0][oc]=FF8F33C6&o[1][ot]=sma&o[1][op]=10&o[1][oc]=DCB3326D&o[2][ot]=sma&o[2][op]=20&o[2][oc]=DC32B363&o[3][ot]=patterns&o[3][op]=&o[3][oc]=000")
            st.image(f"https://charts2-node.finviz.com/chart.ashx?cs=l&t={stock}&tf=w&s=linear&ct=candle_stick&o[0][ot]=sma&o[0][op]=40&o[0][oc]=FF8F33C6&o[1][ot]=sma&o[1][op]=30&o[1][oc]=DCB3326D&o[2][ot]=sma&o[2][op]=10&o[2][oc]=DC32B363&o[3][ot]=patterns&o[3][op]=&o[3][oc]=000")
            st.image(f"https://charts2-node.finviz.com/chart.ashx?cs=l&t={stock}&tf=d&s=linear&ct=candle_stick&o[0][ot]=sma&o[0][op]=50&o[0][oc]=FF8F33C6&o[1][ot]=ema&o[1][op]=10&o[1][oc]=DCB3326D&o[2][ot]=ema&o[2][op]=21&o[2][oc]=DC32B363&o[3][ot]=patterns&o[3][op]=&o[3][oc]=000")



if option == "ETF":
    with open('etf') as f:
        symbols=[i.strip() for i in f.readlines()]
        symbols = list(dict.fromkeys(symbols))

    if timing == "Daily":
        for stock in symbols:
            st.image(f"https://charts2-node.finviz.com/chart.ashx?cs=l&t={stock}&tf=d&s=linear&ct=candle_stick&o[0][ot]=sma&o[0][op]=50&o[0][oc]=FF8F33C6&o[1][ot]=ema&o[1][op]=10&o[1][oc]=DCB3326D&o[2][ot]=ema&o[2][op]=21&o[2][oc]=DC32B363&o[3][ot]=patterns&o[3][op]=&o[3][oc]=000")


    if timing == "Weekly":
        for stock in symbols:
            st.image(f"https://charts2-node.finviz.com/chart.ashx?cs=l&t={stock}&tf=w&s=linear&ct=candle_stick&o[0][ot]=sma&o[0][op]=40&o[0][oc]=FF8F33C6&o[1][ot]=sma&o[1][op]=30&o[1][oc]=DCB3326D&o[2][ot]=sma&o[2][op]=10&o[2][oc]=DC32B363&o[3][ot]=patterns&o[3][op]=&o[3][oc]=000")

    if timing == "Multi":
        for stock in symbols:
            st.image(f"https://charts2-node.finviz.com/chart.ashx?cs=l&t={stock}&tf=m&s=linear&ct=candle_stick&o[0][ot]=sma&o[0][op]=5&o[0][oc]=FF8F33C6&o[1][ot]=sma&o[1][op]=10&o[1][oc]=DCB3326D&o[2][ot]=sma&o[2][op]=20&o[2][oc]=DC32B363&o[3][ot]=patterns&o[3][op]=&o[3][oc]=000")
            st.image(f"https://charts2-node.finviz.com/chart.ashx?cs=l&t={stock}&tf=w&s=linear&ct=candle_stick&o[0][ot]=sma&o[0][op]=40&o[0][oc]=FF8F33C6&o[1][ot]=sma&o[1][op]=30&o[1][oc]=DCB3326D&o[2][ot]=sma&o[2][op]=10&o[2][oc]=DC32B363&o[3][ot]=patterns&o[3][op]=&o[3][oc]=000")
            st.image(f"https://charts2-node.finviz.com/chart.ashx?cs=l&t={stock}&tf=d&s=linear&ct=candle_stick&o[0][ot]=sma&o[0][op]=50&o[0][oc]=FF8F33C6&o[1][ot]=ema&o[1][op]=10&o[1][oc]=DCB3326D&o[2][ot]=ema&o[2][op]=21&o[2][oc]=DC32B363&o[3][ot]=patterns&o[3][op]=&o[3][oc]=000")

if option == "DWM":
    stock = st.text_input('Type the stock ticker:')
    st.write(stock.upper())

            st.image(f"https://charts2-node.finviz.com/chart.ashx?cs=l&t={stock}&tf=m&s=linear&ct=candle_stick&o[0][ot]=sma&o[0][op]=5&o[0][oc]=FF8F33C6&o[1][ot]=sma&o[1][op]=10&o[1][oc]=DCB3326D&o[2][ot]=sma&o[2][op]=20&o[2][oc]=DC32B363&o[3][ot]=patterns&o[3][op]=&o[3][oc]=000")
            st.image(f"https://charts2-node.finviz.com/chart.ashx?cs=l&t={stock}&tf=w&s=linear&ct=candle_stick&o[0][ot]=sma&o[0][op]=40&o[0][oc]=FF8F33C6&o[1][ot]=sma&o[1][op]=30&o[1][oc]=DCB3326D&o[2][ot]=sma&o[2][op]=10&o[2][oc]=DC32B363&o[3][ot]=patterns&o[3][op]=&o[3][oc]=000")
            st.image(f"https://charts2-node.finviz.com/chart.ashx?cs=l&t={stock}&tf=d&s=linear&ct=candle_stick&o[0][ot]=sma&o[0][op]=50&o[0][oc]=FF8F33C6&o[1][ot]=ema&o[1][op]=10&o[1][oc]=DCB3326D&o[2][ot]=ema&o[2][op]=21&o[2][oc]=DC32B363&o[3][ot]=patterns&o[3][op]=&o[3][oc]=000")
