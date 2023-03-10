import streamlit as st
from datetime import datetime, date, timedelta
import pandas as pd

st.title("Stock Tracking Dashboard")

option = st.sidebar.selectbox("Which Dashboard?", ('FANG', 'INDEX', 'Daily'))

timing = st.sidebar.selectbox("What Timeframe?", ('Daily', 'Weekly', 'Both'))

st.header(option)


if option == "FANG":
    symbols=['SPY', 'QQQ', 'IWM', 'DIA', 'VTI', 'IWO', 'MDY', 'RSP', 'SSO', 'QLD', 'SDS', 'QID', 'TQQQ', 'SQQQ', 'XLK', 'SMH', 'IGV', 'TAN', 'FFTY', 'CIBR', 'WCLD', 'XLF', 'XLE', 'XLP', 'XLV', 'XLI', 'XLK', 'XLU', 'XLY', 'XLB', 'XOP', 'XHB', 'XME', 'OIH', 'XLC', 'ITB', 'PAVE', 'JETS', 'XBI', 'ITB', 'ARKK', 'AAPL', 'AMZN', 'MSFT', 'GOOGL', 'META', 'NFLX', 'NVDA', 'TSLA', 'AMD', 'COST', 'ASML', 'LRCX', 'KLAC', 'ANET', 'PANW', 'AVGO', 'AMAT', 'CAT', 'DE', 'HD', 'CRM', 'WMT', 'FTNT', 'JPM', 'AXP', 'MA', 'V', 'CDNS', 'SNPS', 'BKNG', 'ORLY', 'ADI', 'WDAY', 'LIN', 'ADSK', 'ALGN', 'TTD', 'CRWD', 'FSLR']

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
    symbols=['A', 'AAPL', 'ABBV', 'ABNB', 'ABT', 'ACN', 'ADBE', 'ADI', 'ADM', 'ADP', 'ADSK', 'AEP', 'AFRM', 'AIG', 'AJG', 'ALB', 'ALGN', 'AMAT', 'AMD', 'AMGN', 'AMT', 'AMZN', 'ANSS', 'AON', 'APD', 'APH', 'ASAN', 'ASML', 'ATVI', 'AVGO', 'AVLR', 'AXP', 'AZN', 'AZO', 'BA', 'BAC', 'BDX', 'BIDU', 'BIIB', 'BILL', 'BK', 'BKNG', 'BKR', 'BLK', 'BMY', 'BRK.B', 'BSX', 'C', 'CAH', 'CARR', 'CAT', 'CB', 'CCI', 'CDNS', 'CEG', 'CHTR', 'CI', 'CIBR', 'CL', 'CMC', 'CMCSA', 'CME', 'CMG', 'CNC', 'COF', 'COP', 'COST', 'CPRT', 'CRM', 'CRWD', 'CSCO', 'CSGP', 'CSX', 'CTAS', 'CTSH', 'CTVA', 'CVS', 'CVX', 'D', 'DAL', 'DDOG', 'DE', 'DEN', 'DG', 'DHR', 'DIA', 'DIS', 'DKNG', 'DLR', 'DLTR', 'DOCU', 'DOW', 'DUK', 'DVN', 'DXCM', 'EA', 'EBAY', 'ECL', 'EL', 'ELV', 'EMR', 'ENPH', 'EOG', 'EQIX', 'ETN', 'EW', 'EXC', 'F', 'FANG', 'FAST', 'FCX', 'FDX', 'FFTY', 'FIS', 'FISV', 'FTNT', 'GD', 'GE', 'GFS', 'GILD', 'GIS', 'GM', 'GOOG', 'GOOGL', 'GRMN', 'GS', 'HCA', 'HD', 'HLT', 'HON', 'HPQ', 'HUBS', 'HUM', 'HZNP', 'IBM', 'ICE', 'IDXX', 'IGV', 'ILMN', 'INTC', 'INTU', 'IQV', 'ISRG', 'ITB', 'ITW', 'IWM', 'IWO', 'JCI', 'JD', 'JETS', 'JNJ', 'JPM', 'KDP', 'KHC', 'KLAC', 'KMB', 'KO', 'LCID', 'LHX', 'LIN', 'LLY', 'LMT', 'LOW', 'LRCX', 'LULU', 'MA', 'MAR', 'MARA', 'MCD', 'MCHP', 'MCK', 'MCO', 'MDB', 'MDLZ', 'MDT', 'MDY', 'MELI', 'MET', 'META', 'MMC', 'MMM', 'MNST', 'MO', 'MPC', 'MRK', 'MRNA', 'MRVL', 'MS', 'MSCI', 'MSFT', 'MSI', 'MTCH', 'MU', 'n/a', 'NEE', 'NEM', 'NET', 'NFLX', 'NKE', 'NOC', 'NOW', 'NSC', 'NTAP', 'NTES', 'NUE', 'NVDA', 'NXPI', 'O', 'ODFL', 'OIH', 'OKTA', 'OLED', 'ON', 'ORCL', 'ORLY', 'OXY', 'PANW', 'PAVE', 'PAYC', 'PAYX', 'PCAR', 'PCTY', 'PDD', 'PEP', 'PFE', 'PG', 'PGR', 'PH', 'PLD', 'PM', 'PNC', 'PRFT', 'PRU', 'PSA', 'PSX', 'PXD', 'PYPL', 'QCOM', 'QLD', 'QQQ', 'QRVO', 'REGN', 'RIVN', 'RNG', 'ROP', 'ROST', 'RPD', 'RSP', 'RTX', 'SBUX', 'SCHW', 'SDS', 'SGEN', 'SHW', 'SIRI', 'SLB', 'SMH', 'SNAP', 'SNPS', 'SO', 'SPG', 'SPGI', 'SPLK', 'SPT', 'SPY', 'SQQQ', 'SRE', 'SSO', 'STM', 'STZ', 'SWKS', 'SYK', 'SYY', 'T', 'TAN', 'TDG', 'TEAM', 'TEL', 'TER', 'TFC', 'TGT', 'TJX', 'TMO', 'TMUS', 'TQQQ', 'TRV', 'TSCO', 'TSLA', 'TSM', 'TSM ', 'TT', 'TTD', 'TXN', 'UNH', 'UNP', 'UPS', 'USB', 'V', 'VEEV', 'VLO', 'VRSK', 'VRSN', 'VRTX', 'VTI', 'VZ', 'WBA', 'WBA ', 'WBD', 'WCLD', 'WDAY', 'WELL', 'WFC', 'WM', 'WMB', 'WMT', 'XBI', 'XEL', 'XHB', 'XLB', 'XLC', 'XLE', 'XLF', 'XLI', 'XLK', 'XLNX', 'XLP', 'XLU', 'XLV', 'XLY', 'XME', 'XOM', 'XOP', 'ZBRA', 'ZM', 'ZS', 'ZTS']
    #symbols=['SPY', 'QQQ', 'IWM', 'DIA', 'VTI', 'IWO', 'MDY', 'RSP', 'SSO', 'QLD', 'SDS', 'TQQQ', 'SQQQ', 'XLK', 'SMH', 'IGV', 'TAN', 'FFTY', 'CIBR', 'WCLD', 'XLF', 'XLE', 'XLP', 'XLV', 'XLI', 'XLK', 'XLU', 'XLY', 'XLB', 'XOP', 'XHB', 'XME', 'OIH', 'XLC', 'ITB', 'PAVE', 'JETS', 'XBI', 'ITB', 'TNX', 'COP', 'CVX', 'ABBV', 'LLY', 'COST', 'EXC', 'XOM', 'UNH', 'PFE', 'TSLA', 'CVS', 'NVDA', 'BMY', 'AAPL', 'TMO', 'AVGO', 'KO', 'AXP', 'SCHW', 'PEP', 'DHR', 'PG', 'WMT', 'JNJ', 'ACN', 'GOOGL', 'MSFT', 'F', 'UNP', 'TGT', 'MCD', 'AMGN', 'AMT', 'WFC', 'TMUS', 'CSCO', 'ABT', 'UPS', 'DOW', 'ORCL', 'CAT', 'V', 'LOW', 'MS', 'BAC', 'MA', 'GILD', 'AMZN', 'TXN', 'QCOM', 'HD', 'COF', 'BKNG', 'NKE', 'GS', 'BLK', 'JPM', 'HON', 'CHTR', 'CRM', 'ADBE', 'INTC', 'DIS', 'BA', 'FDX', 'META', 'SBUX', 'NFLX', 'PANW', 'DLTR', 'FTNT', 'REGN', 'AZN', 'VRTX', 'PAYX', 'ORLY', 'DDOG', 'ADP', 'AEP', 'CTAS', 'DXCM', 'VRSK', 'SNPS', 'MRVL', 'CTSH', 'FAST', 'LULU', 'AMD', 'CDNS', 'INTU', 'CSX', 'ZS', 'VRSN', 'SPLK', 'CRWD', 'ISRG', 'KLAC', 'TEAM', 'ADI', 'IDXX', 'CPRT', 'ABNB', 'ODFL', 'ILMN', 'NTES', 'WDAY', 'ATVI', 'ASML', 'AMAT', 'FISV', 'MCHP', 'MU', 'ANSS', 'NXPI', 'MRNA', 'LRCX', 'ADSK', 'MTCH', 'MELI', 'SWKS', 'ALGN', 'OKTA', 'PYPL', 'GOOG', 'BRK.B', 'MRK', 'VZ', 'CMCSA', 'LIN', 'PM', 'T', 'NEE', 'RTX', 'MDT', 'SPGI', 'IBM', 'LMT', 'C', 'DE', 'MO', 'NOW', 'PLD', 'CB', 'MDLZ', 'CI', 'DUK', 'GE', 'MMM', 'CCI', 'MMC', 'ZTS', 'SO', 'EOG', 'SYK', 'TJX', 'PNC', 'BDX', 'CME', 'USB', 'PGR', 'NOC', 'D', 'SLB', 'SHW', 'CL', 'TFC', 'FIS', 'PXD', 'EW', 'OXY', 'EQIX', 'WM', 'AON', 'MPC', 'ITW', 'HUM', 'EL', 'BSX', 'FCX', 'NSC', 'ICE', 'GM', 'ETN', 'APD', 'NEM', 'VLO', 'SRE', 'DG', 'EMR', 'GD', 'HCA', 'PSA', 'MCK', 'MCO', 'ADM', 'CNC', 'AIG', 'DVN', 'MET', 'PSX', 'LHX', 'MAR', 'ROP', 'CTVA', 'WMB', 'KMB', 'SYY', 'TRV', 'APH', 'AZO', 'TEL', 'GIS', 'IQV', 'HPQ', 'WBD', 'ECL', 'XEL', 'STZ', 'DLR', 'PRU', 'HLT', 'A', 'CMG', 'WELL', 'O', 'EA', 'KDP', 'MNST', 'KHC', 'WBA', 'BIDU', 'LCID', 'JD', 'ROST', 'BIIB', 'PCAR', 'EBAY', 'ZM', 'SGEN', 'SIRI', 'CEG', 'PDD', 'DOCU', 'ALB', 'CMC', 'DAL', 'TSM', 'WBA', 'CAH', 'DEN', 'TSM', 'STM', 'QRVO', 'TER', 'ON', 'OLED', 'SNAP', 'TTD', 'HUBS', 'NET', 'RNG', 'NTAP', 'ASAN', 'BILL', 'AFRM', 'PCTY', 'SPT', 'PRFT', 'PAYC', 'MARA', 'RPD', 'GRMN', 'MDB', 'ZBRA', 'HZNP', 'VEEV', 'TSCO', 'DKNG', 'ENPH']


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


