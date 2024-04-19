import streamlit as st
from datetime import datetime, date, timedelta
import pandas as pd

st.set_page_config(
    page_title="Stock Tracking Dashboard",
    page_icon="🧊",
    layout="wide",
    initial_sidebar_state="auto"
)

#st.title("Stock Tracking Dashboard")

option = st.sidebar.selectbox("Watchlist?", ('Daily_review', 'WEEKLY_WL', 'ETF', 'SPQQ100', 'NEW_Daily_review'))

timing = st.sidebar.selectbox("What Timeframe?", ('Daily', 'Weekly', 'Multi'))

st.header(option)


if option == "Daily_review":
    symbols=['SPY', 'QQQ', 'DIA',  'IWO', 'VTI', 'RSP', 'QQQE', 'SDS', 'XLK', 'SMH', 'IGV', 'CIBR', 'VGT', 'TAN', 'FFTY', 'IBIT', 
             'XLF', 'XLE', 'XLP', 'XLV', 'XLI', 'XLK', 'XLC', 'XLU', 'XLY', 'XLB', 'XOP', 'XHB', 'XME', 'OIH', 'ITB', 'PAVE', 'JETS', 'XBI', 'GDX', 'GDXJ',
             'ARKK', 'BLOK', 'AIQ', 'WCLD', 'BOTZ', 'IPAY',  'SOXL', 'SSO', 'QLD', 'TQQQ', 'SQQQ', 'FNGU', 'XLG', 'IVV', 'IJH', 'IJR', 'IDEV', 'IEMG', 'AGG', 'TLT', 'FTEC', 'FDN',
             'AAPL', 'AMZN', 'MSFT', 'GOOGL', 'META', 'NFLX', 'NVDA', 'TSLA', 'AMD', 'COST', 'NOW', 'AVGO', 
             'ASML', 'LRCX', 'AMAT', 'QCOM', 'TSM', 'ARM', 'SMCI', 'ANET', 'PANW', 'CRWD', 'UBER', 'COIN', 'ZS', 
               ]

    if timing == "Daily":
        for stock in symbols:
            st.image(f"https://charts2-node.finviz.com/chart.ashx?cs=l&t={stock}&tf=d&s=linear&ct=candle_stick&o[0][ot]=sma&o[0][op]=50&o[0][oc]=FF8F33C6&o[1][ot]=ema&o[1][op]=10&o[1][oc]=DCB3326D&o[2][ot]=ema&o[2][op]=21&o[2][oc]=DC32B363&o[3][ot]=patterns&o[3][op]=&o[3][oc]=000")

    if timing == "Weekly":
        for stock in symbols:
            st.image(f"https://charts2-node.finviz.com/chart.ashx?cs=l&t={stock}&tf=w&s=linear&ct=candle_stick&o[0][ot]=sma&o[0][op]=40&o[0][oc]=FF8F33C6&o[1][ot]=sma&o[1][op]=30&o[1][oc]=DCB3326D&o[2][ot]=sma&o[2][op]=10&o[2][oc]=DC32B363&o[3][ot]=patterns&o[3][op]=&o[3][oc]=000")
            st.image(f"https://charts2-node.finviz.com/chart.ashx?cs=l&t={stock}&tf=d&s=linear&ct=candle_stick&o[0][ot]=sma&o[0][op]=50&o[0][oc]=FF8F33C6&o[1][ot]=ema&o[1][op]=10&o[1][oc]=DCB3326D&o[2][ot]=ema&o[2][op]=21&o[2][oc]=DC32B363&o[3][ot]=patterns&o[3][op]=&o[3][oc]=000")

    if timing == "Multi":
        for stock in symbols:
            st.image(f"https://charts2-node.finviz.com/chart.ashx?cs=l&t={stock}&tf=m&s=linear&ct=candle_stick&o[0][ot]=sma&o[0][op]=5&o[0][oc]=FF8F33C6&o[1][ot]=sma&o[1][op]=10&o[1][oc]=DCB3326D&o[2][ot]=sma&o[2][op]=20&o[2][oc]=DC32B363&o[3][ot]=patterns&o[3][op]=&o[3][oc]=000")
            st.image(f"https://charts2-node.finviz.com/chart.ashx?cs=l&t={stock}&tf=w&s=linear&ct=candle_stick&o[0][ot]=sma&o[0][op]=40&o[0][oc]=FF8F33C6&o[1][ot]=sma&o[1][op]=30&o[1][oc]=DCB3326D&o[2][ot]=sma&o[2][op]=10&o[2][oc]=DC32B363&o[3][ot]=patterns&o[3][op]=&o[3][oc]=000")
            st.image(f"https://charts2-node.finviz.com/chart.ashx?cs=l&t={stock}&tf=d&s=linear&ct=candle_stick&o[0][ot]=sma&o[0][op]=50&o[0][oc]=FF8F33C6&o[1][ot]=ema&o[1][op]=10&o[1][oc]=DCB3326D&o[2][ot]=ema&o[2][op]=21&o[2][oc]=DC32B363&o[3][ot]=patterns&o[3][op]=&o[3][oc]=000")


