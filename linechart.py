import pandas as panda
import plotly_express as plot

data=panda.read_csv("line_chart.csv")

chart=plot.line(data,x="Country",y="Per capita income",color="Year",title="Countries Capital Income")

chart.show()