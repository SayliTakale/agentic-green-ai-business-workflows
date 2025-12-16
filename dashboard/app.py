import streamlit as st
import pandas as pd

st.title("Green AI Sustainability Dashboard")

data = {
    "Model": ["Baseline", "Green"],
    "Energy Usage": [120, 65]
}

df = pd.DataFrame(data)

st.subheader("Current vs Optimized Energy Usage")
st.bar_chart(df.set_index("Model"))

st.subheader("Suggested Model Swap")
st.write("Baseline Model → Green Model")

st.subheader("Impact Over Time")
st.line_chart([120, 90, 65])
