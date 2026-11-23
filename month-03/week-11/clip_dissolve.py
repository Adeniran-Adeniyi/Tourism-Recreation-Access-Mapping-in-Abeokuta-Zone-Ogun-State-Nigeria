import geopandas as gpd

wards = gpd.read_file("data/processed/wards.gpkg", layer="wards").to_crs(epsg=32631)
roads = gpd.read_file("data/processed/roads.gpkg", layer="roads").to_crs(epsg=32631)

agodi = wards[wards["ward_name"] =="Agodi"]

agodi_road = gpd.clip(roads, agodi)
print("Road in Agodi:", len(agodi_road))


print("Road lenght in Agodi:", round(agodi_road.length.sum() /1000, 2), "km")

# mergin wards into lagas

lgas = wards.dissolve(by="lga_name")
print(lgas.reset_index()[["lga_name"]])
print("LGA area:", round(lgas.area.iloc[0] / 1000000, 1), "km2")