import streamlit as st

st.title("Unit Converter")
st.markdown("### Convert length, weight, and time")
st.write("## Welcome! Select a category to convert units.")

category = st.selectbox("Select a Category", ["Length","Weight","Time"])

def convert_unit(category, value, unit):
    if category == "Length":
        if unit == "Kilometer to miles":
            return value * 0.621371
        elif unit == "Miles to kilometer":
            return value / 0.621371
        
    elif category == "Weight":
        if unit == "Kilogram to pounds":
            return value * 2.20462
        elif unit == "Pounds to kilogram":
            return value / 2.20462
        
    elif category == "Time":
        if unit == "secound to minutes":
            return value * 60
        elif unit == "Minutes to secound":
            return value / 60
        elif unit == "Minutes to hours":
            return value / 60
        elif unit == "Hours to minutes":
            return value * 60
        elif unit == "Hours to days":
            return value / 24
        elif unit == "Days to hours":
            return value * 24
        
if category == "Length":
    unit = st.selectbox("Select a Unit", ["Kilometer to miles", "Miles to kilometer"])
elif category == "Weight":
    unit = st.selectbox("Select a Unit", ["Kilogram to pounds", "Pounds to kilogram"])
elif category == "Time":
    unit = st.selectbox("Select a Unit", ["secound to minutes", "Minutes to secound", "Minutes to hours", "Hours to minutes", "Hours to days", "Days to hours"])

value = st.number_input("Enter the value to convert", min_value=0.0)

if st.button("Convert"):
    result = convert_unit(category, value, unit)
    st.success(f"The converted value is: {result:.2f}")