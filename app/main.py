import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

st.set_page_config(layout="wide")
st.title("📅 Smart Calendar Heatmap Generator")

uploaded_file = st.file_uploader("📤 Upload a CSV file (must include date and value columns)", type=['csv'])

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.write("🗂 Raw Data Preview")
    st.dataframe(df.head())

    # Auto-detect date and value columns
    date_col = st.selectbox("Select the date column", df.columns)
    value_col = st.selectbox("Select the value column", df.columns)

    # Convert date and extract year/month/day
    df[date_col] = pd.to_datetime(df[date_col], errors='coerce')
    df = df.dropna(subset=[date_col])
    df['date'] = df[date_col].dt.date
    df = df.groupby('date')[value_col].sum().reset_index()

    # Pivot for heatmap
    df['date'] = pd.to_datetime(df['date'])
    df['dow'] = df['date'].dt.dayofweek  # 0 = Monday
    df['week'] = df['date'].dt.isocalendar().week
    df['year'] = df['date'].dt.year

    st.subheader("📆 Select Year")
    year_selected = st.selectbox("Year", sorted(df['year'].unique(), reverse=True))
    df = df[df['year'] == year_selected]

    pivot_table = df.pivot(index='dow', columns='week', values=value_col)

    fig, ax = plt.subplots(figsize=(20, 4))
    sns.heatmap(pivot_table, cmap='YlGnBu', linewidths=0.5, linecolor='gray', ax=ax, cbar_kws={'label': value_col})
    ax.set_yticklabels(['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'], rotation=0)
    ax.set_title(f"{value_col} Heatmap - {year_selected}", fontsize=16)
    st.pyplot(fig)

else:
    st.info("👆 Upload a CSV file to begin.")