if option == "WEEKLY_WL":
    with open('daily') as f:
        symbols=[i.strip() for i in f.readlines()]

    if timing == "Daily":
        for stock in symbols:
            st.image(f"https://charts2-node.finviz.com/chart.ashx?cs=l&t={stock}&tf=d&s=linear&ct=candle_stick&o[0][ot]=sma&o[0][op]=50&o[0][oc]=FF8F33C6&o[1][ot]=ema&o[1][op]=10&o[1][oc]=DCB3326D&o[2][ot]=ema&o[2][op]=21&o[2][oc]=DC32B363&o[3][ot]=patterns&o[3][op]=&o[3][oc]=000")


    if timing == "Weekly":
        for stock in symbols:
            st.image(f"https://charts2-node.finviz.com/chart.ashx?cs=l&t={stock}&tf=w&s=linear&ct=candle_stick&o[0][ot]=sma&o[0][op]=40&o[0][oc]=FF8F33C6&o[1][ot]=sma&o[1][op]=30&o[1][oc]=DCB3326D&o[2][ot]=sma&o[2][op]=10&o[2][oc]=DC32B363&o[3][ot]=patterns&o[3][op]=&o[3][oc]=000")
            st.image(f"https://charts2-node.finviz.com/chart.ashx?cs=l&t={stock}&tf=d&s=linear&ct=candle_stick&o[0][ot]=sma&o[0][op]=50&o[0][oc]=FF8F33C6&o[1][ot]=ema&o[1][op]=10&o[1][oc]=DCB3326D&o[2][ot]=ema&o[2][op]=21&o[2][oc]=DC32B363&o[3][ot]=patterns&o[3][op]=&o[3][oc]=000")

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
            st.image(f"https://charts2-node.finviz.com/chart.ashx?cs=l&t={stock}&tf=d&s=linear&ct=candle_stick&o[0][ot]=sma&o[0][op]=50&o[0][oc]=FF8F33C6&o[1][ot]=ema&o[1][op]=10&o[1][oc]=DCB3326D&o[2][ot]=ema&o[2][op]=21&o[2][oc]=DC32B363&o[3][ot]=patterns&o[3][op]=&o[3][oc]=000")

    if timing == "Multi":
        for stock in symbols:
            st.image(f"https://charts2-node.finviz.com/chart.ashx?cs=l&t={stock}&tf=m&s=linear&ct=candle_stick&o[0][ot]=sma&o[0][op]=5&o[0][oc]=FF8F33C6&o[1][ot]=sma&o[1][op]=10&o[1][oc]=DCB3326D&o[2][ot]=sma&o[2][op]=20&o[2][oc]=DC32B363&o[3][ot]=patterns&o[3][op]=&o[3][oc]=000")
            st.image(f"https://charts2-node.finviz.com/chart.ashx?cs=l&t={stock}&tf=w&s=linear&ct=candle_stick&o[0][ot]=sma&o[0][op]=40&o[0][oc]=FF8F33C6&o[1][ot]=sma&o[1][op]=30&o[1][oc]=DCB3326D&o[2][ot]=sma&o[2][op]=10&o[2][oc]=DC32B363&o[3][ot]=patterns&o[3][op]=&o[3][oc]=000")
            st.image(f"https://charts2-node.finviz.com/chart.ashx?cs=l&t={stock}&tf=d&s=linear&ct=candle_stick&o[0][ot]=sma&o[0][op]=50&o[0][oc]=FF8F33C6&o[1][ot]=ema&o[1][op]=10&o[1][oc]=DCB3326D&o[2][ot]=ema&o[2][op]=21&o[2][oc]=DC32B363&o[3][ot]=patterns&o[3][op]=&o[3][oc]=000")

