import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

df_day = pd.read_csv("dashboard/day.csv")
df_day['dteday'] = pd.to_datetime(df_day['dteday'])

st.title("Bike Rental Analysis Dashboard")

st.subheader("Dataset Preview")
st.write(df_day.head())

# Visualization: Total rental berdasarkan Cuaca (Line Plot)
st.subheader("Total rental berdasarkan Cuaca")
weather_colors = {1: "blue", 2: "orange", 3: "red", 4: "grey"}
weather_labels = {1: "Clear", 2: "Mist", 3: "Light Snow/Rain", 4: "Heavy Rain/Snow"}
daily_weather = df_day.groupby(['dteday', 'weathersit'])['cnt'].sum().reset_index()

plt.figure(figsize=(12, 6))
lines = []
for weather, color in weather_colors.items():
    subset = daily_weather[daily_weather['weathersit'] == weather]
    line, = plt.plot(subset['dteday'], subset['cnt'], label=weather_labels[weather], color=color)
    lines.append(line)
plt.title("Total Penyewaan Sepeda Harian Berdasarkan Cuaca")
plt.xlabel("Tanggal")
plt.ylabel("Total Rental")
plt.xticks(rotation=45)
plt.legend(handles=lines, title="Weather Condition")
st.pyplot(plt)

# Visualization: Working Day vs Weekend (Bar Plot)
st.subheader("Working Day vs Weekend Rental Comparison")
day_labels = {0: "Weekend/Holiday", 1: "Working Day"}

day_data = df_day.groupby("workingday")["cnt"].mean().reset_index()
day_data["Day Type"] = day_data["workingday"].map(day_labels)

x = np.arange(len(day_data))
colors = ["red", "blue"]

fig, ax = plt.subplots(figsize=(8, 5))

ax.bar(x, day_data["cnt"], color=colors)
ax.set_title("Average Total Bike Rentals: Working Day vs Weekend")
ax.set_ylabel("Average Number of Rentals")
ax.set_xlabel("Day Type")
ax.set_xticks(x)
ax.set_xticklabels(day_data["Day Type"])

st.pyplot(fig)

st.subheader("Kesimpulan")

st.write("""
1. **Faktor cuaca pada rental sepeda**: Dari hasil analisis visualisasi data, dapat disimpulkan bahwa cuaca memiliki pengaruh yang signifikan terhadap jumlah penyewaan sepeda. Cuaca cerah terbukti menjadi faktor yang paling mendukung peningkatan jumlah penyewaan sepeda, dengan penyewa lebih cenderung menggunakan sepeda saat kondisi cuaca mendukung aktivitas luar ruangan
2. **Working Day vs Weekend**: Hasil analisis menunjukkan bahwa jumlah penyewaan sepeda pada hari kerja lebih tinggi dibandingkan dengan weekend/holiday.
""")