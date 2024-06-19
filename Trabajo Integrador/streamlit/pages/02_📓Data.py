import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st
import plotly.express as px
import geopandas as gpd
import folium
from streamlit_folium import st_folium
from pathlib import Path

path_lagos = Path('../custom_data/lagos_arg.csv')
path_aeropuertos = Path('../custom_data/ar-airports-custom.csv')

# Leer el archivo CSV de los lagos
try:
    df_lagos = pd.read_csv(path_lagos)
except FileNotFoundError as e:
    st.error(f"Error al leer el archivo de lagos: {e}")
    st.stop()

# Leer el archivo CSV de los aeropuertos
try:
    df_aeropuertos = pd.read_csv(path_aeropuertos)
except FileNotFoundError as e:
    st.error(f"Error al leer el archivo de aeropuertos: {e}")
    st.stop()

st.title('Análisis de Lagos y Aeropuertos')

# Sección de Lagos
st.header('Lagos')

st.subheader('Mapa de Lagos')
try:
    # Creo un GeoDataFrame desde el DataFrame de lagos
    gdf_lagos = gpd.GeoDataFrame(
        df_lagos, geometry=gpd.points_from_xy(df_lagos['Longitud (GD)'], df_lagos['Latitud (GD)']))

    # Creo un mapa centrado en Argentina
    mapa_lagos = folium.Map(location=[-38.4161, -63.6167], zoom_start=4)

    # Agrego marcadores de los lagos al mapa
    for idx, row in gdf_lagos.iterrows():
        folium.Marker([row.geometry.y, row.geometry.x], popup=row['Nombre']).add_to(mapa_lagos)

    # Mostrar el mapa en Streamlit
    st_folium(mapa_lagos, width=700, height=500)
except Exception as e:
    st.error(f"Error al crear el mapa de lagos: {e}")

# DataFrame de los Lagos
st.subheader('Datos de los Lagos')
st.dataframe(df_lagos)

# Superficie de los Lagos
st.subheader('Superficie de los Lagos')
try:
    fig, ax = plt.subplots(figsize=(12, 6))
    ax.bar(df_lagos['Nombre'], df_lagos['Superficie (km2)'], color='skyblue')
    ax.set_xlabel('Nombre del Lago')
    ax.set_ylabel('Superficie (km²)')
    ax.set_title('Superficie de los Lagos')
    plt.xticks(rotation=45)
    st.pyplot(fig)
except KeyError as e:
    st.error(f"Error en el gráfico de barras: {e}")

# Relación entre Profundidad Máxima y Profundidad Media
st.subheader('Relación entre Profundidad Máxima y Profundidad Media')
try:
    fig, ax = plt.subplots(figsize=(10, 6))
    scatter = ax.scatter(df_lagos['Profundidad máxima (m)'], df_lagos['Profundidad media (m)'], color='blue', alpha=0.5)
    ax.set_xlabel('Profundidad Máxima (m)')
    ax.set_ylabel('Profundidad Media (m)')
    ax.set_title('Relación entre Profundidad Máxima y Profundidad Media')

    for i, nombre in enumerate(df_lagos['Nombre']):
        ax.text(df_lagos['Profundidad máxima (m)'][i], df_lagos['Profundidad media (m)'][i], nombre, fontsize=9)

    ax.grid(True)
    st.pyplot(fig)
except KeyError as e:
    st.error(f"Error en el gráfico de dispersión: {e}")

# Sección de Aeropuertos
st.header('Aeropuertos')

# Mapa de Aeropuertos
st.subheader('Mapa de Aeropuertos')
try:
    # Creo un mapa centrado en Argentina
    mapa_aeropuertos = folium.Map(location=[-38.4161, -63.6167], zoom_start=4)

    # Agrego aeropuertos al mapa
    for idx, row in df_aeropuertos.iterrows():
        folium.Marker(location=[row['latitude_deg'], row['longitude_deg']],
                      popup=row['name'],
                      icon=folium.Icon(color='red')).add_to(mapa_aeropuertos)

    # Mostrar el mapa en Streamlit
    st_folium(mapa_aeropuertos, width=700, height=500)
except Exception as e:
    st.error(f"Error al crear el mapa de aeropuertos: {e}")

# Datos de los Aeropuertos
st.subheader('Datos de los Aeropuertos')
st.dataframe(df_aeropuertos)

# Número de Aeropuertos por Tipo
st.subheader('Número de Aeropuertos por Tipo')
try:
    type_counts = df_aeropuertos['type'].value_counts()
    fig = px.bar(type_counts, x=type_counts.index, y=type_counts.values, title='Número de Aeropuertos por Tipo', labels={'x': 'Tipo de Aeropuerto', 'y': 'Cantidad'})
    fig.update_layout(xaxis_title='Tipo de Aeropuerto', yaxis_title='Cantidad', xaxis_tickangle=-45)
    st.plotly_chart(fig)
except KeyError as e:
    st.error(f"Error en el gráfico de barras: {e}")

# Distribución de Aeropuertos por Provincia
st.subheader('Distribución de Aeropuertos por Provincia')
try:
    prov_counts = df_aeropuertos['prov_name'].value_counts()
    fig = px.pie(prov_counts, values=prov_counts.values, names=prov_counts.index, title='Distribución de Aeropuertos por Provincia')
    st.plotly_chart(fig)
except KeyError as e:
    st.error(f"Error en el gráfico de torta: {e}")