if option == "SPQQ100":
    with open('master') as f:
        symbols=[i.strip() for i in f.readlines()]
        symbols = list(dict.fromkeys(symbols))

    if timing == "Daily":
        for stock in symbols:
            st.image(f"https://charts2-node.finviz.com/chart.ashx?cs=l&t={stock}&tf=d&s=linear&ct=candle_stick&o[0][ot]=sma&o[0][op]=50&o[0][oc]=FF8F33C6&o[1][ot]=ema&o[1][op]=10&o[1][oc]=DCB3326D&o[2][ot]=ema&o[2][op]=21&o[2][oc]=DC32B363&o[3][ot]=patterns&o[3][op]=&o[3][oc]=000")


    if timing == "Weekly":
        for stock in symbols:
            st.image(f"https://charts2-node.finviz.com/chart.ashx?cs=l&t={stock}&tf=w&s=linear&ct=candle_stick&o[0][ot]=sma&o[0][op]=40&o[0][oc]=FF8F33C6&o[1][ot]=sma&o[1][op]=30&o[1][oc]=DCB3326D&o[2][ot]=sma&o[2][op]=10&o[2][oc]=DC32B363&o[3][ot]=patterns&o[3][op]=&o[3][oc]=000")
            st.image(f"https://charts2-node.finviz.com/chart.ashx?cs=l&t={stock}&tf=d&s=linear&ct=candle_stick&o[0][ot]=sma&o[0][op]=50&o[0][oc]=FF8F33C6&o[1][ot]=ema&o[1][op]=10&o[1][oc]=DCB3326D&o[2][ot]=ema&o[2][op]=21&o[2][oc]=DC32B363&o[3][ot]=patterns&o[3][op]=&o[3][oc]=000")

    if timing == "Multi":
        for stock in symbols:
            st.image(f"https://charts2-node.finviz.com/chart.ashx?cs=l&t={stock}&tf=m&s=linear&ct=candle_stick&o[0][ot]=sma&o[0][op]=5&o[0][oc]=FF8F33C6&o[1][ot]=sma&o[1][op]=10&o[1][oc]=DCB3326D&o[2][ot]=sma&o[2][op]=20&o[2][oc]=DC32B363&o[3][ot]=patterns&o[3][op]=&o[3][oc]=000")
            st.image(f"https://charts2-node.finviz.com/chart.ashx?cs=l&t={stock}&tf=w&s=linear&ct=candle_stick&o[0][ot]=sma&o[0][op]=40&o[0][oc]=FF8F33C6&o[1][ot]=sma&o[1][op]=30&o[1][oc]=DCB3326D&o[2][ot]=sma&o[2][op]=10&o[2][oc]=DC32B363&o[3][ot]=patterns&o[3][op]=&o[3][oc]=000")
            st.image(f"https://charts2-node.finviz.com/chart.ashx?cs=l&t={stock}&tf=d&s=linear&ct=candle_stick&o[0][ot]=sma&o[0][op]=50&o[0][oc]=FF8F33C6&o[1][ot]=ema&o[1][op]=10&o[1][oc]=DCB3326D&o[2][ot]=ema&o[2][op]=21&o[2][oc]=DC32B363&o[3][ot]=patterns&o[3][op]=&o[3][oc]=000")

