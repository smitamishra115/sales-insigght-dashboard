import pandas as pd
import streamlit as st 
import plotly.express as px

st.title('Sales Insight Dashboard')
st.set_page_config(page_title="Sales Dashboard", layout="wide")

df = pd.read_csv("Superstore_data.csv", encoding="latin1")

df['Order Date'] = pd.to_datetime(df['Order Date'], format="%d-%m-%Y")
df['Ship Date'] = pd.to_datetime(df['Ship Date'], format="%d-%m-%Y")
df['Year'] = df['Order Date'].dt.year

st.subheader("Key Metrics")

col1, col2 = st.columns(2)
col1.metric("Total Sales", f"₹{df['Sales'].sum():,.2f}")
col2.metric("Total Profit", f"₹{df['Profit'].sum():,.2f}")

st.divider()

st.sidebar.title("Filters")

selected_region = st.sidebar.selectbox("Select Region", df['Region'].unique())
filtered_df = df[df['Region'] == selected_region]

st.subheader("Key Insight")

region_profit = df.groupby('Region')['Profit'].sum()
best_region = region_profit.idxmax()
worst_region = region_profit.idxmin()
st.write(f"{best_region} region has the highest profit, while {worst_region} has the lowest profit")

st.subheader("Sales by Category")

category_sales = filtered_df.groupby('Category')['Sales'].sum().reset_index()
fig = px.bar(category_sales, x='Category', y='Sales')
st.plotly_chart(fig)

st.divider()

st.subheader("Yearly Sales Trend")

Yearly_Sales = filtered_df.groupby('Year')['Sales'].sum()
st.line_chart(Yearly_Sales)

st.divider()
