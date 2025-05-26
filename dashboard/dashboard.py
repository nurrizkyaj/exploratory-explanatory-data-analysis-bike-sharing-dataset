# Dashboard
import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("dashboard/cleaned_dataset.csv")

df['dteday'] = pd.to_datetime(df['dteday'])

st.title("🚲 Bicycle Sharing Dashboard")

st.sidebar.header("Filter")
day_type = st.sidebar.selectbox("Select Day Type", ['All', 'Working Day', 'Holiday'])

if day_type != 'All':
    df = df[df['Day Type'] == day_type]

st.subheader("📈 Key Metrics")
col1, col2 = st.columns(2)
with col1:
    st.metric("Total Users", f"{df['cnt'].sum():,}")
with col2:
    st.metric("Average Daily Users", f"{df['cnt'].mean():,.0f}")

st.subheader("🔍 Average Users: Working Day vs Holiday")
avg_df = df.groupby('Day Type')['cnt'].mean().reset_index()
sns.set(style="whitegrid")
fig1, ax1 = plt.subplots()
sns.barplot(data=avg_df, x='Day Type', y='cnt', palette='Blues', ax=ax1)
ax1.set_ylabel("Average Number of Users")
st.pyplot(fig1)

st.subheader("🌡️ Temperature vs Bicycle Users")
fig2, ax2 = plt.subplots()
sns.scatterplot(data=df, x='temp', y='cnt', alpha=0.6, ax=ax2)
sns.regplot(data=df, x='temp', y='cnt', scatter=False, color='red', ax=ax2)
ax2.set_xlabel("Normalized Temperature")
ax2.set_ylabel("Number of Bicycle Users")
st.pyplot(fig2)