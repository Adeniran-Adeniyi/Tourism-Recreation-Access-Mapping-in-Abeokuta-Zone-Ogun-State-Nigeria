import geopandas as gpd

wards = gpd.read_file("data/processed/wards.gpkg",layer="wards")
print('CRS:', wards.crs)

wards["area_wrong"]= wards.area
print(wards[["ward_name", "area_wrong"]].head(3))

print("suggested UTM:", wards.estimate_utm_crs())
ward_utm = wards.to_crs(epsg=32631)
ward_utm["area_km2"]=ward_utm.area/1000000
print(ward_utm[['ward_name','area_km2']].head(3))
print("ibadan north total:", round(ward_utm["area_km2"].sum(),1),"km2")