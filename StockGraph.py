import plotly.graph_objects as go 
import yfinance

tsla = yfinance.Ticker("TSLA")
hist = tsla.history(period = "1y")

fig = go.Figure(data = go.Scatter(x=hist.Index, y = hist['Close']))
fig.show()