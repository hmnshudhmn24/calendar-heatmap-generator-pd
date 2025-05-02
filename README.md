# 📅 Smart Calendar Heatmap Generator

This **Streamlit** app visualizes time-based data like sales, activity logs, or productivity using a **calendar-style heatmap** generated with **Seaborn** and **Pandas**.

## 🎯 Features

- Upload any CSV with a date and value column
- Automatically detects date and value columns
- Groups data by day and week using Pandas
- Generates calendar-style heatmaps with Seaborn
- Interactive controls to select the year and columns

## 📁 Sample Data Format

```csv
timestamp,value
2023-01-01,5
2023-01-02,6
...
```

## 🚀 How to Run

1. Install the required libraries:

```bash
pip install pandas streamlit seaborn matplotlib
```

2. Launch the app:

```bash
streamlit run app/main.py
```

3. Upload a time-based dataset and generate a smart calendar heatmap!

## 📂 Project Structure

- `app/main.py` — Main Streamlit script
- `data/sample.csv` — Sample time-based dataset
- `README.md` — Project documentation

---

🔥 Powered by Pandas, Seaborn, and Streamlit for beautiful data-driven calendars!
