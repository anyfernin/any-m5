import streamlit as st
import pandas as pd
import datetime

st.title("APP DE TITANIC")
sidebar = st.sidebar

titanic_link = 'titanic.csv'
titanic_data = pd.read_csv(titanic_link)
# Create the title for the web app st.title("My First Streamlit App") sidebar = st.sidebar
sidebar.title("This is the sidebar.")
sidebar = st.sidebar
sidebar.title("This is the sidebar.")
sidebar.write("You can add any elements to the sidebar.")

today = datetime.date.today()
today_date = sidebar.date_input('Current date', today)
st.success('Current date: `%s` ' % (today_date))

st.header("Dataset")
agree = sidebar.checkbox("show DataSet Overview ? ")
if agree:
  st.dataframe(titanic_data)

selected_town = st.radio("Select Embark Town", titanic_data['embark_town'].unique())
st.write("Selected Embark Town:", selected_town)

st.write(titanic_data.query(f"""embark_town==@selected_town"""))

st.markdown("___")

# Select a range of the fare and then display the dataset with this selection
optionals = st.expander("Optional Configurations", True)
fare_min = optionals.slider(
    "Minimum Fare",
    min_value=float(titanic_data['fare'].min()),
    max_value=float(titanic_data['fare'].max())
)
fare_max = optionals.slider(
    "Maximum Fare",
    min_value=float(titanic_data['fare'].min()),
    max_value=float(titanic_data['fare'].max())
)
subset_fare = titanic_data[(titanic_data['fare'] <= fare_max) & (fare_min <= titanic_data['fare'])]
st.write(f"Number of Records With Fare Between {fare_min} and {fare_max}: {subset_fare.shape[0]}")

# Display of the dataset 
st.dataframe(subset_fare)