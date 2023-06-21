import streamlit as sl


sl.header("Contact Me")

with sl.form(key="email_form"):
    user_email = sl.text_input("Your email address")
    message = sl.text_area("Your message")
    button = sl.form_submit_button("Submit")
    if button:
        print("I was pressed!")