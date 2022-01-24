import pandas as pd 
import altair as alt

# Question 2: Creating a chart based on the mpg dataset
url = "https://github.com/byuidatascience/data4python4ds/raw/master/data-raw/mpg/mpg.csv"

# Use the read_scv module in pandas to pull a csv file from a url
mpg = pd.read_csv(url)

# Create a chart with the mpg data set, setting 'displ' as the x-axis and 'hwy' as the y-axis in the chart
chart = (alt.Chart(mpg)
  .encode(
    x='displ', 
    y='hwy')
  .mark_circle()
)

chart

# Save the chart as a .png file
chart.save("my_chart1.png")

# Question 3: Creating a markdown table given the following code
print(mpg
  .head(5)
  .filter(["manufacturer", "model","year", "hwy"])
  .to_markdown(index=False))