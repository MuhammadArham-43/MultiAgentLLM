import streamlit as st
import os
import requests
from requests.exceptions import HTTPError

def display_loading_overlay(show: bool):
    if show:
        st.markdown(
            """
            <style>
            .loading-overlay {
                position: fixed;
                top: 0;
                left: 0;
                width: 100%;
                height: 100%;
                background: rgba(255, 255, 255, 0.5);
                z-index: 1000;
                display: flex;
                align-items: center;
                justify-content: center;
            }
            .loading-overlay > div {
                font-size: 24px;
                font-weight: bold;
            }
            </style>
            <div class="loading-overlay">
                <div></div>
            </div>
            """,
            unsafe_allow_html=True
        )
    else:
        st.markdown(
            """
            <style>
            .loading-overlay {
                display: none;
            }
            </style>
            """,
            unsafe_allow_html=True
        )

st.set_page_config(page_title="Realtime Agentic LLM")
st.title("General Purpose Multi-Agent LLM")
query = st.text_input("Query", "")
spinner_placeholder = st.empty()

if st.button("Send Request"):
    if query:
        with st.spinner("Executing"):
            display_loading_overlay(True)
            try:
                api_url = os.getenv("SERVER_URL", "http://localhost:8080/query/")
                response = requests.post(api_url, json={"topic": query})
                response.raise_for_status()
                result = response.json()
                st.markdown(result.get("response", "No response found"))

            except HTTPError as http_err:
                st.error(f"HTTP error occurred: {http_err}")
            except Exception as err:
                st.error(f"An error occurred: {err}")
            finally:
                display_loading_overlay(False)
    else:
        st.warning("Please enter a query before sending the request.")
