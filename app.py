import streamlit as st

st.title("Satellite Blackout AI")

st.write("This MVP predicts possible satellite communication blackout.")

time = st.selectbox(
    "Select time:",
    ["Now", "In 3 minutes", "In 5 minutes"]
)

if st.button("Analyze"):
    st.subheader("Result")
    st.write("Blackout risk: 72%")
    st.write("Recommendation: wait 3 minutes for safer communication.")
