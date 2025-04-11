import streamlit as st
# Retrieve data from session state
if "number_of_boilers" in st.session_state and "boiler" in st.session_state:
    st.write(f"Name: {st.session_state['number_of_boilers']}")
    st.write(f"Age: {st.session_state['boiler']}")
else:
    st.warning("No data found. Please go to the Input Page and enter your information.")
