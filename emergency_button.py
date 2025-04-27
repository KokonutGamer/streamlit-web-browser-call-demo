import streamlit as st

# Streamlit app
st.title("Emergency Button")

# Button to trigger emergency action
if st.button("Call Emergency Services"):
    # Display a clickable link for the user to dial the number
    st.markdown("[Click here to call emergency services](tel:425-394-8991)")
    st.success("Click the link above to dial emergency services.")
