import streamlit as st
from datetime import datetime, date, timedelta
import pandas as pd

st.title("Stock Tracking Dashboard")

option = st.sidebar.selectbox("Which Dashboard?", ('FANG', 'INDEX', 'Daily'))

timing = st.sidebar.selectbox("What Timeframe?", ('Daily', 'Weekly', 'Both'))

st.header(option)


if option == "FANG":
    symbols=['SPY', 'QQQ', 'DIA', 'IWM', 'VTI', 'VIXY', 'XLK','SMH', 'IGV', 'TAN', 'TLT', 'ARKK', 'FFTY', 'SQQQ', 'TQQQ', 'SSO', 'UPRO', 'QLD', 'SPXL', 'SOXL',
             'TECL', 'TNA', 'UDOW', 'ERX', 'FAS', 'LABU', 'NUGT', 'JNUG', 'GUSH',
             'XLK', 'XLY', 'XLP', 'XLRE', 'XLE', 'XLV', 'XLB', 'XLI', 'XLF', 'XLU', 'XLC', 'XHB', 'XSW', 'XSD', 'KRE', 'XME', 'XRT','XOP', 'GLD', 'KBE',
             'AAPL', 'AMZN', 'MSFT', 'GOOGL', 'META', 'NFLX', 'NVDA', 'TSLA', 'ADBE', 'NOW', 'CRM', 'TEAM', 'ASML', 'LRCX', 'AMAT', 'AMD', 'TSM', 'MU',
             'FTNT', 'TTD',  'COST', 'HD', 'INTU', 'ISRG', 'SNPS', 'ACN', 'ABNB','SNOW', 'DDOG', 'RBLX', 'MDB', 'CRWD', 'NET', 'APPS', 'SHOP', 'ETSY',
             'OKTA', 'ZS', 'PANW', 'ANET', 'JNPR', 'TWLO', 'ROKU', 'U', 'DOCU', 'ZM', 'UBER']

    if timing == "Daily":
        for stock in symbols:
            st.image(f"https://charts2-node.finviz.com/chart.ashx?cs=l&t={stock}&tf=d&s=linear&ct=candle_stick&o[0][ot]=sma&o[0][op]=50&o[0][oc]=FF8F33C6&o[1][ot]=sma&o[1][op]=10&o[1][oc]=DCB3326D&o[2][ot]=sma&o[2][op]=20&o[2][oc]=DC32B363&o[3][ot]=patterns&o[3][op]=&o[3][oc]=000")

    if timing == "Weekly":
        for stock in symbols:
            st.image(f"https://charts2-node.finviz.com/chart.ashx?cs=l&t={stock}&tf=w&s=linear&ct=candle_stick&o[0][ot]=sma&o[0][op]=40&o[0][oc]=FF8F33C6&o[1][ot]=sma&o[1][op]=30&o[1][oc]=DCB3326D&o[2][ot]=sma&o[2][op]=10&o[2][oc]=DC32B363&o[3][ot]=patterns&o[3][op]=&o[3][oc]=000")

    if timing == "Both":
        for stock in symbols:
            st.image(f"https://charts2-node.finviz.com/chart.ashx?cs=l&t={stock}&tf=d&s=linear&ct=candle_stick&o[0][ot]=sma&o[0][op]=50&o[0][oc]=FF8F33C6&o[1][ot]=sma&o[1][op]=10&o[1][oc]=DCB3326D&o[2][ot]=sma&o[2][op]=20&o[2][oc]=DC32B363&o[3][ot]=patterns&o[3][op]=&o[3][oc]=000")
            st.image(f"https://charts2-node.finviz.com/chart.ashx?cs=l&t={stock}&tf=w&s=linear&ct=candle_stick&o[0][ot]=sma&o[0][op]=40&o[0][oc]=FF8F33C6&o[1][ot]=sma&o[1][op]=30&o[1][oc]=DCB3326D&o[2][ot]=sma&o[2][op]=10&o[2][oc]=DC32B363&o[3][ot]=patterns&o[3][op]=&o[3][oc]=000")

