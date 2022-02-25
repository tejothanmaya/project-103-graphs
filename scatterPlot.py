import pandas as pd
import plotly.express as pe

df = pd.read_csv("CSV.csv")
countries = df["country"].tolist()
cases = df["cases"].tolist()
dates = df["date"].tolist()

pe.scatter(x= dates , y= cases , color= countries)
pe.show()