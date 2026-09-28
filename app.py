import streamlit as st
import pandas as pd
import plotly.express as px

# Настройка страницы
st.set_page_config(page_title="Сквозная аналитика", layout="wide")
st.title("📊 Панель сквозной аналитики (MVP)")

# Имитация склеенных данных (Реклама + СРМ)
data = {
    'Канал': ['Yandex Direct', 'VK Ads', 'Telegram Ads', 'SEO'],
    'Расходы, руб': [50000, 35000, 20000, 5000],
    'Клики': [1200, 850, 400, 600],
    'Сделки': [45, 22, 18, 30],
    'Выручка, руб': [120000, 48000, 60000, 90000]
}
df = pd.DataFrame(data)

# Считаем базовые метрики сквозной аналитики
df['CAC (Цена клиента)'] = (df['Расходы, руб'] / df['Сделки']).round(2)
df['ROMI (%)'] = (((df['Выручка, руб'] - df['Расходы, руб']) / df['Расходы, руб']) * 100).round(2)

# Верхние карточки (KPI)
col1, col2, col3 = st.columns(3)
col1.metric("Общая выручка", f"{df['Выручка, руб'].sum():,} руб")
col2.metric("Общие расходы", f"{df['Расходы, руб'].sum():,} руб")
col3.metric("Средний ROMI", f"{df['ROMI (%)'].mean():.1f}%")

st.divider()

# Интерактивные графики
left_chart, right_chart = st.columns(2)

with left_chart:
    st.subheader("Окупаемость каналов (ROMI)")
    fig_romi = px.bar(df, x='Канал', y='ROMI (%)', color='Канал', text='ROMI (%)')
    st.plotly_chart(fig_romi, use_container_width=True)

with right_chart:
    st.subheader("Соотношение Расходы / Выручка")
    fig_compare = px.bar(df, x='Канал', y=['Расходы, руб', 'Выручка, руб'], barmode='group')
    st.plotly_chart(fig_compare, use_container_width=True)

# Таблица с данными
st.subheader("Детальная статистика по когортам")
st.dataframe(df, use_container_width=True)
