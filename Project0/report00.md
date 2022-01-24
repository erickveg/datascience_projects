# Project Document Title

__Erick Vega__

## Project Summary

The purpose of this project is to introduce the required tools to properly develop and run the upcoming projects in the CSE250 course. Altair, a visualization package, will be used to generate the chart presented in this project.

## Technical Details

#### 1. Finish the readings and come to class prepared with any questions to get your environment working smoothly.

I completed the readings and installed the required packages. I run on a problem saving the Altair chart but this was solved in class installing Node.js.

#### 2. Write a python script to create the example Altair chart from section 3.2.2 of the textbook.

This is the chart created using Altair and data from the **mpg** dataset:

![Altair Chart](my_chart.png)

#### 3. Include a markdown table created from a particular code. 

| manufacturer   | model   |   year |   hwy |
|:---------------|:--------|-------:|------:|
| audi           | a4      |   1999 |    29 |
| audi           | a4      |   1999 |    29 |
| audi           | a4      |   2008 |    31 |
| audi           | a4      |   2008 |    30 |
| audi           | a4      |   1999 |    26 |


## Appendix A



```python
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
```