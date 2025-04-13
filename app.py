import streamlit as st
import requests

st.title("Sales Email Agent")

email = st.text_input("Lead Email")
lead_info = st.text_area("Lead Description")

if st.button("Generate & Send Email"):
    with st.spinner("Thinking..."):
        response = requests.post("http://localhost:8000/send-email", json={
            "email": email,
            "lead_info": lead_info
        })
        st.success(response.json()["message"])
        st.code(response.json()["generated_email"])
