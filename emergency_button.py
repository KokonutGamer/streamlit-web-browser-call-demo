import streamlit as st
import webbrowser

# Streamlit app
st.title("Emergency Button")

# Button to trigger emergency action
if st.button("Call Emergency Services"):
    # Replace with the actual action you want to perform
    # Example: Open a URL to dial emergency services (e.g., tel:911 for mobile devices)
    webbrowser.open("tel:425-394-8991")  # This works on mobile devices with a browser
    st.success("Dialing emergency services...")
