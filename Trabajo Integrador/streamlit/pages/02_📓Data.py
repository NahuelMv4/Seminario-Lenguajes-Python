import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st
import plotly.express as px
import geopandas as gpd
import folium
from streamlit_folium import st_folium
from pathlib import Path

path_lagos = Path('../customdata/lagos_arg.csv')
path_aeropuertos = Path('../customdata/ar-airports-custom.csv')

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
st.write('Violeta: Superficie Grande')
st.write('Azul: Superficie Media')
st.write('Turquesa: Superficie Chica')
try:
    # Crear un mapa centrado en Argentina
    mapa_lagos = folium.Map(location=[-38.4161, -63.6167], zoom_start=4)

    # Definir colores para cada categoría de Sup Tamaño
    colores = {
        "grande": "purple",
        "medio": "blue",
        "chico": "turquoise"
    }

    # Añadir puntos al mapa
    for _, row in df_lagos.iterrows():
        folium.CircleMarker(
            location=[row["Latitud (GD)"], row["Longitud (GD)"]],
            radius=5,
            color=colores[row["Sup Tamaño"]],
            fill=True,
            fill_color=colores[row["Sup Tamaño"]],
            fill_opacity=0.6,
            popup=row["Nombre"]
        ).add_to(mapa_lagos)

    # Mostrar el mapa en Streamlit
    st_folium(mapa_lagos, width=700, height=500)
except Exception as e:
    st.error(f"Error al crear el mapa de lagos: {e}")

# DataFrame de los Lagos
st.subheader('Datos de los Lagos')
st.dataframe(df_lagos)

# Superficie de los Lagos
st.subheader('Superficie de los Lagos')
max_barras = st.slider('Seleccione cuántos lagos mostrar:', 1, min(30, len(df_lagos)), 10)

try:
    # Ordenar lagos por superficie y seleccionar los primeros según la elección del usuario
    df_lagos_sorted = df_lagos.sort_values(by='Superficie (km2)', ascending=False).head(max_barras)

    fig, ax = plt.subplots(figsize=(12, 6))
    ax.bar(df_lagos_sorted['Nombre'], df_lagos_sorted['Superficie (km2)'], color='skyblue')
    ax.set_xlabel('Nombre del Lago')
    ax.set_ylabel('Superficie (km²)')
    ax.set_title(f'Superficie de los {max_barras} Lagos más Grandes')
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
def generate_map():
    attr = (
    '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> '
    'contributors, &copy; <a href="https://cartodb.com/attributions">CartoDB</a>'
    )
    
    tiles = 'https://wms.ign.gob.ar/geoserver/gwc/service/tms/1.0.0/capabaseargenmap@EPSG%3A3857@png/{z}/{x}/{-y}.png'
    m = folium.Map(
        location=(-33.457606, -65.346857),
        control_scale=True,
        zoom_start=5,
        name='es',
        tiles=tiles,
        attr=attr
    )
    return m

colores_elevation = {
    'bajo': 'green',
    'medio': 'blue',
    'alto': 'red'
}

st.subheader('Mapa de Aeropuertos')
try:
    # Creo un mapa centrado en Argentina
    mapa_aeropuertos = generate_map()

    # Agrego aeropuertos al mapa
    for idx, row in df_aeropuertos.iterrows():
        color_point = colores_elevation.get(row['elevation_name'], 'gray')
        folium.Marker(location=[row['latitude_deg'], row['longitude_deg']],
                      popup=row['name'],
                      icon=folium.Icon(color=color_point)).add_to(mapa_aeropuertos)

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