if option == "INDEX":
    symbols=['SPY', 'QQQ', 'IWM', 'DIA', 'VTI', 'IWO', 'MDY', 'RSP', 'SSO', 'QLD', 'SDS', 'TQQQ', 'SQQQ', 'XLK', 'SMH', 'IGV', 'TAN', 'FFTY', 'CIBR', 'WCLD', 'XLF', 'XLE', 'XLP', 'XLV', 'XLI', 'XLK', 'XLU', 'XLY', 'XLB', 'XOP', 'XHB', 'XME', 'OIH', 'XLC', 'ITB', 'PAVE', 'JETS', 'XBI', 'ITB', 'TNX', 'COP', 'CVX', 'ABBV', 'LLY', 'COST', 'EXC', 'XOM', 'UNH', 'PFE', 'TSLA', 'CVS', 'NVDA', 'BMY', 'AAPL', 'TMO', 'AVGO', 'KO', 'AXP', 'SCHW', 'PEP', 'DHR', 'PG', 'WMT', 'JNJ', 'ACN', 'GOOGL', 'MSFT', 'F', 'UNP', 'TGT', 'MCD', 'AMGN', 'AMT', 'WFC', 'TMUS', 'CSCO', 'ABT', 'UPS', 'DOW', 'ORCL', 'CAT', 'V', 'LOW', 'MS', 'BAC', 'MA', 'GILD', 'AMZN', 'TXN', 'QCOM', 'HD', 'COF', 'BKNG', 'NKE', 'GS', 'BLK', 'JPM', 'HON', 'CHTR', 'CRM', 'ADBE', 'INTC', 'DIS', 'BA', 'FDX', 'META', 'SBUX', 'NFLX', 'PANW', 'DLTR', 'FTNT', 'REGN', 'AZN', 'VRTX', 'PAYX', 'ORLY', 'DDOG', 'ADP', 'AEP', 'CTAS', 'DXCM', 'VRSK', 'SNPS', 'MRVL', 'CTSH', 'FAST', 'LULU', 'AMD', 'CDNS', 'INTU', 'CSX', 'ZS', 'VRSN', 'SPLK', 'CRWD', 'ISRG', 'KLAC', 'TEAM', 'ADI', 'IDXX', 'CPRT', 'ABNB', 'ODFL', 'ILMN', 'NTES', 'WDAY', 'ATVI', 'ASML', 'AMAT', 'FISV', 'MCHP', 'MU', 'ANSS', 'NXPI', 'MRNA', 'LRCX', 'ADSK', 'MTCH', 'MELI', 'SWKS', 'ALGN', 'OKTA', 'PYPL', 'GOOG', 'BRK.B', 'MRK', 'VZ', 'CMCSA', 'LIN', 'PM', 'T', 'NEE', 'RTX', 'MDT', 'SPGI', 'IBM', 'LMT', 'C', 'DE', 'MO', 'NOW', 'PLD', 'CB', 'MDLZ', 'CI', 'DUK', 'GE', 'MMM', 'CCI', 'MMC', 'ZTS', 'SO', 'EOG', 'SYK', 'TJX', 'PNC', 'BDX', 'CME', 'USB', 'PGR', 'NOC', 'D', 'SLB', 'SHW', 'CL', 'TFC', 'FIS', 'PXD', 'EW', 'OXY', 'EQIX', 'WM', 'AON', 'MPC', 'ITW', 'HUM', 'EL', 'BSX', 'FCX', 'NSC', 'ICE', 'GM', 'ETN', 'APD', 'NEM', 'VLO', 'SRE', 'DG', 'EMR', 'GD', 'HCA', 'PSA', 'MCK', 'MCO', 'ADM', 'CNC', 'AIG', 'DVN', 'MET', 'PSX', 'LHX', 'MAR', 'ROP', 'CTVA', 'WMB', 'KMB', 'SYY', 'TRV', 'APH', 'AZO', 'TEL', 'GIS', 'IQV', 'HPQ', 'WBD', 'ECL', 'XEL', 'STZ', 'DLR', 'PRU', 'HLT', 'A', 'CMG', 'WELL', 'O', 'EA', 'KDP', 'MNST', 'KHC', 'WBA', 'BIDU', 'LCID', 'JD', 'ROST', 'BIIB', 'PCAR', 'EBAY', 'ZM', 'SGEN', 'SIRI', 'CEG', 'PDD', 'DOCU', 'ALB', 'CMC', 'DAL', 'TSM', 'WBA', 'CAH', 'DEN', 'TSM', 'STM', 'QRVO', 'TER', 'ON', 'OLED', 'SNAP', 'TTD', 'HUBS', 'NET', 'RNG', 'NTAP', 'ASAN', 'BILL', 'AFRM', 'PCTY', 'SPT', 'PRFT', 'PAYC', 'MARA', 'RPD', 'GRMN', 'MDB', 'ZBRA', 'HZNP', 'VEEV', 'TSCO', 'DKNG', 'ENPH']


    if timing == "Daily":
        for stock in symbols:
            st.image(f"https://charts2-node.finviz.com/chart.ashx?cs=l&t={stock}&tf=d&s=linear&ct=candle_stick&o[0][ot]=sma&o[0][op]=50&o[0][oc]=FF8F33C6&o[1][ot]=sma&o[1][op]=10&o[1][oc]=DCB3326D&o[2][ot]=sma&o[2][op]=20&o[2][oc]=DC32B363&o[3][ot]=patterns&o[3][op]=&o[3][oc]=000")

    if timing == "Weekly":
        for stock in symbols:
            st.image(f"https://charts2-node.finviz.com/chart.ashx?cs=l&t={stock}&tf=w&s=linear&ct=candle_stick&o[0][ot]=sma&o[0][op]=40&o[0][oc]=FF8F33C6&o[1][ot]=sma&o[1][op]=30&o[1][oc]=DCB3326D&o[2][ot]=sma&o[2][op]=10&o[2][oc]=DC32B363&o[3][ot]=patterns&o[3][op]=&o[3][oc]=000")

    if timing == "Both":
        for stock in symbols:
            st.image(f"https://charts2-node.finviz.com/chart.ashx?cs=l&t={stock}&tf=d&s=linear&ct=candle_stick&o[0][ot]=sma&o[0][op]=50&o[0][oc]=FF8F33C6&o[1][ot]=sma&o[1][op]=10&o[1][oc]=DCB3326D&o[2][ot]=sma&o[2][op]=20&o[2][oc]=DC32B363&o[3][ot]=patterns&o[3][op]=&o[3][oc]=000")
            st.image(f"https://charts2-node.finviz.com/chart.ashx?cs=l&t={stock}&tf=w&s=linear&ct=candle_stick&o[0][ot]=sma&o[0][op]=40&o[0][oc]=FF8F33C6&o[1][ot]=sma&o[1][op]=30&o[1][oc]=DCB3326D&o[2][ot]=sma&o[2][op]=10&o[2][oc]=DC32B363&o[3][ot]=patterns&o[3][op]=&o[3][oc]=000")


if option == "IBD":
    with open('daily') as f:
        symbols=[i.strip() for i in f.readlines()]

    if timing == "Daily":
        for stock in symbols:
            st.image(f"https://finviz.com/chart.ashx?t={stock}")

    if timing == "Weekly":
        for stock in symbols:
            st.image(f"https://finviz.com/chart.ashx?t={stock}&ta=0&ty=c&p=w&s=l", width=None)

    if timing == "Both":
        for stock in symbols:
            st.image(f"https://finviz.com/chart.ashx?t={stock}")
            st.image(f"https://finviz.com/chart.ashx?t={stock}&ta=0&ty=c&p=w&s=l", width=None)


