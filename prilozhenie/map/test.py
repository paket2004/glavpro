import folium

m = folium.Map(location=[55.751244, 37.618423], zoom_start=15, tiles="Stamen Terrain")

# Добавляем Google Satellite (неофициальный способ)
google_satellite = "https://mt1.google.com/vt/lyrs=s&x={x}&y={y}&z={z}"
folium.TileLayer(
    tiles=google_satellite,
    attr="Google Satellite",
    name="Google Satellite",
).add_to(m)

folium.LayerControl().add_to(m)
m.save("map.html")