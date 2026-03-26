
# Example of using columns, sidebar, tabs, and expander in Streamlit:
import streamlit as st

# ── Columns ──────────────────────────────────
col1, col2, col3 = st.columns(3)
with col1:
    st.metric("Temperature", "28°C", "+2°C")
with col2:
    st.metric("Humidity", "65%", "-5%")
with col3:
    st.metric("Wind", "12 km/h", "+3 km/h")

# ── Sidebar ──────────────────────────────────
with st.sidebar:
    st.title("Settings")
    theme = st.selectbox("Theme", ["Light", "Dark", "Auto"])
    language = st.radio("Language", ["English", "Urdu"])

# ── Tabs ─────────────────────────────────────
tab1, tab2 = st.tabs(["📊 Data", "📈 Charts"])
with tab1:
    st.write("Data goes here")
with tab2:
    st.write("Charts go here")

# ── Expander (accordion) ──────────────────────
with st.expander("Click to see more details"):
    st.write("Hidden content revealed on click!")