if option == "NEW_Daily_review":
    st.write("MARKET RESEARCH")

    url = "https://finviz.com/groups.ashx?g=sector&v=210&o=name"
    st.write("FINVIZ Groups [link](%s)" % url)
    
    url = "https://www.sectorspdrs.com/sectortracker"
    st.write("SPDR Sectors [link](%s)" % url)
        
    url = "https://stockcharts.com/freecharts/rrg/?s=VTI,QQQ,DIA,IWO,SMH,IGV,CIBR,IBIT,XME,GLD,XHB,XLB,XLC,XLE,XLF,XLI,XLK,XLP,XLRE,XLU,XLV,XLY,SDS,XOP,BLOK,ARKK,FFTY,AIQ&b=SPY&p=w&g=1y&t=6&c=false&f=chg,d"
    st.write("SPDR Sectors RRG [link](%s)" % url)

    options = st.selectbox(
        'Pick the SPDR sectors',
        ['DAILY', 'XLK', 'SMH', 'IGV', 'CIBR', 'XLC', 'XLY', 'XLP', 'XLF', 'XLV', 'XLI', 'XLE', 'XLB', 'XLU', 'XOP', 'XHB', 'XME', 'TAN', 'BLOK', 'AIQ',  ])
    
    #st.write('You selected:', options)
    
    
    #options = st.checkbox('XLK', 'XLC', 'XLY', 'XLP', 'XLF', 'XLV', 'XLI', 'XLE', 'XLB', 'XLU', 'XOP', 'XHB', 'XME')
    
    
    
    
    SPDR = {
        'DAILY' : ['SPY', 'QQQ', 'DIA',  'IWO', 'VTI', 'RSP', 'QQQE', 'SDS', 'XLK', 'SMH', 'IGV', 'CIBR', 'VGT', 'TAN', 'FFTY', 'IBIT', 'AAPL', 'AMZN', 'MSFT', 'GOOGL', 'META', 'NFLX', 'NVDA', 'TSLA', 'AMD', 'COST', 'NOW', 'AVGO', 'XLC', 'XLY', 'XLP', 'XLF', 'XLV', 'XLI', 'XLE', 'XLB', 'XLU', 'XOP', 'XHB', 'XME' ],
        'XLK': ['MSFT', 'AAPL', 'AVGO', 'NVDA', 'CRM', 'AMD', 'ADBE', 'ACN', 'ORCL', 'CSCO', 'QCOM', 'INTU', 'IBM', 'AMAT', 'INTC', 'NOW', 'TXN', 'MU', 'LRCX', 'ADI'],
        'XLC': ['META', 'GOOGL', 'GOOG', 'NFLX', 'VZ', 'T', 'TMUS', 'EA', 'DIS', 'CMCSA', 'CHTR', 'TTWO', 'WBD', 'OMC', 'LYV', 'IPG', 'NWSA', 'MTCH', 'FOXA', 'PARA'],
        'XLY': ['AMZN', 'TSLA', 'HD', 'MCD', 'LOW', 'BKNG', 'TJX', 'NKE', 'SBUX', 'CMG', 'ABNB', 'ORLY', 'MAR', 'AZO', 'HLT', 'F', 'GM', 'DHI', 'ROST', 'LULU'],
        'XLP': ['PG', 'COST', 'WMT', 'KO', 'PEP', 'PM', 'MDLZ', 'TGT', 'MO', 'CL', 'STZ', 'KMB', 'MNST', 'GIS', 'SYY', 'KR', 'DG', 'KVUE', 'ADM', 'EL'],
        'XLF': ['BRK-B', 'JPM', 'V', 'MA', 'BAC', 'WFC', 'SPGI', 'GS', 'AXP', 'PGR', 'C', 'MS', 'BLK', 'SCHW', 'CB', 'MMC', 'FI', 'BX', 'ICE', 'CME'],
        'XLV': ['LLY', 'UNH', 'JNJ', 'MRK', 'ABBV', 'TMO', 'ABT', 'DHR', 'PFE', 'AMGN', 'ISRG', 'ELV', 'SYK', 'MDT', 'CI', 'BMY', 'VRTX', 'BSX', 'REGN', 'CVS', 'GEHC'],
        'XLI': ['CAT', 'GE', 'UBER', 'UNP', 'RTX', 'ETN', 'HON', 'UPS', 'DE', 'BA', 'ADP', 'LMT', 'WM', 'PH', 'CSX', 'ITW', 'TT', 'TDG', 'GD', 'EMR'],
        'XLE': ['XOM', 'CVX', 'COP', 'MPC', 'EOG', 'SLB', 'PSX', 'PXD', 'VLO', 'WMB', 'OKE', 'OXY', 'HES', 'HAL', 'FANG', 'KMI', 'BKR', 'DVN', 'TRGP', 'CTRA'],
        'XLB': ['LIN', 'SHW', 'FCX', 'ECL', 'APD', 'NUE', 'NEM', 'DOW', 'CTVA', 'MLM', 'VMC', 'PPG', 'DD', 'LYB', 'STLD', 'IFF', 'BALL', 'AVY', 'PKG', 'CF'],
        'XLU': ['NEE', 'SO', 'DUK', 'CEG', 'SRE', 'AEP', 'D', 'EXC', 'PCG', 'PEG', 'ED', 'XEL', 'EIX', 'WEC', 'AWK', 'DTE', 'ETR', 'ES', 'PPL', 'FE'],
        'XLRE': ['PLD', 'AMT', 'EQIX', 'WELL', 'SPG', 'PSA', 'O', 'CCI', 'DLR', 'CSGP', 'EXR', 'VICI', 'CBRE', 'AVB', 'WY', 'SBAC', 'IRM', 'EQR', 'INVH', 'ARE'],
        'XOP': ['COP', 'EOG', 'PXD', 'FANG', 'OXY', 'HES', 'MRO', 'DVN', 'APA', 'CXO', 'XOM', 'CVX', 'SLB', 'PSX', 'MPC', 'HAL', 'BKR'],
        'XHB': ['WSM', 'CSL', 'OC', 'BLD', 'TT', 'JCI', 'TOL', 'NVR', 'DHI', 'PHM', 'BLDR', 'ALLE', 'LEN', 'FBIN', 'MAS', 'LII', 'LOW', 'TPX', 'CARR', 'FND', 'HD'],
        'XBI': ['EXAS', 'CRNX', 'ROIV', 'EXEL', 'CYTK', 'KRYS', 'NTRA', 'VKTX', 'CERE', 'SRPT', 'ALNY', 'BMRN', 'DYN', 'MRNA', 'NBIX', 'BPMC', 'INSM', 'AMGN', 'VRTX', 'IONS'],
        'XME': ['FCX', 'AA', 'UEC', 'STLD', 'RGLD', 'NUE', 'CLF', 'CMC', 'CRS', 'RS', 'ATI', 'HL', 'MP', 'CEIX', 'X', 'BTU', 'ARCH', 'AMR', 'CDE'],
        'SMH': ['NVDA', 'TSM', 'AVGO', 'ASML', 'MU', 'QCOM', 'TXN', 'LRCX', 'AMAT', 'INTC', 'AMD', 'ADI', 'KLAC', 'SNPS', 'CDNS', 'NXPI', 'MRVL', 'MCHP', 'STM', 'MPWR'],
        'IGV': ['MSFT', 'CRM', 'ORCL', 'ADBE', 'INTU', 'NOW', 'SNPS', 'PANW', 'CDNS', 'CRWD', 'ROP', 'WDAY', 'ADSK', 'FTNT', 'PLTR', 'DDOG', 'HUBS', 'EA', 'FICO', 'TEAM'],
        'CIBR': ['AVGO', 'CSCO', 'CRWD', 'INFY', 'PANW', 'GEN', 'CHKP', 'FFIV', 'LDOS', 'FTNT', 'BAH', 'TENB', 'OTEX', 'CYBR', 'AKAM', 'QLYS', 'NET', 'OKTA', 'SAIC', 'VRNS', 'RPD', 'S', 'ZS'],
        'TAN': ['ENPH', 'SEDG', 'RUN', 'FSLR', 'SOL', 'CSIQ', 'JKS', 'MAXN', 'NOVA', 'SPWR'],
        'BLOK': ['GLXY', 'COIN', 'MSTR', 'BYON', 'PYPL', 'HOOD', 'NU', 'IBM', 'SQ', 'RBLX', 'MARA', 'CLSK', 'CORZ', 'RIOT', 'CME', 'ACN'],
        'AIQ': ['AAPL', 'MSFT', 'GOOGL', 'AMZN', 'FB', 'TSLA', 'NVDA', 'CRM', 'PYPL', 'ADBE'],
        'PAVE': ['DE', 'CAT', 'UNP', 'EMR', 'JCI', 'NUE', 'FAST', 'VRSK', 'VRSN', 'WAB'],
        'JETS': ['LUV', 'DAL', 'UAL', 'AAL', 'ALK', 'JBLU', 'SAVE', 'HA', 'SKYW', 'MESA']
    }
    
    if options:
        st.write(options)
        st.header(options)
    
        for sector, stocks in SPDR.items():
            spdr_sector = sector
            if spdr_sector in options:
    
                #print(f"Top 10 stocks in {sector}:")
                for stock in stocks:
                    col1, col2 = st.columns(2)
                #print(f"- {stock}")
                    with col1:
                        st.image(f"https://charts2-node.finviz.com/chart.ashx?cs=l&t={stock}&tf=w&s=linear&ct=candle_stick&o[0][ot]=sma&o[0][op]=40&o[0][oc]=FF8F33C6&o[1][ot]=sma&o[1][op]=30&o[1][oc]=DCB3326D&o[2][ot]=sma&o[2][op]=10&o[2][oc]=DC32B363&o[3][ot]=patterns&o[3][op]=&o[3][oc]=000", width=1024)
                    with col2:
                        st.image(f"https://charts2-node.finviz.com/chart.ashx?cs=l&t={stock}&tf=d&s=linear&ct=candle_stick&o[0][ot]=sma&o[0][op]=50&o[0][oc]=FF8F33C6&o[1][ot]=ema&o[1][op]=10&o[1][oc]=DCB3326D&o[2][ot]=ema&o[2][op]=21&o[2][oc]=DC32B363&o[3][ot]=patterns&o[3][op]=&o[3][oc]=000", width=1024)

