import streamlit as sl

sl.set_page_config(layout="wide")

col1, col2 = sl.columns(2)

with col1:
    sl.image("006 images/21.jpg")

with col2:
    sl.title("Damir Kokic")
    content = """
    Hi! My name is Damir. I love to program in Python, and you can find some of my projects below. I currently work as
    a Data Analyst and love to play sports. 
    """
    sl.info(content)