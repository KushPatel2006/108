import plotly.figure_factory as ff
import pandas as np
import csv

df = np.read_csv("D:/projects")
fig = ff.create_distplot([df["Avg Rating"].tolist()], ["rating"])
fig.show()