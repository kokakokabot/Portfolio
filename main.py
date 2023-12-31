import streamlit as sl
import pandas as pd

sl.set_page_config(layout="wide")

col1, col2 = sl.columns(2)

with col1:
    sl.image("006 images/21.jpg")

with col2:
    sl.title("Damir Kokic")
    content = """
    Hi! My name is Damir and I love to program in Python. I currently work as a Data Analyst and a hope my journey 
    inspires anyone reading this. I graduated with a Bachelors in Economics, but my main passion has always been Python.
    That is why I try to combine my love for the language and any job I've held to this date. 
    """
    sl.info(content)

content2 = """
You can find some of the applications I built below.
"""

sl.write(content2)

col3, empty_col, col4 = sl.columns([1.5, 0.5, 1.5])


df = pd.read_csv("data.csv", sep=",")

with col3:
    for index, row in df[:10].iterrows():
        sl.header(row["title"])
        sl.write(row["description"])
        sl.image("006 images/" + row["image"])
        sl.write(f"[Source Code]({row['url']})")

with col4:
    for index, row in df[10:].iterrows():
        sl.header(row["title"])
        sl.write(row["description"])
        sl.image("006 images/ " + row["image"])
        sl.write("[Source Code](https://python.com)")