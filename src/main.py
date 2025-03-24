import folium
import pandas as pd
import numpy as np
from scipy.spatial import ConvexHull
from folium.plugins import PolyLineTextPath

# Cargar datos
df_gull = pd.read_csv("data/gull.csv")

# Filtrar por individuos deseados
identificadores_deseados = ["PC70", "PC66", "PC71"]
df_gull = df_gull[df_gull["individual-local-identifier"].isin(identificadores_deseados)]

# Convertir fecha y filtrar por año 2010
df_gull["timestamp"] = pd.to_datetime(df_gull["timestamp"])
df_gull = df_gull[df_gull["timestamp"].dt.year == 2010]

# Renombrar columnas
df_gull.rename(columns={'individual-local-identifier': 'Pajaro', 'location-long': 'Longitud', 'location-lat': 'Latitud'}, inplace=True)

# Crear el mapa centrado en la ubicación media
m = folium.Map(location=[df_gull["Latitud"].mean(), df_gull["Longitud"].mean()], zoom_start=6)

# Asignar colores
colores = {'PC70': 'green', 'PC66': 'purple', 'PC71': 'yellow'}

# Agregar puntos y convex hulls al mapa
for pajaro, grupo in df_gull.groupby("Pajaro"):
    color = colores[pajaro]
    
    # Agregar puntos individuales
    for _, row in grupo.iterrows():
        folium.CircleMarker(
            location=[row["Latitud"], row["Longitud"]],
            radius=3, color=color, fill=True, fill_color=color, fill_opacity=0.5
        ).add_to(m)
    
    # Calcular Convex Hull si hay suficientes puntos
    if len(grupo) >= 3:
        puntos = grupo[['Latitud', 'Longitud']].values
        hull = ConvexHull(puntos)
        hull_coords = [(puntos[i, 0], puntos[i, 1]) for i in hull.vertices]
        hull_coords.append(hull_coords[0])  # Cerrar el polígono
        
        # Dibujar el Convex Hull en el mapa
        folium.Polygon(
            locations=hull_coords, 
            color=color, 
            fill=True, 
            fill_opacity=0.3, 
            tooltip=f"Gull: {pajaro}"  # Tooltip con identificador del pájaro
        ).add_to(m)

# Agregar una leyenda
legend_html = '''
<div style="
    position: fixed; 
    bottom: 30px; left: 30px; width: 200px; height: 110px; 
    background-color: white; z-index:9999; font-size:14px;
    border:2px solid grey; padding: 10px; opacity: 0.9;
">
<b> Leyenda </b><br>
<span style="color: green;">&#9679;</span> PC70 <br>
<span style="color: purple;">&#9679;</span> PC66 <br>
<span style="color: yellow;">&#9679;</span> PC71 <br>
</div>
'''
m.get_root().html.add_child(folium.Element(legend_html))

# Guardar y mostrar mapa
m.save("mapa_gull.html")
m