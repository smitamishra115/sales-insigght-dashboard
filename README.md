# sales-insigght-dashboard


🌐 **Live Demo**: [Click here to view the dashboard](https://sales-insigght-dashboard-sulgbvwy2pv4kusk7g3wcm.streamlit.app/)

An interactive data analytics dashboard built with Python and Streamlit that analyzes retail sales data to uncover business insights around revenue, profitability, and regional/category performance.

## 📊 Overview

This project analyzes the Superstore Sales dataset to answer key business questions:
- What is the total revenue and profit?
- Which regions and product categories are the most/least profitable?
- How has sales performance trended over the years?
- Which sub-categories are underperforming, and why?

## 🔍 Key Insights

- Identified that the **West region** generates the highest profit, while the **Central region** has the lowest, despite similar sales volumes.
- Discovered that the **Tables** sub-category was operating at a loss, driven by an average discount of ~26% compared to the dataset-wide average of ~15.6%.
- Found that **Technology** had both the highest sales and highest profit margin, while **Furniture** had high sales but a weak profit margin (~2.5%).

## 🛠️ Tech Stack

- **Python** – data processing and logic
- **Pandas** – data cleaning, transformation, and analysis
- **Streamlit** – interactive web dashboard
- **Plotly** – data visualization

## ✨ Features

- Interactive sidebar filter to view data by region
- Real-time metric cards for Total Sales and Total Profit
- Auto-generated insight summary highlighting top/bottom performing regions
- Category-wise sales visualization (bar chart)
- Year-wise sales trend visualization (line chart)

## 📁 Dataset

The dataset used is the [Superstore Sales Dataset] from Kaggle, containing ~10,000 transaction records across 21 columns including order details, customer information, sales, discount, and profit data.

## 🚀 How to Run

1. Clone this repository

2. Install dependencies
  
3. Run the app