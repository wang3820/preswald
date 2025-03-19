from preswald import text, plotly, connect, get_df, table, query, slider
import pandas as pd
import plotly.express as px

text("# Big Ten College Basketball Efficiency Analysis 2017")

# Load the CSV
connect() # load in all sources, which by default is the sample_csv
df = get_df("cbb_csv")

sql = "SELECT * FROM cbb_csv WHERE YEAR = 2018 AND CONF = 'B10' ORDER BY BARTHAG DESC"

filtered_df = query(sql, "cbb_csv")
filtered_df = filtered_df[['TEAM', 'ADJOE', 'ADJDE', 'BARTHAG']]
filtered_df = filtered_df.rename(columns={
    "TEAM": "Team",
    "ADJOE": "Adjusted Offensive Efficiency",
    "ADJDE": "Adjusted Defensive Efficiency",
    "BARTHAG": "Overall Rating"
})

table(filtered_df, title="Statistics")

threshold = slider("Threshold", min_val=90, max_val=125, default=90)
table(filtered_df[filtered_df["Adjusted Offensive Efficiency"] > threshold], title="Dynamic Data View")

fig = px.scatter(filtered_df, x="Adjusted Offensive Efficiency", y="Adjusted Defensive Efficiency", color="Team")
plotly(fig)